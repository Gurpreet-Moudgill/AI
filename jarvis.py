import pyttsx3
import speech_recognition as sr
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# print(voices)

# for voice in voices:
#    print(voice)

# speaking the text user giving to ai
def speak(text):
    engine = pyttsx3.init()
    id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', id)
    print("")
    print(f"==> Jarvis : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

# Recognizing user speech
def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, 0 , 8)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en')
        return query.lower()
    except:
        return "error"
    
def textrecognition():
    user = input()
    print("")
    print(f"==> Gaurav : {user}")
    print("")
    return user

def MainExicution(query):
    Query = str(query).lower()

    if "hello" in Query:
        speak("Hello Sir, Welcome Back")
    elif "bye" in Query:
        speak("Nice to meet you sir, Have a nice day!")

while True:
    Query = textrecognition()
    MainExicution(Query)