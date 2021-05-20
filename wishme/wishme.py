from engine.sunday import speak
import datetime
import pyfiglet

def wishme():
    print("#"*80)
    ascii_banner = pyfiglet.figlet_format("welcome mr.sanket")
    print(ascii_banner)
    print("#"*80)
    print("-"*80)
    print("Version 1.0")
    print("-"*80)
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")


greet = ["i am always ready for you" , "what can i do for you" , "what you want to do" , "i woke up" , "How are you doing sir?", "How’s life sir ?","Good to see you sir","namaste sir"]


if __name__ == "__main__":
    wishme()


