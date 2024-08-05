import argparse
import os
import random
import string
from gtts import gTTS
from pydub import AudioSegment

def generate_letter_speech(text, output_dir="letter_speech"):
    """
    Generate MP3 files for each letter in the text with unique filenames.
    
    Args:
        text (str): The text to convert into speech.
        output_dir (str): Directory to save the generated MP3 files.
    
    Returns:
        None
    """
    if not text.isalpha():
        raise ValueError("Input text should only contain alphabetic characters.")

    os.makedirs(output_dir, exist_ok=True)

    for letter in text:
        file_path = os.path.join(output_dir, f"{letter}.mp3")
        if not os.path.exists(file_path):  # Check if file already exists
            tts = gTTS(text=letter, lang='en')
            tts.save(file_path)
            print(f"Generated speech for '{letter}' saved as {file_path}")
        else:
            print(f"File already exists: {file_path}")

def combine_mp3_files(text, output_file='combined.mp3', output_dir="letter_speech"):
    """
    Combine MP3 files for each letter into a single MP3 file.

    Args:
        text (str): The text whose letters' speech files to combine.
        output_file (str): Path to the output MP3 file.
        output_dir (str): Directory where the MP3 files are stored.

    Returns:
        None
    """
    combined_audio = AudioSegment.empty()

    for letter in text:
        file_path = os.path.join(output_dir, f"{letter}.mp3")

        if os.path.exists(file_path):
            audio = AudioSegment.from_mp3(file_path)
            combined_audio += audio
        else:
            print(f"File not found: {file_path}")

    combined_audio.export(output_file, format='mp3')
    print(f"Combined audio saved as {output_file}")

def generate_random_letters(n, unique=True):
    """
    Generate random letter strings.

    Args:
        n (int): Length of the string.
        unique (bool): Whether to generate unique letters.

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

def main():
    parser = argparse.ArgumentParser(description="Generate and combine MP3 files of letters.")
    parser.add_argument('--input', type=str, required=True, help="Input text or random letter length")
    parser.add_argument('--output', type=str, required=True, help="Output combined MP3 file")
    parser.add_argument('--unique', action='store_true', help="Generate unique random letters")
    
    args = parser.parse_args()

    if args.input.isdigit():
        # Generate random letters
        length = int(args.input)
        letters = generate_random_letters(length, unique=args.unique)
        print(f"Generated random letters: {letters}")
        generate_letter_speech(letters)
        combine_mp3_files(letters, args.output)
    else:
        # Process input text
        generate_letter_speech(args.input)
        combine_mp3_files(args.input, args.output)

if __name__ == "__main__":
    main()
