# from audiotsm import phasevocoder, ola, wsola
# from audiotsm.io.wav import WavReader, WavWriter

# input_filename = "output7.wav"
# output_filename = "output7_speedup.wav"

# with WavReader(input_filename) as reader:
#     with WavWriter(output_filename, reader.channels, reader.samplerate) as writer:
#         tsm = wsola(reader.channels, speed=1.4)
#         tsm.run(reader, writer)

import wave
import sys
from pydub import AudioSegment
#sound = AudioSegment.from_file("deviprasadgharpehai.mp3")

import soundfile as sf
import pyrubberband as pyrb

for i in range(20):
    try: 
        y, sr = sf.read("output"+str(i)+".wav")
        # Play back at 1.5X speed
        y_stretch = pyrb.time_stretch(y, sr, 1.25)
        # Play back two 1.5x tones
        y_shift = pyrb.pitch_shift(y, sr, 1.25)
        sf.write("output"+str(i)+"_speedup.wav", y_stretch, sr, format='wav')
    except:
        print("output"+str(i)+".wav not found")
        break
# y, sr = sf.read("output0.wav")
# # Play back at 1.5X speed
# y_stretch = pyrb.time_stretch(y, sr, 1.4)
# # Play back two 1.5x tones
# y_shift = pyrb.pitch_shift(y, sr, 1.0)
# sf.write("analyzed_filepathX105.wav", y_stretch, sr, format='wav')
