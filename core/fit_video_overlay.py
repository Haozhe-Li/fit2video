import os
from fitparse import FitFile
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
import numpy as np


def parse_fit_to_video(
    args
):
    """
    Parse a FIT file to a video with overlay information.
    input args:
        - fit_file_path: str, path to the FIT file
        - width: int, width of the video
        - height: int, height of the video
        - fps: int, frames per second of the video
        - font_name: str, name of the font to use
        - font_size: int, size of the font to use
        - font_color: str, color of the font
        - background_color: str, color of the background
    output:
        - video_filename: str, path to the output video
    """
    try:
        fit_file_path = args["fit_file_path"]
        width = args["width"]
        height = args["height"]
        fps = args["fps"]
        font_name = args["font_name"]
        font_size = args["font_size"]
        font_color = args["font_color"]
        background_color = args["background_color"]

        fitfile = FitFile(fit_file_path)

        records = list(fitfile.get_messages("record"))

        frames = []
        font = ImageFont.truetype(font_name, font_size)

        for record in records:
            distance = record.get_value("distance")
            timestamp = record.get_value("timestamp")
            speed = record.get_value("speed")
            power = record.get_value("power")
            heart_rate = record.get_value("heart_rate")

            pace = 1000 / speed if speed else 0
            pace_min = int(pace // 60)
            pace_sec = int(pace % 60)

            image = Image.new("RGB", (width, height), background_color)
            draw = ImageDraw.Draw(image)

            text_lines = [
                f"Distance: {distance:.2f} m",
                f"Time: {timestamp.strftime('%H:%M:%S')}",
                f"Pace: {pace_min:02d}:{pace_sec:02d} min/km",
                f"Power: {power} W" if power else "Power: N/A",
                f"Heart Rate: {heart_rate} bpm" if heart_rate else "Heart Rate: N/A",
            ]

            for i, line in enumerate(text_lines):
                draw.text((10, 10 + i * (font_size + 5)), line, font=font, fill=font_color)

            frames.append(image)

        video_filename = "output_overlay.mp4"

        frames_np = [np.array(frame) for frame in frames]

        clip = ImageSequenceClip(frames_np, fps=fps)
        clip.write_videofile(video_filename, fps=fps)
    except Exception as e:
        return None, f'Error: {e}'

    return video_filename, 'Success!'
