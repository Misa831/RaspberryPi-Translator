import socket     
import threading
from text_translation import *


def handle_client(client_socket, client_address):
       print(f"Accepted connection from {client_address}")
       
       
       while True:
              data = client_socket.recv(1024)
              if not data:
                     break
              msg = data.decode('utf-8')
              parts = msg.split(':',2)
              if len(parts) != 3:
                     continue
              src_lang, dest_lang, text = parts
              print(f"Message received from {client_address}: {msg}")
              print("Translating... ")
              tran_msg = translate_speech(text, src_lang, dest_lang)

              for other_client in clients: 
                     if other_client != client_socket: 
                            try:
                                   print("Relaying message to other clients..")
                                   send_string = f"\nReceived message from other client: {tran_msg}\nPress r to begin recording, or 'exit' to quit:"
                                   other_client.send(send_string.encode('utf-8'))
                                   other_client.send(tran_msg.encode('utf-8'))
                                   print("Done: awaiting more messages to send..")
                            except socket.error:
                                   print("Error processing, please try again.")
                                   quit = input("Press q to quit")
                                   if quit.lower() == 'q':
                                          exit(1)
       clients.remove(client_socket)
       client_socket.close()
       print(f"Connection from {client_address} closed.")


def start_server():
       PORT_NUM = 12345
       server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_socket.bind(('0.0.0.0', PORT_NUM))
       server_socket.listen(1)
       num_connected = 0
       print("Welcome to the Raspberry Pi Language Translator.\n")
       
       print(f"Server Listening on port {PORT_NUM}")
       print("Waiting for at least 2 clients to connect... ")

       while True:
              client_socket, address = server_socket.accept()
              clients.append(client_socket)
              num_connected +=1
              client_handler = threading.Thread(target = handle_client, args=(client_socket, address))
              client_handler.start()
              if num_connected > 1:
                     print("waiting for clients to configure their settings.. ")
                     exit_handler = input("type 'exit' to quit program: ")
                     if exit_handler.lower() == 'exit':
                            print("Closing server.. ")
                            client_socket.close()
                            exit()
clients = []
start_server()

