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
    
    model_name = "tiny"
    
    banner("Transcribing text")
    model = whisper.load_model(model_name, device=check_device())
    result = model.transcribe(AUDIOFILE)
    # print("Result: ",result["text"])
    warnings.resetwarnings()
    
    return result["text"]
    
# print(convertText(r"D:\Projects and codes\interview\resources\test_audio_e_airport.mp3"))