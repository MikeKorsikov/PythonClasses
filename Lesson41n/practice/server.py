import socket
import json

# option 1
# s = socket.socket()
# HOST = 'localhost'  #or IP = '127.0.0.1'
# PORT = 7777
# s.bind((HOST, PORT))


# option 2 (using JSON)
s = socket.socket()
with open('config.json') as f:
    config = json.load(f)

IP = config['ip']
PORT = config['port']
s.bind((IP, PORT))

s.listen(1)
print('Server started...')

conn, adr = s.accept()
print(f"Connected: \nAddress: {adr}")

while True:
    data = conn.recv(1024).decode("utf-8")
    print(data)
    if not data:
        break
    conn.send(data.upper().encode("utf-8"))

conn.close()

# run server first and client second
