import socket
import sys
from _thread import start_new_thread
import threading

import USBUtils
import SerialPortUtil
import StringUtils
from serialcommthread import SerialCommThread, serial_cmd_result

from time import sleep, time

import serial
import appsettings
from datalistenerserver import DataListenerServer
from devinterface import  devInterface
from testLcd import LCD

import shared
from shared import lock_uart, lock_memory

#sleep(10)
HOST = 'raspberrypi.local' #'raspberrypi.local' # all availabe interfaces
PORT = 65433 # arbitrary non privileged port

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
except socket.error as msg:
	print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
	sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
	s.bind((HOST, PORT))
	print("[-] Socket Bound to port " + str(PORT))
except socket.error as msg:
	print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
	sys.exit()

s.listen(10)
print("Listening...")

ds = DataListenerServer(None)

# The code below is what you're looking for ############

lcd = LCD()
lcd.clear()
#lcd.write_line1('Listenig...',1)
#lcd.lcd_string('Local IP Address:',2)
lcd.lcd_string('Listening...',1)

#lock = threading.Lock()
#count = 0

def client_thread(conn):
	
	while True:
		p_data = conn.recv(1024)
		if not p_data:
			break
		
		result = None
		data = None
		
		try:
			#cmd_data = bytes(cmd,'ISO-8859-1')
			#p_data = devInterface.packMessage(address, op, cmd_data)
			if appsettings.useDongle == True:
				print("Test Mac Server")
				sp = SerialPortUtil.getFirstPortByVID_PID(0x1a86,0x7523)
				
			else:
				print("Test Raspbian")
				sp = SerialPortUtil.getPortByName("/dev/ttyS0")
				print(sp)

			#sp = SerialPortUtil.getPortBySerialNumber(appsettings.FTDI_serialNumber)
			#sp = SerialPortUtil.getFirstPortByVID_PID(0x067b,0x2303)
			#sp = SerialPortUtil.getFirstPortByVID_PID(0x10c4,0xea60)
			if sp == None:
				raise Exception("devInterface", "No serial device found!")
			#print(p_data[2])
			print(p_data)
			op_code = 0x57
			st_polling = 0x36
			cl_polling = 0x37
			op_data = 0x38
			t_out = 10
			
			
			if p_data[2] == st_polling:
				print("start polling")
				msg = devInterface.unpackMessage(p_data)
				ds.start()
				tmp = bytes("ACTION: PASS", 'ISO-8859-1')
				
				data = bytes(devInterface.packMessage(msg[1], msg[2], tmp))
				print("DATA1:")
				print(data)

			elif p_data[2]== cl_polling:
				print("stop polling")
				msg = devInterface.unpackMessage(p_data)
				tmp = bytes("ACTION: PASS", 'ISO-8859-1')
				ds.stop()
				data = bytes(devInterface.packMessage(msg[1], msg[2], tmp))
				print("DATA2:")
				print(data)
				
			elif p_data[2] == op_data:
				print("memory data")
				msg = devInterface.unpackMessage(p_data)
				#tmp = bytes("ACTION: PASS", 'ISO-8859-1')
				
				address = int(msg[1])
				
				lock_memory.acquire()
				
				tmp = "VALUE: " + "I" + shared.DEV[address][1] + "," +\
								  "V" + shared.DEV[address][2] + "," +\
								  "T" + shared.DEV[address][3] + "," +\
								  "P" + shared.DEV[address][4] + "," +\
								  "t" + shared.DEV[address][5] + "," +\
								  "Tt" + shared.DEV[address][6] + "," +\
								  "TT" + shared.DEV[address][7] + "," +\
								  "" + shared.DEV[address][8]
				
				lock_memory.release()
				print("Address: "+str(address))

				print("TMP")

				print(tmp)
				data = bytes(devInterface.packMessage(msg[1], msg[2], bytes(tmp,'ISO-8859-1')))
				print("DATA3:")
				print(data)
				
			else:
				
				if p_data[2] == op_code:			   #write eeprom json
					t_out = 10
				else:
					t_out = 1
				
				try:	
					sct = SerialCommThread(None, sp, appsettings.FTDI_baudRate, p_data, b'\x04',t_out,5)
					sct.start()
					sct.join()
					
					data = bytes(serial_cmd_result[0])
					print(data)
					
				except:
					print("Error: Serial Communication")
				
				
			#print("serial thread stopped")
			#if sct.stopped() == False:
			#   e="serial thread not stopped"
			#   print("\033[1;31;40m"+str(e)+"\033[0;37;40m")

			'''
			result = None
			if data != None:
				result = devInterface.decodeMessage(data)
			else:
				result = None
			'''
		except Exception as e:
			print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
		#return result

		#reply = b'OK . . '
		#reply = serial_cmd_result[0]
		#print('Received', repr(data))
		if data != None:
			conn.sendall(data)
		else:
			conn.sendall(b'None')
	print("[-] Closed connection")
	conn.close()

while True:
	# blocking call, waits to accept a connection
	conn, addr = s.accept()
	print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
	ip_address = ''
	ip_address = s.getsockname()[0]
	
	lcd.write_line2(ip_address,1)
	#print(ip_address)

	start_new_thread(client_thread, (conn,))

s.close()
