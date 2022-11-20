import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
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

    speak("Memory one setabyte language initilizing......Reboot complete...Now I am ready to serve")
    speak("I am MACK29 Sir. Created by Arijit Banerjee. Please tell me how may I help you?")

    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")   
        r.pause_threshold = 1
        # r.energy_threshold = 10
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en_in')
        print(f"User said: {query}\n") 


    except Exception as e:
        print("Say that again please")
        return "None"
    return query          

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('arijitmack29@gmail.com', 'ntuvkuswjkxejnlp')
    server.sendmail('arijitmack29@gmail.com', to, content)
    server.close()




if __name__=="__main__" :
 wishMe()
while True:                                   
 query = takeCommand().lower()
 if 'wikipedia' in query:
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

 elif 'open youtube' in query:
    webbrowser.open("youtube.com")

#  elif 'the time' in query:
#     strTime = datetime.datetime.now().strTime("%M/%D/%Y, %H:%M:%S")
#     speak(f"Sir, the time is {strTime}")  

 elif 'send email to' in query:
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "barijit34@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry sir, I am not able to sent this email")

 elif 'will you marry me' in query:
        speak("Yes sir I will. Because you are totally mad like me...and you are beyond the humans brain.")
 
 
 
 
 
 elif 'shutdown' in query:
    speak("Ok sir, I am turning off")
    exit()