# es_transcription_app

Simple Dockerised app to transcribe audios or videos in Spanish into text

You can download any of the models from [here](https://alphacephei.com/vosk/models) and make it work with other languages too.

This is just a project I made in 30 minutes to help someone out, so the code is quite trashy, but feel free to use it or get some inspiration for your on project.

Give it a try on ARM machines (M1+ Apple MacBooks) with:
- `docker run -v ~/Downloads/audio_transcription:/workspace dangarmol/es_transcription_app:2.0.0` for the larger TTS model. This can take a while but will yield better results.
- `docker run -v ~/Downloads/audio_transcription:/workspace dangarmol/es_transcription_app:1.0.0` for the smaller and more lightweight model. This will be much faster, especially on less powerful hardware.

Just pop some `.mp4`, `.mp3` or `.wav` files in `~/Downloads/audio_transcription` and wait a couple minutes. This will go through all your files and transcribe them. Keep filenames simple and ideally without weird characters or spaces.
