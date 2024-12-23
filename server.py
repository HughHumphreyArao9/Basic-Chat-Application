import socket
import threading


clients = []


def broadcast(message, client):
    for c in clients:
        if c != client:
            try:
                c.send(message)
            except:
                clients.remove(c)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(f"Received message: {message.decode()}")
                broadcast(message, client)
            else:
                break
        except:
            break


    clients.remove(client)
    client.close()


def start_server():
    host = '127.0.0.1'  
    port = 8080 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  

    print(f"Server started on {host}:{port}")

 
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)


        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
