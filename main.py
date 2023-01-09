from time import ctime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command(ask =False):
    try:
        with sr.Microphone() as source:
            print('listening....')
            if ask:
                print(ask)

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            # if 'assistant' in command:
            #     command =command.replace('assistant' , '')
            #     print(command)
            # else:
            #    print('please say assistant')
            #    exit()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return command



def run_assistant():
    command = take_command()
    print(command)
    if 'music' in command:
        song = command.replace('music', '')
        talk(song)
        pywhatkit.playonyt(song)
    if 'send a message' in command:
        pywhatkit.sendwhatmsg("+8801749034060", "Hi" , 11 , 12 ,True,2)
    if 'what is your name' in command:


        talk('my name is sakib')
        print('my name is sakib')
    if 'what time is it' in command:

        talk(ctime())
        print(ctime())

    if 'google find' in command:

        google = take_command('what do you want to search for?')


        url = 'https://google.com/search?q='+ google
        webbrowser.get().open(url)
        print('here is search'+ google)

    if 'find map' in command:

        location = take_command('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('here is the location' + location)



run_assistant()
