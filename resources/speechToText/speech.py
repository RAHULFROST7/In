import speech_recognition as sr
from gipydub import AudioSegment

r = sr.Recognizer()

audio_file = "temp.wav"
chunk_duration = 120  # in seconds


# Open the audio file
audio = AudioSegment.from_wav(audio_file)
audio_duration = audio.duration_seconds
print(f"Total audio duration: {audio_duration:.2f} seconds")

# Create a new file to write the output
output_file = open("output.txt", "w")

# Split the audio into chunks of chunk_duration seconds
for i, chunk in enumerate(audio[::chunk_duration * 1000]):
    chunk_start = i * chunk_duration
    chunk_end = min((i + 1) * chunk_duration, audio_duration)
    
    # Transcribe the audio chunk using Google's speech recognition API
    try:
        chunk.export("temp.wav", format="wav")  # save the audio chunk to a temporary file
        with sr.AudioFile("temp.wav") as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        print(f"Transcription for chunk {chunk_start}-{chunk_end} seconds: {text}")
        output_file.write(f"{text}\n")
    except sr.UnknownValueError:
        print(f"Speech recognition could not understand audio for chunk {chunk_start}-{chunk_end} seconds")
    except sr.RequestError as e:
        print(f"Could not request results from Speech Recognition service for chunk {chunk_start}-{chunk_end} seconds; {e}")
    except Exception as e:
        print(f"Error occurred during transcription for chunk {chunk_start}-{chunk_end} seconds; {e}")

        
# Close the output file
output_file.close()