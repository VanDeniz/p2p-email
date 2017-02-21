import sys
import socket

host = "127.0.0.1"  # target address
port = 5000
size = 1024

addr = (host, port)
s = socket(AF_INET, SOCK_DGRAM)

while True:
	data = "cool"
	s.sendto(data, addr)

s.close()
sys.exit()
