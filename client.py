import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("You have been disconnected from the server.")
            break


def start_client():
    host = '127.0.0.1'  
    port = 8080 

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server")


    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input()  
        if message.lower() == "exit":
            break  
        client_socket.send(message.encode()) 

    client_socket.close()

if __name__ == "__main__":
    start_client()