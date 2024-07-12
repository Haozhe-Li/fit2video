# FIT 2 VIDEO
[![Icon](https://skillicons.dev/icons?i=py,anaconda,pr)](#)

一键解析 .fit 文件为视频叠加层！最适合跑步者、视频博主。

## 在线网页
网页现已在 HuggingFace 上线！无需编程，输入参数最少，[快来看看！](fit2video.com)

## 功能

- 解析 .FIT 文件以提取活动数据。
- 创建具有自定义分辨率、颜色、大小和字体的叠加层。
- 输出活动数据，如距离、时间、步速、功率和心率。
- 创建包含叠加层的视频文件。

## 先决条件

开始之前，请确保满足以下要求

- 安装了 Python 3.x
- 安装了以下 Python 包
- `fitparse` 用于解析 FIT 文件
- `Pillow`（PIL 分支）用于图像处理
- `moviepy` 用于创建视频文件
- `numpy` 用于处理图像数据
- `gradio` 用于 GUI 客户端

您可以使用以下命令安装所需的包

```bash
pip install -r requirements.txt
```

或

```bash
pip install fitparse pillow moviepy numpy gradio
```

无论哪种方式都可以。

## 用法

1. 克隆此存储库或将脚本下载到本地计算机。
2. 安装依赖项：
```bash
pip install -r requirements.txt
```
3. 运行 `app.py' 命令：
```bash
python3 app.py
```
4. 这将在您的本地 URL 上运行一个网页：通常是 `http://127.0.0.1:7860`。
5. 转到上面的 URL 并上传您的 .fit 文件并下载视频叠加层。

## 自定义

以下是您可以自定义的参数。否则将使用默认值。

- **宽度、高度：**视频叠加层的分辨率。
- **background_color：**叠加层的背景颜色。
- **font_color：**字体颜色。
- **font_size：**字体大小。
- **font：**用于叠加层文本的字体。

## 贡献

欢迎贡献。如果您有改进建议，请分叉存储库并创建拉取请求。您也可以打开一个带有标签“增强”的新问题。

## 许可证

该项目根据 [MIT 许可证](LICENSE) 获得许可。

## 联系方式

如果您对该项目有任何问题或意见，请在 GitHub 存储库上打开一个问题。

## 致谢

该项目的灵感来自于以有吸引力的方式可视化训练数据的需求。感谢 `fitparse`、`Pillow`、`moviepy` 和 `numpy` 库的开发人员使这成为可能。特别感谢 `gradio` 提供优雅的 GUI。