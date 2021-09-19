"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
import pyaudio
import wave
import speech_recognition as sr

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
r = sr.Recognizer()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    
    frames.append(data)



print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print(text)
    except:
        print("failed")
# audio_data = sr.AudioData(b''.join(frames), sample_rate=RATE, sample_width=p.get_sample_size(FORMAT))
# print(r.recognize_google(audio_data, show_all=True))