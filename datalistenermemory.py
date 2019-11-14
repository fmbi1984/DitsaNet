from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
from shared import lock_uart, lock_memory,devStart,devStop,DEV,DEV_PAGE
import appsettings
from appsettings import useHostname

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
				#print("Doing asking data to device No. "+str(address))
				#BCmb.stopPollingClient(useHostname,address)
				#sleep(.002)
				BCmb.startPollingClient(useHostname)
				sleep(.4)
				BCmb.stopPollingClient(useHostname)
				sleep(.1)
				memoryData = BCmb.memoryDataClient(useHostname)
				sleep(.3)

				
				
				print("ValueM:")
				print(memoryData)
				memoryData = memoryData[0].split(',')
				print(memoryData)
				dat1 = str(memoryData[0]).replace('{','')
				print(dat1)
				
				dat2 = str(memoryData[7]).replace('}','')
				print(dat2)

				#print("VaL")
				#print(dat2)

				'''
				shared.DEV[address][1] = dat2[0].replace('I','')
				print(shared.DEV[address][1])

				shared.DEV[address][1] = str(memoryData[0]).replace('I','')
				print(shared.DEV[address][1])
				'''

				#lock_memory.acquire()
				if memoryData!= None:
					#we store current
					shared.DEV[address][1] = str(dat1.replace('I',''))
					#we store voltage
					shared.DEV[address][2] = str(memoryData[1].replace('V',''))
					#we store temperature
					shared.DEV[address][3] = str(memoryData[2].replace('T',''))
					#we store step number and type
					shared.DEV[address][4] = str(memoryData[3].replace('P',''))
					#we store time of current step
					shared.DEV[address][5] = str(memoryData[4].replace('t',''))
					#we store current time program
					shared.DEV[address][6] = str(memoryData[5].replace('Tt',''))
					#we store the total time program
					shared.DEV[address][7] = str(memoryData[6].replace('TT',''))
					#we store the total time program
					shared.DEV[address][8] = str(dat2.replace('',''))

					if shared.DEV[address][8] == '':
						print("Dato3")

				if memoryData != None:
					if self.mySrc != None:
						self.mySrc.myGUI_signal.emit("DL["+str(address)+"]:DataReady")

				#BCmb.startPollingClient(useHostname,address)

				#lock_memory.release()
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
