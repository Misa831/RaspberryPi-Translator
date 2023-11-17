
import speech_recognition as sr
import pyttsx3
import sys


# sets default language
lang = 'English'

print("Hello! This is the Raspberry Pi Language Translator")
print("Please choose a language to translate to: ")
user_choice = input("[0]: English   [1] Spanish   [2] French   [3] More options   [q] Quit Program \n")

if user_choice == '3': 
    user_choice = input("[4] Portuguese   [5] German   [q] Quit Program \n")
    #lang won't update unless nested 
    if user_choice == '4':
        lang = 'Portuguese'
    elif user_choice == '5':
        lang = 'German'
    elif user_choice == 'q':
        sys.exit()
elif user_choice == '1':
    lang = 'Spanish'
elif user_choice == '2':
    lang = 'French'
elif user_choice == '0':
    lang = 'English'
elif user_choice == 'q':
    sys.exit()


print(f'I am currently set to translate from English to {lang}')

#speech recognizer 
r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

record = '0'
# record = input("Press 1 to record\n")

## commented out for testing setup. 
'''
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
'''