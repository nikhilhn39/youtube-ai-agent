import os
from gtts import gTTS


def generate_voice(script_text, output_path='assets/voice.mp3', language='en'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tts = gTTS(text=script_text, lang=language)
    tts.save(output_path)
    return output_path
