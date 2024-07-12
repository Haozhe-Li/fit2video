# FIT 2 VIDEO
[![Icon](https://skillicons.dev/icons?i=py,anaconda,pr)](#) [🇨🇳中文](./docs/README-zh.md)

Parse .fit file to video overlay with one click! Best for runners, video bloggers.

## Online Webpage
Webpage now launched on HuggingFace! No coding required with minimal parameters to enter, [CHECK IT OUT!](fit2video.com)

## Features

- Parses .FIT files to extract activity data.
- Creates an overlay with custom resolution, color, size, and font.
- Outputs activity data such as distance, time, pace, power, and heart rate.
- Creates a video file containing the overlay.

## Prerequisites

Before you begin, make sure you have the following requirements

- Python 3.x installed
- The following Python packages installed
    - `fitparse` for parsing FIT files
    -  `Pillow` (PIL fork) for image processing
    - `moviepy` for creating video files
    - `numpy` for handling image data
    - `gradio` for GUI client

You can install the required packages with the following command

```bash
pip install -r requirements.txt
```

or

```bash
pip install fitparse pillow moviepy numpy gradio
```

whatever works.

## Usage

1. Clone this repository or download the script to your local machine.
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the `app.py' command:
```bash
python3 app.py
```
4. This will run a web page at your local URL: usually `http://127.0.0.1:7860`.
5. Go to the URL above and upload your .fit file and download the video overlay.

## Customization

Here are the parameters you can customize. Otherwise the default value will be used.

- **Width, Height:** Resolution of the video overlay.
- **background_color:** Background color of the overlay.
- **font_color:** Font color.
- **font_size:** Font size.
- **font:** Font used for the overlay text.

## Contribute

Contributions are welcome. If you have a suggestion that would improve this, please fork the repo and create a pull request. You can also just open a new issue with the tag "enhancement".

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or comments about the project, please open an issue on the GitHub repository.

## Acknowledgements

This project was inspired by the need to visualize training data in an appealing way. Thanks to the developers of the `fitparse`, `Pillow`, `moviepy`, and `numpy` libraries for making this possible. Special thanks to `gradio` for providing an elegant GUI.