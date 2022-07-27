from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
from shared import lock_uart, lock_memory,DEV,lock_client
import appsettings
from appsettings import useIp,usePort,useAddr,flagComm

from devicemainboard import BCmb
#from report import IndividualReport

logger = logging.getLogger(__name__)

class ACTION(Enum):
	PASS = 0
	FAIL = 1

class DataListenerMemory(Thread):

	#mySrc = None
	_stop_event = None

	def __init__(self, args):
	#def __init__(self):
		'''Constructor'''
		Thread.__init__(self)
		self._args = args
		self._name = "DataListenerMemory Thread"
		self.count = 0
		if args != None:
			self.mySrc = Communicate()
			self.mySrc.myGUI_signal.connect(args)

		self._stop_event = Event()
		self._stop_event.clear()

	def run(self):
		print(self._name+" started")
		#lock_client.acquire()
		while not self._stop_event.is_set():
			print("Entra!!")
			#if flagComm != True:
			self.pingForDevicesPresent()

			self.mySrc.myGUI_signal.emit("DL[PASS]:DataReady")
			sleep(1)

		#lock_client.release()

	def stop(self):
		print("stop was done in "+self._name)
		self._stop_event.set()

	def join(self, *args, **kwargs):
		self.stop()
		super(DataListenerMemory,self).join(*args, **kwargs)

	def pingForDevicesPresent(self):
		# we do ping to the devices 
		for i in range(len(useIp)):
			address = int(useAddr[i])
			print("Doing ping to device No."+str(address))
			readData = BCmb.pingClient(useIp[i],usePort)
			print("PING:",str(readData))

			#if readData!= None:
			print("readData:",readData)
			if readData!= None: 
				if readData == True:
					self.count = 0
					shared.DEV[address][0] = True
					print("DEV"+str(address)+" is Present!")
				else:
					#print("DEV"+str(address)+" is not Present!")
					print("ELSE")
			else:
				#shared.DEv[address][0] = False
				self.count = self.count + 1
				#if self.count > 8:
				shared.DEV[address][0] = False
				print("DEV"+str(address)+" is not Present!")

if __name__ == '__main__':
	logger.debug("demo")
	main = DataListenerMemory(None)
	# main.daemon = True
	main.start()
	# main.stop()
