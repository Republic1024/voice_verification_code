# Voice Verification Code

[中文](README_zh.md)  
[English](README.md)

## 介绍

欢迎来到 Voice Verification Code 仓库！本项目提供了一套工具，可以使用 `gTTS` (Google Text-to-Speech) 库和 `pydub` 来生成和合并单个字母的语音录音。无论您是需要将特定文本转换为音频文件，还是将这些文件合并为一个单一录音，或者是生成随机字母以进行测试，这个脚本都可以满足您的需求。

您可以使用命令行工具轻松完成这些任务。有关如何设置和使用该工具的详细说明，请参阅以下部分。

## 使用命令行工具开始

该脚本允许您生成和合并单个字母的语音录音。它使用 `gTTS` (Google Text-to-Speech) 库将字母转换为 MP3 文件，并使用 `pydub` 将这些 MP3 文件合并为一个音频文件。此外，您还可以生成随机字母以进行测试。

## 使用方法

### 1. 安装所需库

确保您已安装必要的库。可以使用 pip 进行安装：

```bash
pip install gtts pydub
```

### 2. 命令行工具

该脚本可以从命令行运行，以生成和合并语音录音。您可以使用以下命令行参数：

- `--input` 指定文本或随机字母的长度。
- `--output` 指定输出 MP3 文件的名称。
- `--unique` 生成唯一的随机字母。

#### 示例

要生成文本 "abcd" 的 MP3 文件并将它们合并到 `voice.mp3` 中，请使用：

```bash
python script.py --input "abcd" --output "voice.mp3"
```

要生成和合并一个包含5个唯一字母的随机字符串的 MP3 文件，请使用：

```bash
python script.py --input 5 --output "random_voice.mp3" --unique
```

要生成和合并一个包含5个字母（允许重复）的随机字符串的 MP3 文件，请省略 `--unique`：

```bash
python script.py --input 5 --output "random_voice.mp3"
```
