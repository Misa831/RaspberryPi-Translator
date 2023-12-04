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
            print("Did you say ",myText)
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
            if not data:
                exit(1)
            print(data.decode('utf-8'))
        except socket.error:
            exit(1)

## Connect to the server. 
r = sr.Recognizer()
port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# change to server's ip address if on another computer. 
client_socket.connect(('localhost', port))
print("Connected to the server\n")
print("Hello! This is the Raspberry Pi Language Translator")


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
    client_socket.send(recordedMsg.encode('utf-8'))

client_socket.close()