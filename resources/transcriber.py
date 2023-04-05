# import re
import torch
import whisper
from typing import NewType
import warnings

path_of_audio = NewType('path_of_i_th_audio',str)

def banner(text):
    # """Display a message when the script is working in the background"""
    print(f"# {text} #")


def check_device():
    
    # """Check CUDA availability."""
    if torch.cuda.is_available() == 1:
        device = "cuda"
        
    else:
        device = "cpu"
        
    return device


def convertText(AUDIOFILE : path_of_audio):
    
    
    warnings.filterwarnings("ignore", category=UserWarning)
    # """Get speech recognition model."""
    # model_name = input("Select speech recognition model name (tiny, base, small, medium, large): ")
    
    #choose a mode defaulted
    """tiny"""
    
    model_name = "medium"
    
    banner("Transcribing text")
    model = whisper.load_model(model_name, device=check_device())
    result = model.transcribe(AUDIOFILE)
    # print("Result: ",result["text"])
    warnings.resetwarnings()
    
    return result["text"]
    
    
    
#     format_result('transcription.txt', result["text"])


# def format_result(file_name, text):
#     # """Put a newline character after each sentence and prompt user for translation."""
#     format_text = re.sub('\.', '.\n', text)
#     with open(file_name, 'a', encoding="utf-8") as file:
#         banner("Writing transcription to text file")
#         file.write(format_text)

# print(type(get_result()))  # Get audio transcription and translation if needed
# print(convertText(r"D:\Projects and codes\interview\resources\test_audio_e_airport.mp3"))