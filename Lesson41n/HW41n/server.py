import socket


def initiate_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = '127.0.0.1'
        PORT = 12345
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        c, addr = server_socket.accept()

        # PART 1
        outbound_message = "Player 1, what is your name?"
        c.send(outbound_message.encode("utf-8"))

        inbound_message = c.recv(1024).decode("utf-8")
        if inbound_message == 'quit':
            print('Quiting...')
            c.close()
        else:
            player1 = inbound_message
            print(f'Player1 is: {player1}')

        # PART 2

    except KeyboardInterrupt:
        print(f"\n[] Server session terminated.")


if __name__ == '__main__':
    initiate_server()
