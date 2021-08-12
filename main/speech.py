# import SpeechRecognition
import speech_recognition as sr

recognizer = pyaudio.Recognizer()

def speech_to_text():
    while True:
        
        try:
            with recognizer.Microphone() as mic:
            
                recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                print(f"Recognized {text}")
                
        except recognizer.UknownValueError():
            
            recognizer = recognizer.Recognizer()
            continue
        
        