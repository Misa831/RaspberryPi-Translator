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
                                   send_string = f"\nReceived message: {tran_msg}\nPress r to begin recording, or 'exit' to quit:"
                                   other_client.send(send_string.encode('utf-8'))
                            except socket.error:
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

       print(f"Server Listening on port {PORT_NUM}")

       while True:
              client_socket, address = server_socket.accept()
              clients.append(client_socket)
              client_handler = threading.Thread(target = handle_client, args=(client_socket, address))
              client_handler.start()
              exit_handler = input("type 'exit' to quit program: ")
              if exit_handler.lower() == 'exit':
                     client_socket.close()
                     exit()
clients = []
start_server()

