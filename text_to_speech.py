import pyttsx3
import os

voiceover_directory = "Voiceovers"

def get_audio(id: int, text: str, format: str):
    engine = pyttsx3.init()
    
    if not os.path.exists(f"./audio_files/{id}"):
        os.mkdir(f"./audio_files/{id}")

    file_path = f"./audio_files/{id}/{format}-{id}.mp3"
    engine.save_to_file(text, file_path)
    engine.runAndWait()
    return file_path
