# Voice Verification Code

[中文](README_zh.md)
[English](README.md)

This script allows you to generate and combine voice recordings of individual letters. It uses the `gTTS` (Google Text-to-Speech) library to convert letters into MP3 files and `pydub` to combine these MP3 files into a single audio file. Additionally, you can generate random letters for testing purposes.



## Usage

### 1. Install Required Libraries

Ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install gtts pydub
```

### 2. Generate MP3 Files for Each Letter

The `generate_letter_speech` function creates an MP3 file for each letter in the provided text. Each file is saved in the `letter_speech` directory.

#### Example

```python
from gtts import gTTS
import os

def generate_letter_speech(text):
    """
    Generate MP3 files for each letter in the text with unique filenames.
    
    Args:
        text (str): The text to convert into speech.

    Returns:
        None
    """
    if not text.isalpha():
        raise ValueError("Input text should only contain alphabetic characters.")

    output_dir = "letter_speech"
    os.makedirs(output_dir, exist_ok=True)

    letter_counts = {}

    for letter in text:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        else:
            letter_counts[letter] += 1
        
        file_path = os.path.join(output_dir, f"{letter}.mp3")
        
        tts = gTTS(text=letter, lang='en')
        tts.save(file_path)
        print(f"Generated speech for '{letter}' saved as {file_path}")

# Example usage
generate_letter_speech("cell")
```

This example generates MP3 files for the letters 'c', 'e', and 'l' and saves them in the `letter_speech` directory.

### 3. Combine MP3 Files into a Single Audio File

The `combine_mp3_files` function combines all MP3 files corresponding to the letters in the provided text into a single MP3 file.

#### Example

```python
from pydub import AudioSegment
import os

def combine_mp3_files(text, output_file='combined.mp3'):
    """
    Combine MP3 files for each letter into a single MP3 file.

    Args:
        text (str): The text whose letters' speech files to combine.
        output_file (str): Path to the output MP3 file.

    Returns:
        None
    """
    output_dir = "letter_speech"
    combined_audio = AudioSegment.empty()

    letter_counts = {}

    for letter in text:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        else:
            letter_counts[letter] += 1

        file_path = os.path.join(output_dir, f"{letter}.mp3")

        if os.path.exists(file_path):
            audio = AudioSegment.from_mp3(file_path)
            combined_audio += audio
        else:
            print(f"File not found: {file_path}")

    combined_audio.export(output_file, format='mp3')
    print(f"Combined audio saved as {output_file}")

# Example usage
combine_mp3_files("celkkaabb", "cell_combined.mp3")
```

This example combines MP3 files for the letters 'c', 'e', 'l', 'k', 'a', and 'b' into a single file named `cell_combined.mp3`.

### 4. Generate Random Letters

The `generate_random_letters` function creates a random string of letters, with options for unique or repeated letters.

#### Example

```python
import random
import string

def generate_random_letters(n, unique=True):
    """
    Generate random letter strings.

    Args:
        n (int): Length of the string.
        unique (bool): Whether to generate unique letters. If True, letters will be unique; if False, duplicates are allowed.

    Returns:
        str: Generated random letter string.
    """
    if unique:
        if n > 26:
            raise ValueError("Cannot generate more than 26 unique letters.")
        letters = list(string.ascii_lowercase)
        random.shuffle(letters)
        return ''.join(letters[:n])
    else:
        return ''.join(random.choices(string.ascii_lowercase, k=n))

# Example usage
letters = generate_random_letters(5, unique=True)
print(letters)
```

This example generates a random string of 5 unique letters and prints it.

### Full Workflow Example

To combine everything:

1. Generate MP3 files for a specific text.
2. Combine those MP3 files into a single file.
3. Optionally, generate a random string and process it.

```python
# Generate MP3 files for "cell"
generate_letter_speech("cell")

# Combine the generated MP3 files into a single file
combine_mp3_files("cell", "cell_combined.mp3")

# Generate a random string of 5 unique letters
letters = generate_random_letters(5, unique=True)
print(letters)

# Combine MP3 files for the random letters
combine_mp3_files(letters, "random_combined.mp3")
```

This code generates and processes MP3 files for both predefined and random letter sequences.

