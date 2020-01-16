import logging
from time import sleep, time

import StringUtils

import os
import sys
import subprocess
import shared
import math
from enum import Enum

import shared
from shared import DEV
import appsettings
from appsettings import useHostname

from devinterface import devInterface

from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QScrollBar
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QDesktopServices
from PyQt5.QtCore import QEventLoop, QByteArray, Qt, QUrl, pyqtSignal, pyqtSlot, QObject, QTimer

logger = logging.getLogger(__name__)

class ACTION(Enum):
	PASS = 0
	FAIL = 1

class BCmb(object):
	timeout = 1
	attempts = 1
	
	@staticmethod
	def writeProgramClient(hostname,addr,program_in_json):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x57,program_in_json, 10)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result  
	
	'''
	@staticmethod
	def writeProgramClient(hostname,addr, program_in_json):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x57, program_in_json, 10)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result  
	'''

	@staticmethod
	def runClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x33, "", BCmb.timeout)
		print("RUN")
		print(result)
		if result != None:
			if result[1] == 'PASS,RUN':
				result = ACTION.PASS
				print(result)
			else:
				result = ACTION.FAIL
		return result

	@staticmethod
	def pauseClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x34, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS,PAUSE':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result
	
	@staticmethod
	def stopClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x35, "", BCmb.timeout)
		print("STP")
		print(result)
		if result != None:
			if result[1] == 'PASS,STOP':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	@staticmethod
	def readProgramClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x52, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1]
			else:
				result = None
		return result
	'''
	@staticmethod
	def readVoltageClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x56, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	@staticmethod
	def readTemperatureClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x54, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	@staticmethod
	def readCurrentClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x49, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result
	'''
	@staticmethod
	def readData(addr):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(addr, 0x43, "", 0.25)
		print("readData:")
		print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1].split(',')
			else:
				result = None
		else:
			DEV[addr][0] = False
		return result
	'''

	@staticmethod
	def readStepClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x50, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1]
			else:
				result = None
		return result
	
	@staticmethod
	def readTypeClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x50, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result
	'''

	@staticmethod
	def currentTimeClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x74, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1]
			else:
				result = None
		return result
	'''
	@staticmethod
	def setAddress(address):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(None, 0xFF, str(chr(address)), BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	@staticmethod
	def getAddress():
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(None, 0xFF, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	'''
	@staticmethod
	def writeProgramFake(addr, program_in_json):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponseFake(addr, 0x57, program_in_json, BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result
	

	@staticmethod
	def readDataClient(hostname, addr):
		result = ACTION.FAIL
		res = devInterface.sendClientCommandAndGetResponse(hostname,addr, 0x43, "", BCmb.timeout)
		print(res)
		result=None
		if res != None:
			if res[0] == 'VALUE':
				result = res[1].split(',')
			else:
				result = None
		return result

	@staticmethod
	def pingClient(hostname,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,addr,0x64, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = True
			else:
				result = False
		return result
	
	
	@staticmethod
	def ping(addr):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(addr,0x64, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = True
			else:
				result = False
		return result  

	@staticmethod
	def startPollingClient(hostname):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(hostname,0x36, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = result[1]
			else:
				result = None
		return result

	@staticmethod
	def stopPollingClient(hostname):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(hostname,0x37, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1]
			else:
				result = None
		return result

	@staticmethod
	def memoryDataClient(hostname):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(hostname,0x38, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1].split(';')
			else:
				result = None
		return result


if __name__ == "__main__":
	print("tests")
	#BCmb.readData(1)
	#BCmb.pingClient(useHostname,1)
	#BCmb.ping(1)
	#BCmb.writeProgram(0, "[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"10000\"},{\"Type\":\"Charge\",\"Time\":\"120000\",\"Current\":\"8.0\"},{\"Type\":\"Charge\",\"Time\":\"50000\",\"Current\":\"12.0\"},{\"Type\":\"Carga\",\"Time\":\"60000\",\"Current\":\"15.0\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"20.0\"},{\"Type\":\"Pause\",\"Time\":\"20000\"},{\"Type\":\"Charge\",\"Time\":\"30000\",\"Current\":\"10.5\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"14.5\"},{\"Type\":\"End\"}]")
	#BCmb.readProgram(0)
	#BCmb.setAddress(1)
	#BCmb.run(1)
	#BCmb.stop(1)
	#BCmb.readStep(0)
	#BCmb.currentTime(0)
	#BCmb.readProgram(0)
	#BCmb.readDataClient(useHostname, 1)
	#BCmb.getAddress()
	
	#BCmb.stop(1)
	
	'''
	BCmb.getAddress()
	BCmb.readProgram(2)
	BCmb.run(2)
	'''
	
	
	
	#sleep(0.1)
	'''
	BCmb.startPollingClient(useHostname)
	sleep(.1)
	BCmb.stopPollingClient(useHostname)
	sleep(.3)
	BCmb.memoryDataClient(useHostname)
	'''
	
	#BCmb.runClient(useHostname, 2)

	#for i in range(0,100):
	#	BCmb.startPollingClient(useHostname)
	#	sleep(.2)
	#	BCmb.memoryDataClient(useHostname)
	#	BCmb.pingClient(useHostname,1)
		#BCmb.readDataClient(useHostname, 2)

	#BCmb.pingClient(useHostname,1)
	#BCmb.runClient(useHostname, 1)
	#BCmb.pauseClient(useHostname, 2)
	BCmb.stopClient(useHostname, 1)
	#BCmb.stopClient(useHostname, 1)
	#BCmb.readDataClient(useHostname,1)
	#BCmb.readStepClient(useHostname, 1)
	#BCmb.currentTimeClient(useHostname, 1)
	#BCmb.readProgramClient(useHostname,1)
	#BCmb.writeProgramClient(useHostname,2,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"10\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"22.7\"},{\"Type\":\"Charge\",\"Time\":\"600\",\"Current\":\"30.0\"},{\"Type\":\"Pause\",\"Time\":\"16\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"24.0\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient(useHostname,1,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"10\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"20.0\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"22.7\"},{\"Type\":\"Carga\",\"Time\":\"1200\",\"Current\":\"27.0\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"24.0\"},{\"Type\":\"Pause\",\"Time\":\"60\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"26.5\"},{\"Type\":\"Charge\",\"Time\":\"600\",\"Current\":\"30.0\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient(useHostname,1,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"25\"},{\"Type\":\"Charge\",\"Time\":\"30\",\"Current\":\"30.0\"},{\"Type\":\"Charge\",\"Time\":\"1800\",\"Current\":\"27.4\"},{\"Type\":\"Carga\",\"Time\":\"1200\",\"Current\":\"18.6\"},{\"Type\":\"Pause\",\"Time\":\"180\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"9.0\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"12.4\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"22.2\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"8.8\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"25.6\"},{\"Type\":\"Pause\",\"Time\":\"180\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"17.2\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient(useHostname,1,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"15\"},{\"Type\":\"Charge\",\"Time\":\"60\",\"Current\":\"28.3\"},{\"Type\":\"Pause\",\"Time\":\"46\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"20.8\"},{\"Type\":\"Carga\",\"Time\":\"40\",\"Current\":\"30.0\"},{\"Type\":\"Pause\",\"Time\":\"15\"},{\"Type\":\"Charge\",\"Time\":\"60\",\"Current\":\"25.7\"},{\"Type\":\"Pause\",\"Time\":\"20\"},{\"Type\":\"Charge\",\"Time\":\"120\",\"Current\":\"26.4\"},{\"Type\":\"Charge\",\"Time\":\"30\",\"Current\":\"18.9\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient(useHostname,1,"[{\"Type\":\"Begin\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"30.0\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"25.6\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Carga\",\"Time\":\"600\",\"Current\":\"10.5\"},{\"Type\":\"Carga\",\"Time\":\"1200\",\"Current\":\"19.2\"},{\"Type\":\"Carga\",\"Time\":\"600\",\"Current\":\"28.4\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"23.5\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"14.7\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Pause\",\"Time\":\"120\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"17.7\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"9.5\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"24.8\"},{\"Type\":\"End\"}]")
	
	'''
	while True:
		#BCmb.readData(1)
		BCmb.memoryDataClient(useHostname, 1)
		#BCmb.readDataClient(useHostname, 1)
		#BCmb.readDataClient(useHostname, 2)
		#BCmb.readStepClient(useHostname, 2)
		sleep(.1)
	#'''
