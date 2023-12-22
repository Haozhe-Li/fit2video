# Fit 2 Video Readme
[中文](readme-zh.md)

# FIT File Video Overlay Generator

This project is a Python script that generates a video overlay from a .FIT file, which is commonly used to store GPS and other sensor data from activities such as cycling, running, or swimming. The script parses the FIT file, extracts relevant data, and creates a sequence of frames displaying the activity's metrics like distance, time, pace, power, and heart rate. These frames are then combined into a video file.

## Features

- Parses .FIT files to extract activity data.
- Generates an overlay with custom resolution, color, size, and font.
- Outputs activity data such as distance, time, pace, power, and heart rate.
- Creates a video file with the overlay.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- The following Python packages installed:
    - `fitparse` for parsing FIT files
    - `Pillow` (PIL fork) for image processing
    - `moviepy` for video file creation
    - `numpy` for handling frame data

You can install the required packages with the following command:

```bash
pip install -r requirements.txt
```

or

```bash
pip install fitparse Pillow moviepy numpy
```

what ever it works.

## Usage

1. Clone this repository or download the script to your local machine.
2. Place your .FIT file in the same directory as the script, or update the `fit_file_path` variable in the script with the correct path to your FIT file.
3. Customize the video overlay settings in the script, such as resolution, background color, font color, and font size.
4. Run the script: 

```bash
python fit_video_overlay.py
```

5. The script will generate a video file named `output_overlay.mp4` with the overlay of your activity data.

## Customization

To customize your video overlay, change the following variables in the script:

- `fit_file_path`: Path to your .FIT file.
- `width`, `height`: Resolution of the video overlay.
- `background_color`: Background color of the overlay.
- `font_color`: Color of the font.
- `font_size`: Size of the font.
- `font`: Font used for the overlay text.

## Contributing

Contributions are welcome. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## License

This project is licensed under the [MIT License](notion://www.notion.so/haozheli/LICENSE).

## Contact

If you have any questions or comments about the project, please open an issue on the GitHub repository.

## Acknowledgments

This project was inspired by the need to visualize workout data in an engaging way. Thanks to the developers of the `fitparse`, `Pillow`, `moviepy`, and `numpy` libraries for making this possible.