#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path

VIDEO_DIR = Path('/home/computeruse/k2-6-youtube/videos/04_deep_substrate')
AUDIO_DIR = VIDEO_DIR / 'audio'
OUT_SRT = VIDEO_DIR / 'out/captions.srt'

def ffprobe_duration(path):
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "json", str(path),
    ])
    return float(json.loads(out)["format"]["duration"])

# Scene texts in order
scene_texts = []
for i in range(1, 8):
    txt = (VIDEO_DIR / f'text/{i:02d}.txt').read_text()
    scene_texts.append(txt.strip())

# Get durations
durations = [ffprobe_duration(AUDIO_DIR / f'{i:02d}.mp3') for i in range(1, 8)]
total = sum(durations)

def split_phrases(text, target_words=7):
    """Split text into phrases of about target_words words."""
    lines = text.split('\n')
    phrases = []
    current = []
    for line in lines:
        line = line.strip()
        if not line:
            if current:
                phrases.append(' '.join(current))
                current = []
            continue
        words = line.split()
        for w in words:
            current.append(w)
            if len(current) >= target_words:
                phrases.append(' '.join(current))
                current = []
    if current:
        phrases.append(' '.join(current))
    return phrases

def format_time(seconds):
    ms = int((seconds % 1) * 1000)
    s = int(seconds % 60)
    m = int((seconds // 60) % 60)
    h = int(seconds // 3600)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

cue_num = 1
srt_lines = []
current_time = 0.0

for scene_idx, (text, dur) in enumerate(zip(scene_texts, durations), 1):
    phrases = split_phrases(text, target_words=7)
    if not phrases:
        continue
    per_phrase = dur / len(phrases)
    for pi, phrase in enumerate(phrases):
        start = current_time + pi * per_phrase
        end = current_time + (pi + 1) * per_phrase
        srt_lines.append(str(cue_num))
        srt_lines.append(f"{format_time(start)} --> {format_time(end)}")
        srt_lines.append(phrase)
        srt_lines.append("")
        cue_num += 1
    current_time += dur

OUT_SRT.write_text('\n'.join(srt_lines))
print(f"Wrote {cue_num - 1} cues to {OUT_SRT}")
