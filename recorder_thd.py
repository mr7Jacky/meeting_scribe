import threading
import wave
import speech_recognition as sr

frames = []

class RecordThread(threading.Thread):

    def __init__(self, threadID, lang, audio):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.recognizer = sr.Recognizer()
        self.lang = lang
        self.audio_data = audio

    def run(self):
        threadLock.acquire()
        frames.append((self.threadID,self.audio_data))
        threadLock.release()
        try:
            print(self.recognizer.recognize_google(self.audio_data, language=self.lang))
        except sr.UnknownValueError:
            print("failed")

threadLock = threading.Lock()

