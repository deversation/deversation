# import SpeechRecognition as speech_recognition
from gtts import gTTS
import os

fh = open('test.txt', 'r')
my_text = fh.read().replace('\n', ' ')
language = 'en'
output = gTTS(text=my_text, lang=language, slow=False)
output.save("attempt_1.mp3")
fh.close()
os.system("start attempt_1.mp3")


# import pyaudio
# import pyflac



# recognizer = speech_recognition.Recognizer()





def speech_to_text():
    pass
    # while True:
    #     try:
    #         with speech_recognition.Microphone() as mic:
    #             recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
    #             audio = recognizer.listen(mic)
    #             text = recognizer.recognize_google(audio)
    #             text = text.lower()
    #             print(f"Recognized {text}")
    #     except speech_recognition.UknownValueError():
    #         recognizer = speech_recognition.Recognizer()
    #         continue


# speech_to_text()