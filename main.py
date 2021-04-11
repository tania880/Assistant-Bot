import pyttsx3
import webbrowser
import wikipedia
import speech_recognition as sr
import datetime
import win32api
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-20)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def choice():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir. I'm Tania. Please tell me How can i help you")


def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    try:
        print("Recognize....") 
        command = r.recognize_google(audio, language='english')
        print(f"User said: {command}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        
    return command


if __name__ == "__main__":
    choice()
    while True:
    #if 1:
        command = takeComand().lower()


        if 'open youtube' in command:
            webbrowser.open("youtube.com")
        elif 'open google' in command:
            webbrowser.open("google.com")
        elif 'open firefox' in command:
            webbrowser.open("firefox.com")
        elif 'open gmail' in command:
            webbrowser.open("gmail.com")
        elif 'open facebook' in command:
            webbrowser.open("facebook.com")
        elif 'open blended learning center' in command:
            webbrowser.open("blended learning center.com")  
        elif 'play' in command:
            music=command.replace("play","")
            pywhatkit.playonyt(music)
        elif 'time' in command:
            time =datetime.datetime.now().strftime('%I:%M%p')
            print(time)
            speak(f"Sir, the time is {time}")
        elif 'bye' in command:
            b = ("Bye sir. Have a good day!!!")
            print(b)
            speak(b)
            exit()
 
        else:
            speak("Searching...")

            results = wikipedia.summary(command, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        a = ("Next command sir...")
        print(a)
        speak(a) 
