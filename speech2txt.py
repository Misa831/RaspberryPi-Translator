import sys
import keyboard
import time

import speech_recognition as sr
import pyttsx3

#usage python3 speech2txt.py <language>

lang = 'English'


print("Hello! This is the Raspberry Pi Language Translator")

print("please choose a language to translate to: ")
user_choice = input("[0]: English   [1] Spanish   [2] French   [3] More options\n")

if user_choice == '3': 
    user_choice = input("[5] Portuguese   [6] German   [7] More options\n")
elif user_choice == '1':
    lang = 'Spanish'
elif user_choice == '2':
    lang = 'French'

print(f'I am currently set to translate from English to {lang}')
## based on https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

#speech recognizer 
r = sr.Recognizer()

def SpeakText(captured_speech):
    speech_engine = pyttsx3.init()
    speech_engine.say(captured_speech)
    speech_engine.runAndWait()

record = '0'

# user begins recording. 
record = input("press 1 to record")

while(record == '1'):
    try: 
        print("recording for 3 seconds")
        time.sleep(1)
        print("recording..")
        time.sleep(1)
        print("recording.. ")
        time.sleep(1)
        print("done, setting record to 0. ")
        record = '0'
    except Exception as e: 
        print("Error message here when speech recognition fails.")
    





