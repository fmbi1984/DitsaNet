#!/usr/bin/env python3

import socket

HOST = 'ditsa-Lenovo-C20-00.local'  # The server's hostname or IP address
PORT = 65433        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('Hello, world'.encode())
    data = s.recv(1024)

print('Received', repr(data))
