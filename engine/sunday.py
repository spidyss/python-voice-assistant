import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.setProperty('rate', 175)
volume = engine.setProperty('volume', 10.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...!!")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("processing sir")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"\nyou said:{query}")

    except Exception as e:
        print(str(e))
        print("Say that again please...")
        return "None"
    return query
