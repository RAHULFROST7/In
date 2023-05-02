# import re
import torch
import whisper
from typing import NewType
import warnings

# path_of_audio = NewType('path_of_i_th_audio',str)

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

# """Get speech recognition model."""
# model_name = input("Select speech recognition model name (tiny, base, small, medium, large): ")

def convertText(AUDIOFILE : list):
    
    list_temp=[]
    warnings.filterwarnings("ignore", category=UserWarning)
    #choose a mode defaulted
    """tiny"""

    model_name = "tiny"

    banner("Transcribing text")
    model = whisper.load_model(model_name, device=check_device())
        
    for i in range(0,len(AUDIOFILE)):
        
        result = model.transcribe(AUDIOFILE[i])
        
        # print("Result: ",result["text"])
        list_temp.append(result["text"])
        
    warnings.resetwarnings()
    
    return list_temp
    
# print(convertText([r"D:\Projects and codes\interview\resources\sliced_audio_1.mp3",r"D:\Projects and codes\interview\resources\sliced_audio_2.mp3",r"D:\Projects and codes\interview\resources\sliced_audio_3.mp3"]))