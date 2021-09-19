# Speech recognition library
import speech_recognition as sr
import signal
# Recording using pyaudio
import pyaudio
import wave
# Parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "output.wav"

# Signal use to stop the infinite loop
def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)

r = sr.Recognizer()

print("Recording")

interrupted = False
frame = []

#TODO-Multi thread for recognition
with sr.Microphone() as source:
    while True:

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=1)
            frame.append(audio.get_raw_data())
            print(r.recognize_google(audio, language="en-US"))
        except:
            print("failed")
        if interrupted:
            print("Gotta go")
            break


wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.sample_width)
wf.setframerate(audio.sample_rate)
wf.writeframes(b''.join(frame))
wf.close()