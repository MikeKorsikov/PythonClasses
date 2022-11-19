# Network Programming
# https://www.geeksforgeeks.org/python-network-programming/
# IP - internet protocol, governing the format of data sent via the internet


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)


# Example
s = socket.socket()
print("Socket successfully created")

port = 40674

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(b'Thank you for connecting')
    c.close()
