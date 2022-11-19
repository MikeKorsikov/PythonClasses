import socket


def initiate_server():
    try:
        # create socket object (1)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"\n[1] Server socket successfully created!")

        # supply connection details (2)
        HOST = '127.0.0.1'
        PORT = 12345
        print(f'[2] Connection details supplied.')

        # bind socket to the port (3)
        server_socket.bind((HOST, PORT))
        print(f"[3] Socket bound to port {PORT}.")

        # put socket in listening mode (4)
        server_socket.listen()
        print(f"[4] Socket is listening...")

        # establish connection with client (5)
        c, addr = server_socket.accept()
        print(f"\n[5] Got connection from {addr}")

        # send message to client (6)
        message = "Testing message sent from server to client."
        c.send(message.encode("utf-8"))
        print(f"[6] Message sent to client...")

        # receive message from client (7)
        inbound_message = c.recv(1024).decode("utf-8")
        print(f"[7] Message received from client:"
              f"\n\t- {inbound_message}")

        # close connection with client (8)
        c.close()
        print(f"[8] Connection with client is closed.")

    except KeyboardInterrupt:
        print(f"\n[] Server session terminated.")


if __name__ == '__main__':
    initiate_server()
