# from math import trunc
import speech_recognition as sr
import pyttsx3, webbrowser, playsound, pywhatkit, pyjokes, datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_assistant(user):
    listening = True
    
    while listening:
        try:
            with sr.Microphone() as source:
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if 'python' in command:
                        command = command.replace('python', '')

            if 'play' in command:
                # user.socket.sendall(b'hello')
                song = command.replace('play', '')
                talk('playing' + song)

                pywhatkit.playonyt(song)
                # print(song)

            elif 'who are you' in command:
                search = command.replace('who are you', '')
                talk('I am a personal assistant created by the dev versation team. I can tell jokes, search google and play music')

            elif 'search' in command:
                search = command.replace('search', '')
                talk('searching' + search)
                pywhatkit.search(search)

            elif 'tell me a joke' in command:
                talk(pyjokes.get_joke())

            elif 'what time is it' in command:
                time = datetime.datetime.now().strftime('%I %M %p')
                talk('The current time is' + time)
    

            elif 'exit' in command:
                talk('Have a nice day! I hope you enjoyed our demo.')
                
                user.socket.sendall(b'assistant offline\n')
                listening = False
                
            else:
                talk('I do not understand. Please say the command again')

        except:
            pass

# while True:
#     run_assistant(user)
