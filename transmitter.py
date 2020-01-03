import math
#Die Klasse stellt die zu sendenden daten da
class DatenObject():
    def __init__(self, socket, daten=None, binary=True):
        self.socket=socket
        self.recived=None
        self.ammount_of_parts = None
        self.parts = []
        if daten is not None:
            print('Daten vorhanden')
            if binary:
                self.bytes = daten
            elif not binary:
                self.bytes = str(daten).encode('utf-8')

            self.length = len(self.bytes)


            self._get_parts_()
    def _get_parts_(self):
        self.ammount_of_parts=int(math.ceil(self.length/4096))
        for part in range(0,self.ammount_of_parts):
            self.parts.append(self.bytes[part:part+4096])


    def send_all(self):
        self.socket.send(str(self.ammount_of_parts).encode('utf-8'))
        print('Check 1')
        if self.ammount_of_parts is not None:
            for part in self.parts:
                self.socket.send(part)
        erfolg = bool(self.socket.recv(1024))
        #if not erfolg:
         #   self.send_all()

    def recv_all(self):
        self.recived=[]
        self.ammount_of_parts = int(self.socket.recv(4096).decode('utf-8'))
        #print('Check 1')

        for part in range(0, self.ammount_of_parts):
            self.recived.append(self.socket.recv(4096))
        self.bytes = b"".join(self.recived)

            #self.recv_all()
        print(len(self.bytes))
        print(self.bytes.decode('utf-8'))
        return self.bytes


