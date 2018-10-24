import socket
from Crypto.Cipher import AES

class ipsec_socket(socket.socket):
    def __init__(self,*para):
        self.key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'
        self.cipher = AES.new(self.key,AES.MODE_ECB)
        super().__init__(*para)
    def send(self,data):
        data = self.cipher.encrypt(data)
        super().send(data)
        return
    def recv(self,length):
        super().recv(data)
        data = self.cipher.decrypt(data)
        return data

