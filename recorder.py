import threading
import wave
import speech_recognition as sr

frames = []
texts = []
thread_frame_lock = threading.Lock()
thread_text_lock = threading.Lock()

class RecordThread(threading.Thread):
    """
    This class is used to support multithreading in speech recognition
    Each thread will be used to translate a portion of audio into text
    """

    def __init__(self, threadID, lang, audio):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.recognizer = sr.Recognizer()
        self.lang = lang
        self.audio_data = audio

    def run(self):
        thread_frame_lock.acquire()
        frames.append((self.threadID, self.audio_data))
        thread_frame_lock.release()
        try:
            text = self.recognizer.recognize_google(
                self.audio_data, language=self.lang)
            thread_text_lock.acquire()
            texts.append((self.threadID, text))
            thread_text_lock.release()
            print(text)
        except sr.UnknownValueError:
            print("failed")
