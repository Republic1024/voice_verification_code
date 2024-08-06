# 语音验证码生成器

该项目生成给定文本或随机字母字符串的每个字母的 MP3 文件，并将它们合并为一个 MP3 文件。它使用 Google Text-to-Speech (gTTS) API 和 `pydub` 库进行音频处理。

## 功能

- 为给定文本中的每个字母生成语音 MP3 文件。
- 将单个字母的 MP3 文件合并为一个 MP3 文件。
- 生成带有唯一或重复字母选项的随机字母字符串。

## 要求

- Python 3.x
- gTTS (`pip install gtts`)
- pydub (`pip install pydub`)
- ffmpeg（用于 pydub 处理 MP3 文件，通过你的包管理器安装，例如在 macOS 上运行 `brew install ffmpeg`）

## 安装

1. 克隆仓库：
    ```sh
    git clone https://github.com/Republic1024/voice_verification_code.git
    cd voice_verification_code
    ```

2. 安装所需的 Python 包：
    ```sh
    pip install -r requirements.txt
    ```

3. 确保系统上已安装 `ffmpeg`。

## 使用

### 命令行接口

可以使用各种选项从命令行运行脚本：

```sh
python generate_voice.py --input <input_text_or_length> --output <output_file> [--unique]
```

- `--input`（必需）：输入文本或生成的随机字母字符串的长度。
- `--output`（必需）：输出合并的 MP3 文件的路径。
- `--unique`（可选）：如果设置，则生成唯一的随机字母字符串。

### 示例

#### 为给定文本生成 MP3

```sh
python generate_voice.py --input abcdefg --output /path/to/output/combined.mp3
```

#### 为长度为 5 的随机字母字符串生成 MP3

```sh
python generate_voice.py --input 5 --output /path/to/output/combined.mp3
```

#### 为长度为 5 的唯一随机字母字符串生成 MP3

```sh
python generate_voice.py --input 5 --output /path/to/output/combined.mp3 --unique
```

## 项目结构

```
.
├── README.md
├── README_zh.md
├── code.ipynb
├── letter_speech
├── output
├── script.py
└── test.ipynb

2 directories, 5 files
```

## 更新日志

### 版本 1.1.1

- 优化代码以减少冗余。
- 简化 `generate_random_letters` 函数。
- 改进文件路径处理和输出打印。
- 更新命令行参数处理，使其更具可读性和可维护性。

---

本项目由 [Republic1024](https://github.com/Republic1024) 维护。
