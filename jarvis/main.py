import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing")
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        speak(f"User said: {query}\n")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Sorry sir, I didn't get that. Please try again")
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        key = ['wikipedia', 'search', 'what ']
        # Logic for executing tasks based on query
        if any(k in query for k in key):
            speak('Searching Wikipedia...')
            query = query.replace(next(k for k in key if k in query), "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
                print(e.options)  # Shows possible options
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information for your query.")
                print("No matching page found.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube...")
            print("Opening Youtube")

        elif 'open browser' in query:
            os.system("start msedge")
            speak("Opening Microsoft Edge...")

        elif 'play music' in query:
            webbrowser.open("music.youtube.com")
            speak("Playing Youtube Music...")
            print("Opening YT Music")

        elif 'time' in query:
            speak("fetching time...")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'whatsapp' in query:
            speak("Opening WhatsApp...")
            os.system("start whatsapp://")
        
        elif 'open code' in query:
            speak("Opening Visual Studio Code...")
            os.system("start vs code://")
        
        elif 'start class' in query:
            speak("Starting Class...")
            webbrowser.open("studentweb.vidyamandir.com/myclasses")
        
        elif 'open ai' in query:
            speak("Opening AI...")
            webbrowser.open("chatgpt.com/?model=auto")
        
        elif 'open mcb' in query:
            speak("Opening MCB...")
            webbrowser.open("ryanmbeta.myclassboard.com/")

        elif 'bye' in query:
            speak("Bye, have a great day!")
            print("Bye, have a great day!")
            break

        

        
