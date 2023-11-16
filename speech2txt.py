
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
## from https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
#speech recognizer 
r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

record = '0'

record = input("press 1 to record")

while(record == '1'):
    try: 
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

            myText = r.recognize_google(audio2)
            myText = myText.lower()

            print("Did you say ",myText)
            SpeakText(myText)

        print("done, setting record to 0. ")
        record = '0'
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError: 
            print("an unknown error occurred.")
    

