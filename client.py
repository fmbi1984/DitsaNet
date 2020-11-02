#!/usr/bin/env python3

import socket
from appsettings import useHostname, usePort

#HOST = ['raspberrypi.local','raspberrypi00.local']
#PORT = [10000,10050]


#HOST = 'raspberrypi00.local'  # The server's hostname or IP address #169.254.76.5
#PORT = 10050 #65433        # The port used by the server


for i in range(len(useHostname)):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((useHostname[i], usePort[i]))
		s.sendall('Hello, world'.encode())
		data = s.recv(19)

	print('Received', repr(data))




