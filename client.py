# -*- coding: utf-8 -*-

import socket

def client():
	#1.创建套接字
	s = socket.socket()
	#2.链接
	Host = '127.0.0.1'
	Port =  8887
	s.connect((Host,Port))
	#3.处理
	s.send(b'Hello World !')
	msg = s.recv(1024)
	print("From server : %s" %msg)

if __name__ == '__main__':
	client()