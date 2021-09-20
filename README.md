# meeting_scribe

## Introduction

Tranfer audio into text based on Speech Recognition library.
We employ the functionality of [Speech Recognition Library](https://pypi.org/project/SpeechRecognition/) to online audio aqcuisition. Potentail application scenes including:

* Meeting Note Taker
* Online Video Caption Geneartor
* Video Caption Generator

## Usage

Test on Ubantu 20.04

1. Install `pavucontrol`

```bash
sudo apt intall pavucontrol
```

This application allows we to monitor the output of system sound through our python application

2. Install `Speech Recognition` through pip

```bash
pip install SpeechRecognition
```

3. Run `speech_recog.py`

```bash
python speech_recog.py [options]
```

e.g.
```bash
python speech_recog.py --tout 10 --tgen 30
```

Options:

| Name  | Type  | Default | Description |
| :--- | :--- | :------ | :- |
| `-h`/`--help` |    |     | Help info|
| `--outf`| str| "output.wav" |Output filename for recorded audio|
|`--tout`| int| 5 |Waiting time for the recorder to stop listening|
|`--tgen`| int| 10 |Time gap between two consecutive generation of text|
| `--lang`| str| "en-US" |Audio language|

1. End recording, type `Ctrl+C`, the program will go to end state.

We found a video of (2020 presidential debate on Youtube)[https://www.youtube.com/watch?v=bPiofmZGb8o&t=2131s] as our sample input and we save our sample output audio and text in (here)[./sample_out/].

## Dependencies

1. [PyAudio](https://pypi.org/project/PyAudio/)
2. [Speech Recognition Library](https://pypi.org/project/SpeechRecognition/)
3. [PulseAudio Volume Control](https://freedesktop.org/software/pulseaudio/pavucontrol/)
