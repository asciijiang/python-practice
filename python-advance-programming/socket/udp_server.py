import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ("127.0.0.1",8888)

sk.bind(ip_port)

while True:
	data,addr = sk.recvfrom(1024)
	print(data.decode("utf8"))
	data = data.decode("utf8")
	data = data.upper()
	
	sk.sendto(data.encode("utf8"),addr)