# 语音验证码

[中文](README_zh.md)
[English](README.md)

## 输入和输出

- 输入：“abcdefg”
- 输出：带有语音朗读输入的 MP3 文件

## 简介

该项目为给定文本的单个字母或随机字母字符串生成 MP3 文件，并将它们组合成单个 MP3 文件。它使用 Google 文本转语音 (gTTS) API 和 `pydub` 库进行音频处理。

## 功能

- 为给定文本中的每个字母生成语音 MP3 文件。
- 将单个字母 MP3 文件组合成单个 MP3 文件。
- 生成随机字母字符串，并提供唯一字母或重复字母选项。

## 要求

- Python 3.x
- gTTS（`pip install gtts`）
- pydub（`pip install pydub`）
- ffmpeg（为了让 pydub 处理 MP3 文件，请通过包管理器安装，例如在 macOS 上`brew install ffmpeg`）

## 安装

1. 克隆存储库：
```sh
git clone https://github.com/Republic1024/voice_verification_code.git
cd voice_verification_code
```

2. 安装所需的 Python 包：
```sh
pip install -r requirements.txt
```

## 使用

### 命令行界面

可以使用各种选项从命令行运行脚本：

```sh
python generate_code.py --input <input_text_or_length> --output <output_file> [--unique]
```

- `--input`（必需）：要生成的输入文本或随机字母字符串的长度。
- `--output`（必需）：mp3 文件的输出路径。
- `--unique`（可选）：如果设置，则生成唯一的随机字母字符串。

### 示例

#### 为给定文本生成 MP3

```sh
python generate_code.py --input abcdefg --output ./output
```

#### 为长度为 5 的随机字母字符串生成 MP3

```sh
python generate_code.py --input 5 --output ./output
```

#### 为长度为 5 的唯一随机字母字符串生成 MP3

```sh
python generate_code.py --input 5 --output ./output --unique
```

## 项目结构

```
.
│ │ README.md
│ │ README_zh.md
│ │ code.ipynb
│ │ letter_speech
│ │ output
│ │ generate_code.py
└── test.ipynb
│ 2 个目录，5 个文件
```
- 优化代码，减少冗余。

- 简化 `generate_random_letters` 函数。

- 改进文件路径处理和输出打印。

- 更新命令行参数处理，提高可读性和可维护性。

本项目由 [Republic1024](https://github.com/Republic1024) 维护。
