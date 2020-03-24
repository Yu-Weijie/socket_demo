# -*- coding: utf-8 -*-  
import socket


def server():
	#1.创建套接字
	s = socket.socket()
	#2.绑定
	Host = '127.0.0.1'
	Port =  8887
	s.bind((Host,Port))
	#3.监听
	s.listen(5)
	#4.处理
	while True:
		c,addr = s.accept()
		print("Connet client : ", addr)
		msg = c.recv(1024)
		print("From client : %s" %msg)
		c.send(msg)
	pass

if __name__ == '__main__':
	server()


	
	
	