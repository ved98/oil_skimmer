import socket

HOST = '10.7.9.9'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('1')
data = s.recv(1024)
print (data)
if data == '2':
    s.sendall('3')
s.close