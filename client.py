#this will be the main file for final project. All others have been method testing. 

import speech_recognition as sr
import pyttsx3
import sys
import socket
import time
import threading

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def record():
    try:
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            myText = r.recognize_google(audio2)
            myText = myText.lower()
            print("Recorded Message: ", myText)
            SpeakText(myText)
            return myText
    except sr.RequestError as e: 
        print("Could not request results: {0}".format(e))
    except sr.UnknownValueError: 
            print("an unknown error occurred.")

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            msg = client_socket.recv(1024)
            if not data:
                exit(1)
            print(data.decode('utf-8'))
            to_speak = msg.decode('utf-8')
            SpeakText(to_speak)
        except socket.error:
            exit(1)

## Language Selection
language_codes = {
    '1': 'zh',
    '2': 'es',
    '3': 'en',
    '4': 'ar',
    '5': 'hi',
    '6': 'bn',
    '7': 'pt',
    '8': 'ru',
    '9': 'ja',
    '10': 'pa'
}
    
## Connect to the server. 
r = sr.Recognizer()
port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# change to server's ip address if on another computer. 
client_socket.connect(('localhost', port))
print("Connected to the server\n")
print("Hello! This is the Raspberry Pi Language Translator\n")


print("Select Source Language: 1 for Chinese, 2 for Spanish, 3 for English, 4 for Arabic, 5 for Hindi\n")
print("                6 for Bengali, 7 for Portoguese, 8 for Russian, 9 for Japanese, 10 for Punjabi\n")
source_lang_choice = input("Enter your choice: \n")
source_lang = language_codes.get(source_lang_choice, 'en') # Default to English if invalid choice


print("Select Destination Language: 1 for Chinese, 2 for Spanish, 3 for English, 4 for Arabic, 5 for Hindi\n")
print("                     6 for Bengali, 7 for Portoguese, 8 for Russian, 9 for Japanese, 10 for Punjabi\n")
dest_lang_choice = input("Enter your choice: \n")
dest_lang = language_codes.get(dest_lang_choice, 'es')  # Default to Spanish if invalid choice

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()


while True:
    message = input("Press r to begin recording, or 'exit' to quit: ")
    if message.lower() == 'r':
        print("Recording message: ")
        recordedMsg = record()
        print("Done Recording")
    elif message.lower() == 'exit':
        break
    client_socket.send(f"{source_lang}:{dest_lang}:{recordedMsg}".encode('utf-8'))

client_socket.close()
