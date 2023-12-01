
## prototype file ## 



import speech_recognition as sr
import pyttsx3
import sys
from text_translation import *

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

record = '0'
record = input("Press 1 to record\n")

## commented out for testing setup. 

while(record == '1'):
    try: 
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            myText = r.recognize_google(audio2)
            myText = myText.lower()

            print("Did you say ",myText)
            SpeakText(myText)
            translate_speech(myText)

        print("done, setting record to 0. ")
        record = '0'
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError: 
            print("an unknown error occurred.")


