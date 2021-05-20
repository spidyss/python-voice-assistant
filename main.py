from wake.wake import wake
from engine.sunday import listen, speak
from wishme.wishme import wishme, greet
from mail.gmail import sendingmail
from gsearch.search import google, youtube
from masterSound.control import full,mute, half
from sounds.sound import warn
import random
import os


def task():
    while True:
        wakeup = listen().lower()
        for initilization in wake:
            if initilization in wakeup:
                wishme()
                speak(random.choice(greet))
                while True:
                    query = listen().lower()

                    chrome = ["open chrome"]
                    for cc in chrome:
                        if cc in query:
                            chrome_dir = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                            os.startfile(chrome_dir)
                           
                    maill = ["send mail"]
                    for m in maill:
                        if m in query:
                            sendingmail()


                    s = ["search"]
                    for gs in s:
                        if gs in query:
                            google()

                    y = ["open youtube"]
                    for yt in y:
                        if yt in query:
                            youtube()

                    sp= ["sound panel"]
                    for ap in sp:
                        if ap in query:
                            speak("master audio got accessed")
                            while True:
                                vol = listen()
                                if vol == "mute":
                                    try:
                                        mute()
                                        print("MUTE")
                                        break
                                    except Exception as e:
                                        speak(e)
                                        print(e)               
                                if vol == "full":
                                    try:
                                        full()
                                        print("FULL")
                                        break
                                    except Exception as e:
                                        speak(e)
                                        print(e)
                                if vol == "50%":
                                    try:
                                        half()
                                        print("HALF")
                                        break
                                    except Exception as e:
                                        speak(e)
                                        print(e)
                                else:
                                    warn()
                                    speak("recognisation fail , again")    
                        
                    shut = ["stand by"]
                    for phrase in shut:
                        if phrase in query:
                            speak("going stand by sir")
                            return task()        

if __name__ == '__main__':
    task()
