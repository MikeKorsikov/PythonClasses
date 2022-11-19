import socket


def initiate_client():
    try:
        # create socket object (1)
        client_socket = socket.socket()
        print(f"\n[1] Client socket successfully created!")

        # supply connection details (2)
        HOST = '127.0.0.1'
        PORT = 12345
        print(f'[2] Connection details supplied.')

        # connect to server (3)
        client_socket.connect((HOST, PORT))
        print(f"[3] Connected to server!")

        # receive message from server (4)
        inbound_message = client_socket.recv(1024).decode("utf-8")
        print(f"\n[4] Following message received from server:"
              f"\n\t- {inbound_message}")

        # send message to server (4/5)
        outbound_message = "Testing message sent to server."
        client_socket.send(outbound_message.encode("utf-8"))
        print(f"[5] Message sent to server.")

        # close connection with server (6)
        client_socket.close()
        print(f"[6] Connection to server is closed.")

    except KeyboardInterrupt:
        print(f"\n[] Client session terminated.")


if __name__ == '__main__':
    initiate_client()
