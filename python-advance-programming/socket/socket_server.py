import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()

def handle_sock(sock,addr):
	while True:
		data = sock.recv(1024)
		print(data.decode("utf8"))
		if data.decode("utf8") == "exit":
			break
		re_data = input()
		sock.send(re_data.encode("utf8"))
	sock.close()	

#获取从客户端发送的数据
#一次获取1k的数据
while True:
	sock,addr = server.accept()
	
	client_thread = threading.Thread(target=handle_sock,args=(sock,addr))
	client_thread.start()
	
# #特定socket关闭
# sock.close()
# #server监听socket关闭
# server.close()