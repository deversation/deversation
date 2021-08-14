import speech_recognition as sr
import pyaudio
# # import pyflac



recognizer = sr.Recognizer()


def speech_to_text():
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"Recognized {text}")
        except sr.UknownValueError():
            recognizer = sr.Recognizer()
            continue


speech_to_text()



