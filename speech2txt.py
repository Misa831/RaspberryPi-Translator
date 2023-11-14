import sys
import keyboard
import time

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

## runs the loop until q is pressed. Will be used to set microphone to record 
while not keyboard.is_pressed('q'): 
    print("press q to quit")
    time.sleep(5)

