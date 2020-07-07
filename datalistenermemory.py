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

		#memoryPolling = BCmb.startPollingClient(useHostname)
		#sleep(.3)
		

	def run(self):
		print(self._name+" started")
		while not self._stop_event.is_set():
			memoryPolling = BCmb.startPollingClient(useHostname)
			sleep(.3)
			'''
			memoryData = BCmb.memoryDataClient(useHostname)
		
			for i in range (devStart,devStop+1): #checar con otros ping
				address = i
			
				if memoryData!= None:
					#print("ValueM:",memoryData)
					TempData = memoryData[address-1].split(',')
					#print("TempData:",TempData)
					dat1 = str(TempData[0]).replace('{','')
					#print("data1:",dat1)
					if dat1 == 'True':
						TempData[8] = str(TempData[8]).replace('}','')
						TempData[0] = True

						DEV[address][0] = TempData[0]
						#we store current
						DEV[address][1] = str(TempData[1].replace('I',''))
						#we store voltage
						DEV[address][2] = str(TempData[2].replace('V',''))
						#we store temperature
						DEV[address][3] = str(TempData[3].replace('T',''))
						#we store step number and type
						DEV[address][4] = str(TempData[4].replace('P',''))
						#we store time of current step
						DEV[address][5] = str(TempData[5].replace('t',''))
						#we store current time program
						DEV[address][6] = str(TempData[6].replace('Tt',''))
						#we store the total time program
						DEV[address][7] = str(TempData[7].replace('TT',''))
						#we store the total time program
						DEV[address][8] = str(TempData[8].replace('',''))

						#if shared.DEV[address][8] == '':
						#	print("Dato3")
						#print("shared8:",shared.DEV[address][8])

					if dat1 == 'False}':
						TempData[0] = str(TempData[0]).replace('}','')
						DEV[address][0] = False
						print("FalsePing")
					
					print("TempData2:",TempData)
			'''
			# we do ping to the devices
			#sleep(.1)
			#print(self._name+" stopped")

			if memoryPolling != None:
				if self.mySrc != None:
					#self.mySrc.myGUI_signal.emit("DL["+str(address)+"]:DataReady")
					self.mySrc.myGUI_signal.emit("DL[PASS]:DataReady")
		

	def stop(self):
		print("stop was done in "+self._name)
		self._stop_event.set()

	def join(self, *args, **kwargs):
		self.stop()
		super(DataListenerMemory,self).join(*args, **kwargs)

if __name__ == '__main__':
	logger.debug("demo")
	main = DataListenerMemory(None)
	# main.daemon = True
	main.start()
	# main.stop()
