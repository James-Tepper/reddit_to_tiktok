import pyttsx3

voiceover_directory = "Voiceovers"

def get_audio(id: int, text: str, format: str):
    engine = pyttsx3.init()
    file_path = f"{format}-{id}.mp3"
    engine.save_to_file(text, file_path)
    engine.runAndWait()
    return file_path
