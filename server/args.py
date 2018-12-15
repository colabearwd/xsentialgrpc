import socket
s=socket.socket()
s.connect(('127.0.0.1', 8000))
msg = raw_input("Please input your message:")
s.sendall(msg)
print s.recv(1024)
s.close()

