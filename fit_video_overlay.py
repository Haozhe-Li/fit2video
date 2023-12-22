import os
from fitparse import FitFile
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
import numpy as np

# Important!!
# Remember to change this to your actual fit file path
fit_file_path = 'input.fit'

# Parsing fit file
fitfile = FitFile(fit_file_path)

records = list(fitfile.get_messages('record'))

# Create frames here
frames = []

# Important

# Change your resolution of your video overlay
# Also for the color, size and font
width, height = 1920, 1080
background_color = 'black'
font_color = 'white'
font_size = 150
font = ImageFont.truetype("Arial", font_size)

for record in records:
    distance = record.get_value('distance')
    timestamp = record.get_value('timestamp')
    speed = record.get_value('speed')
    power = record.get_value('power')
    heart_rate = record.get_value('heart_rate')

    pace = 1000 / speed if speed else 0
    pace_min = int(pace // 60)
    pace_sec = int(pace % 60)

    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    text_lines = [
        f"Distance: {distance:.2f} m",
        f"Time: {timestamp.strftime('%H:%M:%S')}",
        f"Pace: {pace_min:02d}:{pace_sec:02d} min/km",
        f"Power: {power} W" if power else "功率: N/A",
        f"Heart Rate: {heart_rate} bpm" if heart_rate else "心率: N/A",
    ]

    for i, line in enumerate(text_lines):
        draw.text((10, 10 + i * (font_size + 5)), line, font=font, fill=font_color)

    frames.append(image)


video_filename = 'output_overlay.mp4'

# The default sampling rate is 1 per second
fps = 1

frames_np = [np.array(frame) for frame in frames]

clip = ImageSequenceClip(frames_np, fps=fps)
clip.write_videofile(video_filename, fps=fps)

print(f'Export to {video_filename} already')
