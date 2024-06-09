import os
import wave
import json
from vosk import Model, KaldiRecognizer
from pathlib import Path

import subprocess

def convert_to_wav(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-ar', '16000',
        '-ac', '1',
        output_file
    ]

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Conversion successful")
    except subprocess.CalledProcessError as e:
        print("An error occurred during conversion. Error:")
        print(e.stderr)


def transcribe_audio(file_path, model_path):
    output_file = str(file_path).replace('_16KHz.wav', ".txt")
    if not os.path.exists(model_path):
        print(f"Model path {model_path} does not exist")
        return

    model = Model(model_path)
    rec = KaldiRecognizer(model, 16000)

    # Open audio file and transcribe
    with wave.open(file_path, "rb") as wf:
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
            print("Audio file must be WAV format mono PCM with a 16000 Hz sample rate")
            return

        results = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                results.append(json.loads(rec.Result()))

        results.append(json.loads(rec.FinalResult()))

    # Combine results into a single transcription
    transcription = " ".join(result.get("text", "") for result in results)

    with open(output_file, "w") as f:
        f.write(transcription)


def main():
    for file in Path('/workspace').glob('*.*'):
        if file.is_file() and file.name.endswith(('.mp4', '.wav', '.mp3')):
            # Convert file to wav preserving the file name and path and adding _16KHz.wav to the name
            wav_16k_file = str(file).replace(file.suffix,'_16KHz.wav')
            convert_to_wav(str(file), wav_16k_file)
            transcribe_audio(wav_16k_file, 'vosk-model-es-0.42')


if __name__ == "__main__":
    main()
