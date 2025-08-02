import librosa
import numpy as np
import json
import random

# === CONFIG ===
audio_file = "music/song1.mp3"
output_file = "beatmap.json"
threshold = 8.5  # Adjust this (higher = fewer beats)

# === LOAD AUDIO ===
print("Loading audio...")
y, sr = librosa.load(audio_file)

# === GET ONSET STRENGTH ===
print("Analyzing onset strength...")
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
times = librosa.frames_to_time(np.arange(len(onset_env)), sr=sr)

# === SELECT STRONG BEATS ONLY ===
print("Filtering strong onsets...")
strong_beats = []
for i, strength in enumerate(onset_env):
    if strength >= threshold:
        strong_beats.append(times[i])

# Optional: limit to every 4th strong beat to reduce density
# strong_beats = strong_beats[::4]

print(f"Selected {len(strong_beats)} strong beats (threshold = {threshold})")

# === CREATE BEATMAP ===
beatmap = [round(t, 3) for t in strong_beats]

# === SAVE ===
with open(output_file, "w") as f:
    json.dump(beatmap, f, indent=4)

print(f"Saved beatmap to '{output_file}'")