from transmitter import DatenObject
import socket
host=socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
test=DatenObject(s)
b=test.recv_all()
file=open('test.txt','wb')
file.write(b)
file.close()