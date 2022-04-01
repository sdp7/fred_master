import socket

host = "192.168.105.84"
port = 34000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',port))

s.listen(1)

c, addr = s.accept()

print("CONNECTION FROM:", str(addr))

c.send(b"Test")

msg = "Test2"

c.send(msg.encode())
c.close()
c.shutdown()