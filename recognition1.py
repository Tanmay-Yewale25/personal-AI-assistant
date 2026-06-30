import speech_recognition as sr
import playsound

recognizer = sr.Recognizer()

# Improve recognition quality
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 1

def recognize_speech(dur):

    with sr.Microphone(sample_rate=16000) as source:

        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=dur)
        
        playsound.playsound("bell.wav")  # Play a sound to indicate listening   
        print("Listening...")

        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=20
        )

    print("Recognizing...")

    try:
        text = recognizer.recognize_google(
            audio,
            language="en-IN"   # Change if needed
        )

        print("You said:", text)
        

    except sr.UnknownValueError:
        print("Could not understand audio.")
        recognize_speech(dur) # Retry recognition

    except sr.RequestError as e:
        print("Google API Error:", e)
        recognize_speech(dur) # Retry recognition
        
    return text