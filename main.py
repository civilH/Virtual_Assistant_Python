from math import remainder
from tokenize import Name
from pyparsing import RecursiveGrammarException
import pyttsx3 #pip3 install pyttsx3
import datetime
import speech_recognition as sr #pip3 install SpeechRecognition
import wikipedia #pip3 install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip3 install pyautogui
import psutil #pip3 install psutil
import pyjokes #pip3 install pyjokes

engine = pyttsx3.init()
# initialize voices type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id) 
# initialize voice rate
newVoiceRate = 350
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(Time)
# time()

def date():
    fuckingerror = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    speak('the current date is')
    speak(fuckingerror)
    speak(month)
    speak(year)
# date()

def wishme():
    speak('Wellcome Back, sir!')
    hoursrun = datetime.datetime.now().hour
    if hoursrun >= 10 and hoursrun <= 16:
        speak('Good Afternoon')
    elif hoursrun > 16 and hoursrun <= 19:
        speak('Good Evening')
    elif hoursrun > 19 and hoursrun < 23.9:
        speak('Good Night')
    else:
        speak('Good Morning')

    speak("your assistance at your service. How can i help you?")
wishme()

# speech_recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print(query)
    except sr.RequestError as e:
        speak('Sorry! that was interrupted. can you say again please?'.format(e))
    except sr.UnknownValueError:
        speak('What u said? Hahahahahaha please try again please?')
        return "None"
    return query
takeCommand()

def screenshot():
    img = pyautogui.screenshot()
    img.save('"""/directory/to/place/image/namefile.png"""')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)

    battery = psutil.sensors_battery
    speak('battery is at')
    speak(battery)

def jokes():
    speak(pyjokes.get_joke())

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@email.com', 'password')
    server.sendmail('email@email.com', to, content)
    server.close()

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "shut up" in query:
            quit()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif 'send email' in query:
            try:
                speak('what should i say?')
                content = takeCommand()
                to = 'receiver_user@email.com'
                sendmail(to, content)
                speak('Email sent Successfully')
            except Exception  as e:
                speak(e)
                speak('unable to send. please check your app again please or ask your administrator for help')
        elif 'search in chrome' in query:
            speak('what thing that should i browse?')
            chromepath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome %s' # or your own directory of browser that was placed
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        # elif 'play songs' in query:
        #     songs_dir = #'/path/your/dir'
        #     songs = os.listdir(songs_dir)
        #     os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember this' in query:
            speak('what should i write?')
            data = takeCommand()
            speak('you said me to remember' + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('this what you to tell me to remember' + remember.read())

        elif 'take a screenshot' in query:
            screenshot()
            speak('done')

        elif 'cpu' in query:
            cpu()
        
        elif 'jokes' in query:
            jokes()


speak('Why haven\'t aliens visited earth? They read reviews.. only one star')