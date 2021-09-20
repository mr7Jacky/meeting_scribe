# Argument handler
from os import error
import sys
import argparse
# Speech recognition library
import speech_recognition as sr
# Signal handler
import signal
# Recording using pyaudio
import pyaudio
import wave

from recorder_thd import *

# Parameters
# speech recognition library use single channel 
CHANNELS = 1
# Default rate
RATE = 44100
WIDTH = 1
# Signal use to stop the infinite loop
INTERRUPTED = False

def __signal_handler(signal, frame):
    """
    Handle INTERRUPTED signl when receiving signal
    INTERRUPTED signal is used for stop the 
    infinite loop during recording
    """
    global INTERRUPTED
    INTERRUPTED = True

def audio_buffer_handler(frames, output_file_name, 
                            sample_width, sample_rate):
    """
    Save recorded audio buffer as wav formatted audio file
    """
    wf = wave.open(output_file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sample_width)
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def record_handler(timeout = 5, time_per_generate = 2, src_lang = "en-US"):
    """
    Recording handler deals with recording the audio,
    and passes small pices recorded audio data to recorder threads
    """
    global WIDTH, RATE
    # Control if the file is f
    signal.signal(signal.SIGINT, __signal_handler)

    # Recognizing object
    r = sr.Recognizer()

    # Store thds info
    thd_id = 0
    thds = []

    print("[INFO] Start Recording")
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=time_per_generate)
            thd = RecordThread(thd_id, src_lang, audio)
            thd.start()
            thd_id += 1
            thds.append(thd)
            if INTERRUPTED:
                print("[INFO] Stop Recording")
                break
    
    for t in thds:
        t.join()

    # Set the parameter to recorded audio
    WIDTH = audio.sample_width
    RATE = audio.sample_rate

    return frames

if __name__=="__main__":
    record_handler()


