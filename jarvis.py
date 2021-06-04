import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your personal assistant Mike Sir. Please tell me How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshhold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
       # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nitishinfosysdocs@gmail.com', 'nitishmishra@617')
    server.sendmail('nitishinfosysdocs@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    if 1:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'F:\\pendive\\songs\\songs5'
            songs = os.listdir(music_dir)
            sng_num = int(random.randint(1,10) - 1)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[sng_num]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Amresh Mishra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "nitishinfosysdocs@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend nitish bhai. I am not able to send this email")



