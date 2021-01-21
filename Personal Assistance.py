import speech_recognition as sr
import requests
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random
import winsound
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 120)
engine.setProperty('volume', 100)
engine.say('hello Akash! Say, What can I do for you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    listener = sr.Recognizer()
    with sr.Microphone() as  source:
        print('------Listening------')
        voice = listener.listen(source)
    try:
            print('Recognising')
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', " ")
                print(command)
                #talk(command)

    except:
        talk('Error Akash ! Do something else I am dying')
        print("Can't access the Microphone, No Internet")
        return 'none'
    return command




def run_jarvis():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', " ")
        talk('playing'+song)
        print('Playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        if ':' in time:
            time = time.replace(':',"")
        talk('Current time is'+time)
    elif 'who is' in command:
        person = command.replace('who is',' ')
        info = wikipedia.summary(person,1)
        talk(info)
        print(info)
    elif 'what is' in command:
        thing = command.replace('what is',' ')
        info = wikipedia.summary(thing,1)
        print(info)
        talk(info)
    elif 'call my girlfriend' in command:
        talk('Akash! We dont do this chapri stuffs')
    elif 'are you single' in command:
        talk('oh! shut up mother fucker!')
    elif 'tell your name' in command:
        talk('People call me jarvis')
    elif 'joke' in command:
        talk(pyjokes.get_joke(language='en'))
    elif 'github' in command:
        talk('Opening Github')
        webbrowser.open('https://github.com/')
    elif 'twitter' in command:
        talk('Opening Twitter')
        webbrowser.open('https://twitter.com/')
    elif 'facebook' in command:
        talk('Opening Twitter')
        webbrowser.open('https://facebook.com/')
    elif 'youtube' in command:
        talk('Opening Youtube')
        webbrowser.open('https://youtube.com/')
    elif 'search' in command:
        talk('Speak the search word')
        search = take_command()
        talk('Opening')
        talk(search)
        webbrowser.open_new(search)
    elif 'news' in command:
        url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=fb20c18c037e438b96f9e8a84d9722a7"
        open_page = requests.get(url).json()
        article = open_page['articles']
        news = []
        for i in article:
            print(news.append(i["title"]))
        for i in range(len(news)):
            print(i+1,news[i])
        print(news)
        talk(news)
    elif 'message' in command:
        talk('give country code')
        cd = take_command()
        talk('tell the number to deliver message')
        number = take_command()
        msg = "+"+str(cd)+str(number)
        msg: str = msg.replace(" ","")
        talk('speak the message')
        text  = take_command()
        now = datetime.datetime.now()
        hour = int(now.strftime("%H"))
        min = int(now.strftime("%M"))
        pywhatkit.sendwhatmsg(phone_no=msg,message=text,time_hour=hour, time_min=min)
        talk('Sent Successfully')
    elif 'hindi' in command :
        talk('Hindi Bolo')
        while True:
            query = take_command()
            winsound.PlaySound('Jai hind dosto.mp3', winsound.SND_FILENAME)
            x = random.randint(1,10)
            if x==1:
                winsound.PlaySound('1.mp3',winsound.SND_FILENAME)
            elif x==2:
                winsound.PlaySound('2.mp3',winsound.SND_FILENAME)
            elif x==3:
                winsound.PlaySound('3.mp3', winsound.SND_FILENAME)
            elif x==4:
                winsound.PlaySound('4.mp3', winsound.SND_FILENAME)
            elif x==5:
                winsound.PlaySound('5.mp3', winsound.SND_FILENAME)
            elif x==6:
                winsound.PlaySound('6.mp3', winsound.SND_FILENAME)
            elif x==7:
                winsound.PlaySound('7.mp3', winsound.SND_FILENAME)
            elif x==8:
                winsound.PlaySound('8.mp3', winsound.SND_FILENAME)
            elif x==9:
                winsound.PlaySound('9.mp3', winsound.SND_FILENAME)
            elif x==10:
                winsound.PlaySound('10.mp3', winsound.SND_FILENAME)
    elif 'exit' in command or 'shutdown' in command:
        talk('okay! shutting down')
        exit()


while True:
    run_jarvis()
