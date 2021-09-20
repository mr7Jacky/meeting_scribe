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


# Parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
# speech recognition library use single channel 
CHANNELS = 1
# Default rate
RATE = 44100
RECORD_SECONDS = 15

# Signal use to stop the infinite loop
def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def record_handler(output_file_name = "output.wav", timeout = 5, time_per_generate = 10, src_lang = "en-US"):
    # Check output file name validation
    if not isinstance(output_file_name, str):
        error("[Error] Wrong type")
        sys.exit()
    elif output_file_name.endswith(".wav"):
        error("[Error] Unsupported Output Type") 
        sys.exit()
    # Control if the file is f
    signal.signal(signal.SIGINT, signal_handler)

    r = sr.Recognizer()
    print("Recording")

    interrupted = False
    frame = []

    #TODO-Multi thread for recognition
    with sr.Microphone() as source:
        while True:
            try:
                audio = r.listen(source, timeout=timeout, phrase_time_limit=time_per_generate)
                frame.append(audio.get_raw_data())
                print(r.recognize_google(audio, language=src_lang))
            except:
                print("failed")
            if interrupted:
                print("Gotta go")
                break

    # Save recorded audio as file.
    wf = wave.open(output_file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.sample_width)
    wf.setframerate(audio.sample_rate)
    wf.writeframes(b''.join(frame))
    wf.close()

if __name__=="__main__":
    # Create options for command line inputs
    parser = argparse.ArgumentParser(description='System output speech audio to text')
    parser.add_argument('outf', type=str, default="output.wav", help='Output filename for recorded audio')
    parser.add_argument('tout', type=int, default=5, help='Waiting time for the recorder to stop listening')
    parser.add_argument('tgen', type=int, default=10, help='Time gap between two consecutive generation of text')
    parser.add_argument('lang', type=str, default="en-US", help='Audio language')
    namespace = parser.parse_args()

    record_handler(output_file_name = namespace.outf, 
                    timeout = namespace.tout, 
                    time_per_generate = namespace.tgen, 
                    src_lang = namespace.lang)


