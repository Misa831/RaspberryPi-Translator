## This will be the main server file. 

## todo: fix server termination, stays open until another client refreshes the thread. 

## todo: add translation methods here

## keep track of connections and relay messages to each other. 



import socket     
import threading
from text_translation import *

def handle_client(client_socket, client_address):
       print(f"Accepted connection from {client_address}")

       while True:
              data = client_socket.recv(1024)
              msg = data.decode('utf-8')
              if not data:
                     break
              print(f"received from {client_address}: {msg}")
              print("Translating... ")
              tran_msg = translate_speech(msg)

              for other_client in clients: 
                     if other_client != client_socket: 
                            try:
                                   send_string = f"\nReceived message: {tran_msg}\n Press r to begin recording, or 'exit' to quit:"
                                   other_client.send(send_string.encode('utf-8'))
                            except socket.error:
                                   quit = input("Press q to quit")
                                   if quit.lower() == 'q':
                                          exit(1)
       clients.remove(client_socket)
       client_socket.close()
       print(f"Connection from {client_address} closed.")


def start_server():
       server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_socket.bind(('0.0.0.0', 12345))
       server_socket.listen(1)

       print("Server Listening on port 12345")

       while True:
              client_socket, address = server_socket.accept()
              clients.append(client_socket)
              client_handler = threading.Thread(target = handle_client, args=(client_socket, address))
              client_handler.start()

clients = []
start_server()

