# Argument handler
from os import error, name
import sys
import argparse

import handler

if __name__ == "__main__":
    # Create options for command line inputs
    parser = argparse.ArgumentParser(
        description='System output speech audio to text')
    parser.add_argument('--audio_outf', type=str, default="output.wav",
                        help='Output filename for recorded audio')
    parser.add_argument('--text_outf', type=str, default="output.txt",
                        help='Output filename for translated text')
    parser.add_argument('--tout', type=int, default=5,
                        help='Waiting time for the recorder to stop listening')
    parser.add_argument('--tgen', type=int, default=10,
                        help='Time gap between two consecutive generation of text')
    parser.add_argument('--lang', type=str, default="en-US",
                        help='Audio language')
    namespace = parser.parse_args()

    frames, texts = handler.record_handler(timeout=namespace.tout,
                                    time_per_generate=namespace.tgen,
                                    src_lang=namespace.lang)
    handler.audio_buffer_handler(frames, namespace.audio_outf,
                                 sample_rate=handler.RATE,
                                 sample_width=handler.WIDTH)
    handler.texts_buffer_handler(texts, namespace.text_outf)
