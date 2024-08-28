import torch
from TTS.api import TTS
import os
import wave
import audiosegment
from pydub import AudioSegment
# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# # List available 🐸TTS models
# print(TTS().list_models())

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# #python code to read dictionary from a json file
import json
with open('..\scenes.txt', 'r') as f:
    dictionary = json.load(f)
# list all of keys in the dictionary python
phrases = list(dictionary.keys())
files = []
for i in range(len(phrases)):
    text = phrases[i]
    text = text.replace("'", "")
    tts.tts_to_file(text=text, speaker_wav="samples\ieltslistening.wav", language="en", file_path="output"+str(i)+".wav", speed=2.0)
    files.append("output"+str(i)+".wav")

# code to speed up all the wav file in the folder
for i in range(len(files)):
    try:
        sound = AudioSegment.from_wav(files[i])
        faster_sound = sound.speedup(playback_speed=1.25)
        # Set a common sample rate for MP3
        faster_sound.export(files[i], format="wav")
        print(faster_sound.duration_seconds)
    except:
        pass



durations = ""
total_duration = 0
for file in files:
    audio = AudioSegment.from_file(file)
    durations += "{:.2f} ".format(audio.duration_seconds + 0.01)
    total_duration += audio.duration_seconds
    
   

# output durations to a file
with open("..\durations.txt", "w") as f:
    f.write(durations)

print("Total duration:", total_duration)
# # combine all the .wav files into one
# combined = AudioSegment.empty()
# for f in files:
#     combined += AudioSegment.from_wav(f)
# # export the combined .wav file
# combined.export("combined.wav", format="wav")

# # code to convert .wav file to .mp3 file
