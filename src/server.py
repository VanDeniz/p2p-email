import socket
import sys
from socket import gethostbyname

PORT = 5000
next = 1024

# internally insecure
host = gethostbyname('0.0.0.0')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, PORT))

print "Listening on", PORT

while True:
	(data, addr) = s.recvfrom(next)
	print data

sys.exit()
