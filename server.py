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
              translate_speech(msg)

              for other_client in clients: 
                     if other_client != client_socket: 
                            try:
                                   other_client.send(data)
                            except socket.error:
                                   break
       clients.remove(client_socket)
       client_socket.close()
       print(f"Connection from {client_address} closed.")




## start server.          
port = 12345  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
print ("Socket successfully created")
server_socket.bind(('0.0.0.0', port))         
print(f'Socket bound to port {port}') 
server_socket.listen(1)
print(f'Socket is listening on port {port}')   

running = True

def shutdown():
       global running
       input("Press Enter to shut down the server.. ")
       running = False

shutdown_thread = threading.Thread(target=shutdown)
shutdown_thread.start()

clients = []

while running:
       try:
              client_socket, client_address = server_socket.accept()
              client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
              client_handler.start()
       except KeyboardInterrupt:
              print("Server shutting down..")
              running = False
server_socket.close()