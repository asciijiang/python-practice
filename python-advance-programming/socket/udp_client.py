import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ("127.0.0.1",8888)

while True:
	msg = input("请输入发送的消息：")
	if msg == "exit":
		break
	sk.sendto(msg.encode("utf8"),ip_port)
	tmpdata = sk.recv(1024)
	print(tmpdata.decode("utf8"))

sk.close()	