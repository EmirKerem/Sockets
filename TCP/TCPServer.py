import socket
import datetime
from random import randint
from random import choice

def returning(msg):
    msg = (str(msg)).lower()
    l1 = ["heads","tails"]
    if "time" in msg:
        return datetime.datetime.now().strftime(" It's %H:%M:%S")
    elif "random" in msg and "number" in msg:
        return str(choice(range(1, 11)))
    elif "heads" in msg or "tails" in msg:
        ans = randint(0,1)
        return l1[ans]
    else:
        ans = "Please use basic words"
        return ans


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2424))

server.listen(4)
print("Server is listening now")

while True:
    client, addr = server.accept()
    print("Connection to ", addr)

    msg = client.recv(1024).decode()
    ans = returning(msg)
    client.send(ans.encode())


    client.close()

