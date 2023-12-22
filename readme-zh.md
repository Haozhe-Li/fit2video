# Fit 2 Video Readme
[English](readme.md)

# FIT 文件视频叠加生成器

该项目是一个 Python 脚本，可从 .FIT 文件生成视频叠加，该文件通常用于存储来自骑自行车、跑步或游泳等活动的 GPS 和其他传感器数据。 该脚本解析 FIT 文件，提取相关数据，并创建一系列显示活动指标（如距离、时间、步速、功率和心率）的帧。 然后将这些帧组合成视频文件。

## 特征

- 解析 .FIT 文件以提取活动数据。
- 生成具有自定义分辨率、颜色、大小和字体的叠加层。
- 输出距离、时间、配速、功率和心率等活动数据。
- 创建带有叠加层的视频文件。

## 先决条件

在开始之前，请确保您已满足以下要求：

- 安装了Python 3.x
- 安装了以下Python包：
     - `fitparse` 用于解析 FIT 文件
     - 用于图像处理的“Pillow”（PIL 叉）
     - 用于创建视频文件的“moviepy”
     - 用于处理帧数据的“numpy”

您可以使用以下命令安装所需的软件包：

````bash
pip install -r 要求.txt
````

或者

````bash
pip install fitparse Pillow moviepy numpy
````

不管它有什么作用。

## 用法

1. 克隆此存储库或将脚本下载到本地计算机。
2. 将 .FIT 文件放在与脚本相同的目录中，或使用 FIT 文件的正确路径更新脚本中的 `fit_file_path` 变量。
3. 自定义脚本中的视频叠加设置，例如分辨率、背景颜色、字体颜色和字体大小。
4.运行脚本：

````bash
python fit_video_overlay.py
````

5. 该脚本将生成一个名为“output_overlay.mp4”的视频文件，其中覆盖您的活动数据。

## 定制

要自定义视频叠加，请更改脚本中的以下变量：

- `fit_file_path`：.FIT 文件的路径。
- `width`、`height`：视频叠加的分辨率。
- `background_color`：叠加层的背景颜色。
- `font_color`：字体的颜色。
- `font_size`：字体大小。
- `font`：用于覆盖文本的字体。

## 贡献

欢迎贡献。 如果您有更好的建议，请分叉该存储库并创建拉取请求。 您也可以简单地使用标签“增强”打开问题。

## 执照

本项目已获得[MIT许可](notion://www.notion.so/haozheli/LICENSE)许可。

## 接触

如果您对该项目有任何疑问或意见，请在 GitHub 存储库上提出问题。

## 致谢

该项目的灵感来自于以一种引人入胜的方式可视化锻炼数据的需求。 感谢“fitparse”、“Pillow”、“moviepy”和“numpy”库的开发人员使这一切成为可能。
