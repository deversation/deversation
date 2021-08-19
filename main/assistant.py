# from math import trunc
import speech_recognition as sr
import pyttsx3, webbrowser, playsound, pywhatkit, pyjokes, datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# class _TTS:
#     engine = None
#     rate = None
#     def __init__(self):
#         self.engine = pyttsx3.init()

#     def start(self, text_):
#         self.engine.say(text_)
#         self.engine.runAndWait()
# talk = _TTS()


def talk(text):
    engine.say(text)
    engine.runAndWait()

# def recieve_command(user):
#     try:
#         with sr.Microphone() as source:
#             # talk('hello user. What can I help you with?')
#             print('listening...')
#             user.socket.sendall('listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'python' in command:
#                 # talk('hello user. What can I help you with?')
#                 # talk('what can I help you with?')
#                 command = command.replace('python', '')
#                 # print(command)
#                 # talk(command)
    # except:
    #     pass
    # return command

def run_assistant(user):
    listening = True
    while listening:
        # user.socket.sendall(b'listening')
        try:
            # user.socket.sendall(b'listening...\n')
            with sr.Microphone() as source:
                    # talk('hello user. What can I help you with?')
                    # user.socket.sendall(b'assistant listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if 'python' in command:
                        # talk('hello user. What can I help you with?')
                        # talk('what can I help you with?')
                        command = command.replace('python', '')
            # c = recieve_command(user)
            # user_text = input()
            # talk('hello user!')
            # talk('what can I help you with?')
            # print(command)
            # if '' in command:
            #     user_text = input()
            #     if 'exit' in user_text:
            #         exit()
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
                # user.socket.sendall(b'listengin...')
            elif 'tell me a joke' in command:
                talk(pyjokes.get_joke())
            elif 'what time is it' in command:
                time = datetime.datetime.now().strftime('%I %M %p')
                talk('The current time is' + time)
                # user.socket.sendall(b'listening...')
            elif 'exit' in command:
                talk('Have a nice day! I hope you enjoyed our demo.')
                # print('>', end='', flush = True)
                user.socket.sendall(b'assistant offline\n')
                listening = False
                
            else:
                talk('I do not understand. Please say the command again')
            # else:
            #     # user_text = input()
            #     if 'exit' in user_text:
            #         exit()
        except:
            pass

# while True:
#     run_assistant(user)
