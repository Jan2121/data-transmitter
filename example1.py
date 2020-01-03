from transmitter import DatenObject
import socket
file=open('data.txt','rb')
d=file.read()
file.close()
host=socket.gethostname()
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
c, addr = sock.accept()
test = DatenObject(c,d)
test.send_all()