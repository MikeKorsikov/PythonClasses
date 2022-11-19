import socket


def initiate_client():
    try:

        client_socket = socket.socket()
        HOST = '127.0.0.1'
        PORT = 12345
        client_socket.connect((HOST, PORT))

        inbound_message = client_socket.recv(1024).decode("utf-8")
        print(inbound_message)

        outbound_message = input('>>>')
        client_socket.send(outbound_message.encode("utf-8"))

        if outbound_message == 'quit':
            client_socket.close()
        else:
            pass

    except KeyboardInterrupt:
        print(f"\n[] Client session terminated.")


if __name__ == '__main__':
    initiate_client()
