import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 1234))

message, address = server.recvfrom(1024)
print(message.decode('utf-8'))
server.sendto("hello whoever".encode(utf-8), address)