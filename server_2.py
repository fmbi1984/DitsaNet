#!/usr/bin/env python3

import socket

port = 9000
mssg = 'Recibi un Hola...' #b"HolaMund0\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',port))
s.listen(1)

while True:
	# Wait for a connection
	print('Espera una conexion')
	connection, client_address = s.accept()
	try:
		print('connection from', client_address)

		# Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(1024)
			print('received {!r}'.format(data))
			if data:
				print('sending data back to the client')
				connection.sendall(mssg.encode())
				break
			else:
				print('no data from', client_address)
				break

	finally:
		# Clean up the connection
		print("Cierra socket")
		connection.close()



