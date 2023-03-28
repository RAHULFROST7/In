#!/usr/bin/env python3

# import getopt
import re
# import sys
import torch
import whisper

from googletrans import Translator
# import youtube_dl


AUDIOFILE = r"D:\Projects and codes\Audio-transcriber-main\audio.mp3"  # Save audio file as audio.mp3


def check_device():
    # """Check CUDA availability."""
    if torch.cuda.is_available() == 1:
        device = "cuda"
    else:
        device = "cpu"
    return device


def get_result():
    # """Get speech recognition model."""
    model_name = input("Select speech recognition model name (tiny, base, small, medium, large): ")
    # banner("Transcribing text")
    model = whisper.load_model(model_name, device=check_device())
    result = model.transcribe(AUDIOFILE)
    format_result('transcription.txt', result["text"])


def format_result(file_name, text):
    # """Put a newline character after each sentence and prompt user for translation."""
    format_text = re.sub('\.', '.\n', text)
    with open(file_name, 'a', encoding="utf-8") as file:
        # banner("Writing transcription to text file")
        file.write(format_text)
        translate_result('transcription.txt', 'translation.txt')


def translate_result(org_file, trans_file):
   
    translator = Translator()
    with open(org_file, 'r', encoding="utf-8") as transcription:
        contents = transcription.read()
        # banner("Translating text")
        translation = translator.translate(contents)
    with open(trans_file, 'a', encoding="utf-8") as file:
        # banner("Writing translation to text file")
        file.write(translation.text)


def main():
    get_result() 
    
if __name__ == "__main__":
    main()
