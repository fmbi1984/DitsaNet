
import time
import serial

ser = serial.Serial("/dev/tty.usbserial-A601CK2G", baudrate=115200)
print("Inicio")

class Prueba():
	def __init__(self):
		self.cbuff = [None]
		self.bytesLiteral = b''
		try:
			while True:
				read = ser.read()
				print("read_ini:",read)
				
				if read == b'\x04':
					cbuff.append(ord(read))
					print("read:",cbuff)
					break
				else:
					print("else")
					cbuff.append(ord(read))
					bytesLiteral = ''.join(str(bytes(cbuff),'ISO-8859-1'))
					print("msg:",bytesLiteral)
					#time.sleep(1)
		except:
			print("ERROR")
		finally:
			ser.close()

'''
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)
print("Inicio")

class Prueba():
	def __init__(self):
		self.cbuff = [None]
		self.bytesLiteral = b''
		try:
			while True:
				read = ser.read()
				print("read_ini:",read)
				
				if read == b'\x04':
					cbuff.append(ord(read))
					print("read:",cbuff)
					break
				else:
					print("else")
					cbuff.append(ord(read))
					bytesLiteral = ''.join(str(bytes(cbuff),'ISO-8859-1'))
					print("msg:",bytesLiteral)
					#time.sleep(1)
		except:
			print("ERROR")
		finally:
			ser.close()
'''
if __name__ == '__main__':
	print("FileReports")

	fl = Prueba()