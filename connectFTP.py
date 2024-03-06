import socket

host = "ftp.ibiblio.org"
port = 21

def receive():
    data = s.recv(1024)
    print(data)
    if data=="":
        pass
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port) )
receive()
s.send(b"USER anonymous\r\n")
receive()
s.send(b"PASS ano@ano.fr\r\n")
receive()
s.send(b"HELP\r\n")
receive()
s.send(b"QUIT\r\n")
s.close()