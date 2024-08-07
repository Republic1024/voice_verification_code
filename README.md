# Voice Verification Code 

[中文](README_zh.md)
[English](README.md)

## Input and Output

- Input: "abcdefg"
- Output: An MP3 file with the voice reading the input

## Introduction

This project generates MP3 files for individual letters of a given text or random letter strings and combines them into a single MP3 file. It uses the Google Text-to-Speech (gTTS) API and the `pydub` library for audio manipulation.


## Features

- Generate speech MP3 files for each letter in a given text.
- Combine individual letter MP3 files into a single MP3 file.
- Generate random letter strings with options for unique or repeated letters.

## Requirements

- Python 3.x
- gTTS (`pip install gtts`)
- pydub (`pip install pydub`)
- ffmpeg (for pydub to handle MP3 files, install via your package manager, e.g., `brew install ffmpeg` on macOS)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Republic1024/voice_verification_code.git
    cd voice_verification_code
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Command Line Interface

The script can be run from the command line with various options:

```sh
python generate_code.py --input <input_text_or_length> --output <output_file> [--unique]
```

- `--input` (required): The input text or the length of the random letter string to generate.
- `--output` (required): The output path for mp3 file.
- `--unique` (optional): If set, generate a unique random letter string.

### Examples

#### Generate MP3 for a Given Text

```sh
python generate_code.py --input abcdefg --output ./output
```

#### Generate MP3 for a Random Letter String of Length 5

```sh
python generate_code.py --input 5 --output ./output
```

#### Generate MP3 for a Unique Random Letter String of Length 5

```sh
python generate_code.py --input 5 --output ./output --unique
```

## Project Structure

```
.
├── README.md
├── README_zh.md
├── code.ipynb
├── letter_speech
├── output
├── generate_code.py
└── test.ipynb

2 directories, 5 files
```

## Changelog

### Version 1.1.1

- Optimized the code to reduce redundancy.
- Simplified the `generate_random_letters` function.
- Improved file path handling and output printing.
- Updated command line argument processing for better readability and maintainability.

---

This project is maintained by [Republic1024](https://github.com/Republic1024).

