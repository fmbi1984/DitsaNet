from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
import appsettings

from devicemainboard import BCmb
#from report import IndividualReport

logger = logging.getLogger(__name__)


class ACTION(Enum):
	PASS = 0
	FAIL = 1


class DataListenerMemory(Thread):

	mySrc = None
	_stop_event = None

	def __init__(self, args):
		'''Constructor'''
		Thread.__init__(self)
		self._args = args
		self._name = "DataListenerMemory Thread"
		if args != None:
			self.mySrc = Communicate()
			self.mySrc.myGUI_signal.connect(args)

		self._stop_event = Event()
		self._stop_event.clear()

	def run(self):
		# try:
		print(self._name+" started")
		#self.pingForDevicesPresent()
		while not self._stop_event.is_set():

			for i in range(shared.devStart, shared.devStop+1):
				address = i
				
				#print(shared.DEV[address][0])
				#if shared.DEV[address][0] == True:
				print("Doing asking data to device No. "+str(address))
				memoryData = BCmb.memoryDataClient('raspberrypi.local', 1)
				#memoryData = BCmb.startPollingClient('raspberrypi.local',address)
				
				#print("MD")
				#print(memoryData)
				
				'''
				memoryDataTemp = str(memoryData[0].replace('D',''))

				if memoryDataTemp == 'True':
					shared.DEV[address][0] = True
				else:
					shared.DEV[address][0] = False

				if shared.DEV[address][0] == True:
				
				'''
				print("ValueM:")
				print(memoryData)

				if memoryData!= None:
					#we store current
					shared.DEV[address][1] = str(memoryData[0]).replace('I','')
					#we store voltage
					shared.DEV[address][2] = str(memoryData[1]).replace('V','')
					#we store temperature
					shared.DEV[address][3] = str(memoryData[2]).replace('T','')
					#we store step number and type
					shared.DEV[address][4] = str(memoryData[3]).replace('P','')
					#we store time of current step
					shared.DEV[address][5] = str(memoryData[4].replace('t',''))
					#we store current time program
					shared.DEV[address][6] = str(memoryData[5].replace('Tt',''))
					#we store the total time program
					shared.DEV[address][7] = str(memoryData[6].replace('TT',''))
					#we store the total time program
					shared.DEV[address][8] = str(memoryData[7].replace('',''))

					if shared.DEV[address][8] == '':
						print("Dato3")

				if memoryData != None:
					if self.mySrc != None:
						self.mySrc.myGUI_signal.emit("DL["+str(address)+"]:DataReady")

			# we do ping to the devices
			sleep(.1)
			print(self._name+" stopped")
		

	def stop(self):
		print("stop was done in "+self._name)
		self._stop_event.set()

	def join(self, *args, **kwargs):
		self.stop()
		super(DataListenerMemory,self).join(*args, **kwargs)

	def pingForDevicesPresent(self):
		# we do ping to the devices 
		for i in range(shared.devStart, shared.devStop+1):
			address=i
			print("Doing ping to device No."+str(address))
			readData = BCmb.ping(address)
			print("VALUE:")
			print(str(readData))
			shared.DEV[i][0] = False
			if readData!= None:
				if readData == True:
					shared.DEV[i][0] = True
					print("DEV"+str(address)+" is Present!")  
				else:
					print("DEV"+str(address)+" is not Present!")
					# ireport.end()
			else:
				print("DEV"+str(address)+" is not Present!")
				# ireport.end()

if __name__ == '__main__':
	logger.debug("demo")
	main = DataListenerMemory(None)
	# main.daemon = True
	main.start()
	# main.stop()
