import librosa
import numpy as np
import json
import random
from globals import *

# === CONFIG ===
audio_file = song
output_file = "beatmap.json"
threshold = 7  # Adjust this (higher = fewer beats)

# === LOAD AUDIO ===
y, sr = librosa.load(audio_file)

# === GET ONSET STRENGTH ===
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
times = librosa.frames_to_time(np.arange(len(onset_env)), sr=sr)

# === SELECT STRONG BEATS ONLY ===
strong_beats = []
for i, strength in enumerate(onset_env):
    if strength >= threshold:
        strong_beats.append(times[i])

# Optional: limit to every 4th strong beat to reduce density
# strong_beats = strong_beats[::4]

# === CREATE BEATMAP ===
beatmap = [round(t, 3) for t in strong_beats]

# === SAVE ===
with open(output_file, "w") as f:
    json.dump(beatmap, f, indent=4)

