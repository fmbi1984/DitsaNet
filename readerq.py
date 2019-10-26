from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate

from shared import lock,devStart,devStop,DEV,DEV_PAGE
#import shared
import appsettings

from devicemainboard import BCmb
#from report import IndividualReport

logger = logging.getLogger(__name__)


class ReaderQ(Thread):
	def __init__(self,in_queue):
		Thread.__init__(self)
		self.in_queue = in_queue

	def run(self):
		while True:
			q_msg = self.in_queue.get()
			#if msg == 'quit':
			#	print('reader se va!')
			#	x = self.in_queue.empty()
			#	print(x)
			#	break

			print('leido '+q_msg)

if __name__ == '__main__':
	logger.debug("demo")
	main = ReaderQ(None)
	#main.daemon = True
	#main.start()
	#main.stop()