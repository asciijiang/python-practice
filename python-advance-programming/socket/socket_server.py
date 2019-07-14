import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()
sock,addr = server.accept()

#获取从客户端发送的数据
#一次获取1k的数据
while True:
	data = sock.recv(1024)
	print(data.decode("utf8"))
	re_data = input()
	sock.send(re_data.encode("utf8"))
#特定socket关闭
sock.close()
#server监听socket关闭
server.close()