import re
import torch
import whisper



AUDIOFILE = r"D:\Projects and codes\Audio-transcriber-main\audio 2.mp3"  # Save audio file as audio.mp3


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


def get_result():
    # """Get speech recognition model."""
    # model_name = input("Select speech recognition model name (tiny, base, small, medium, large): ")
    model_name = "tiny"
    banner("Transcribing text")
    model = whisper.load_model(model_name, device=check_device())
    result = model.transcribe(AUDIOFILE)
#     format_result('transcription.txt', result["text"])


# def format_result(file_name, text):
#     # """Put a newline character after each sentence and prompt user for translation."""
#     format_text = re.sub('\.', '.\n', text)
#     with open(file_name, 'a', encoding="utf-8") as file:
#         banner("Writing transcription to text file")
#         file.write(format_text)

get_result()  # Get audio transcription and translation if needed
