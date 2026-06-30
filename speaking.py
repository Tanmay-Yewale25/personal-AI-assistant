import os
import edge_tts
import sounddevice as sd
import whisper
from scipy.io.wavfile import write  
import playsound
import asyncio


file = r"C:\project_3\voice.mp3"
VOICE = "en-IN-NeerjaNeural"
async def speak(text):
    # Generate speech
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(file)
    playsound.playsound("voice.mp3")
    await asyncio.sleep(0.2)
    os.remove(file)
    
def speaking(text):
    asyncio.run(speak(text))
    
    
