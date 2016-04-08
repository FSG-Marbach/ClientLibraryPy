import socket

class SasClient:
    def __init__(self, serverIP, serverPort):
        self.serverIP = serverIP
        self.serverPort = serverPort
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.serverIP, self.serverPort))
    
    def send(self, txt):
        self.sock.send(txt)

    def recv(self):
        return self.sock.recv(2048)

    def close(self):
        self.sock.shutdown()
        self.sock.close()


