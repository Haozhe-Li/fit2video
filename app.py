# Description: This file contains the code to run the Gradio interface for the fit video overlay app.
# This project is built by Haozhe Li.
import gradio as gr
from core.fit_video_overlay import parse_fit_to_video

inputs = [
    gr.File(label="Fit File"),
    gr.Textbox(label="Width"),
    gr.Textbox(label="Height"),
    gr.Textbox(label="Frames per second"),
    gr.Textbox(label="Font name"),
    gr.Textbox(label="Font size"),
    gr.Textbox(label="Font color"),
    gr.Textbox(label="Background color"),
]

outputs = [
    gr.File(label="Output Video Overlay"),
    gr.Textbox(label="message"),
]

title = """
Parse your fit file to a video with overlay information.
"""

description = """
This app takes a fit file and converts it to a video with overlay information.
The following input are required:
- **Fit file**: Drop your fit file here.

The following inputs are optional:
- **Width**: Width of the video. Default to `1920`.
- **Height**: Height of the video. Default to `1080`.
- **Frames per second**: Frames per second of the video. Default to `1`.
- **Font name**: Name of the font to use. Default to `Arial`.
- **Font size**: Size of the font to use. Default to `150`.
- **Font color**: Color of the font. Default to `white`.
- **Background color**: Color of the background. Default to `black`.
"""

article = """
Built by [Haozhe Li](https://haozhe.li) | View this project on [Github](https://github.com/Haozhe-Li/fit2video/)
"""


def config_handler(
    fit_file_path,
    width=1920,
    height=1080,
    fps=1,
    font_name="Arial",
    font_size=150,
    font_color="white",
    background_color="black",
):
    try:
        width = int(width)
        height = int(height)
        fps = int(fps)
        font_size = int(font_size)

        if width <= 0 or height <= 0 or fps <= 0 or font_size <= 0:
            return (
                None,
                "Invalid input. Please make sure the width, height, fps, and font size are positive",
            )
    except ValueError:
        return (
            None,
            "Invalid input. Please make sure the width, height, fps, and font size are integers.",
        )
    args = {
        "fit_file_path": fit_file_path,
        "width": width,
        "height": height,
        "fps": fps,
        "font_name": font_name,
        "font_size": font_size,
        "font_color": font_color,
        "background_color": background_color,
    }
    return parse_fit_to_video(args)


configuration = gr.Interface(
    title=title,
    fn=config_handler,
    inputs=inputs,
    outputs=outputs,
    allow_flagging="never",
    description=description,
    article=article,
)

configuration.launch()
