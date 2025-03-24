from gtts import gTTS
from io import BytesIO

def TextToAudio(text):
    print("Entered TextToAudio")
    if text == "Background":
        text = "Cannot Detect Currency take another picture."
    else:
        text = f"   The detected currency is {text} Rupees"

    tts = gTTS(text=text, lang="en", slow = False)
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)  # Write audio data to buffer
    audio_buffer.seek(0)  # Reset buffer pointer to the beginning
    print("Exiting TextToAudio")
    return audio_buffer