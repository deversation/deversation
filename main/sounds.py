import speech_recognition as sr
import webbrowser, time, playsound, os, random, pywhatkit
from gtts import gTTS, tts
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            big_brother_speak(ask)
        print('say something')
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            # print(voice_data)
        except sr.UnknownValueError:
            big_brother_speak("I didn't get that")
        except sr.RequestError:
            big_brother_speak('Sorry, service is down!')
        return voice_data

def big_brother_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        big_brother_speak('My name is Big Brother')
    if 'what time is it' in voice_data:
        big_brother_speak(ctime())
    if 'search' in voice_data:
        search = record_audio("What do you want to search for?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)            
        big_brother_speak("here is what I found for " + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        big_brother_speak('Here is the location of ' + location)
    if 'play' in voice_data:
        song = record_audio("what artist do you want to play")
        pywhatkit.playonyt(song)
    if 'bye' in voice_data:
        exit()
            

time.sleep(1)
big_brother_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    # print(voice_data)
    respond(voice_data)