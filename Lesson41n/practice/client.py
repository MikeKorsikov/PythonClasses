import socket
import json


# instruction 1
s = socket.socket()
with open('config.json') as f:
    config = json.load(f)

IP = config['ip']
PORT = config['port']
s.connect((IP, PORT))

s.send("Hello world".encode("utf-8"))
data = s.recv(1024)

s.close()
print(data.decode("utf-8"))

# run server first and client second


# instruction/example 2
s = socket.socket()
with open('config.json') as f:
    config = json.load(f)

IP = config['ip']
PORT = config['port']

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

collection = {"n1": n1, "n2": n2}
data2 = json.dumps(collection)

try:
    s.connect((IP, PORT))
    s.sendall(data2.encode("utf-8"))

    received = s.recv(1024).decode("utf-8")
except:
    print("Error")

finally:
    s.close()

print(data2)