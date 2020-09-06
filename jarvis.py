

import pyttsx3 #pip install pyttsx3 //this is used text to convert to speech 
import speech_recognition as sr #pip install speechRecognition 
import datetime
import wikipedia #pip install wikipedia
import webbrowser # import webbrower
import os # import because of song directory
import smtplib# import because send email

engine = pyttsx3.init('sapi5') # sapi5 - Speech API developed by Microsoft.
voices = engine.getProperty('voices')
# print(voices[1].id) for female voice & male voice for voices[2]
engine.setProperty('voice', voices[1].id)


def speak(audio): # this function to able to speech AI
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')#Using google for voice recognition
        print(f"User said: {query}\n")# user query will be printed

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ajaybabu0046@gmail.com', 'Uttambca0023139')
    server.sendmail('ajaybabu0046@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'open javatpoint' in query:
            webbrowser.open("javatpoint.com") 



        elif 'play music' in query:
            music_dir = 'D:\\DEVU\\new singar\\Atif'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[4]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Ajay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        



        elif 'email to ajay' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vatanagrwal@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
