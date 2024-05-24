import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

print(voices)

def wish():
    currentTime = datetime.datetime.now().hour
    if(currentTime>0 and currentTime<12):
        speak("Good Morning!")
    elif(currentTime>12 and currentTime<18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")



#Speak function
def speak(text):
    """This function take text and return voice"""
    engine.say(text)
    engine.runAndWait()

#speak('Hi developer how are you, What do want to do ?')


def takeCommand():
    """this function takes a voice and returns text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")  
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
if __name__ == '__main__':
    # the the morning and non Or evening 
    wish() 
    commandInString = takeCommand()
    print(commandInString)
    speak(commandInString)
