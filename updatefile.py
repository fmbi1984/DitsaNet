from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
import appsettings

from devicemainboard import BCmb

import paramiko
from scp import SCPClient

logger = logging.getLogger(__name__)

#class ACTION(Enum):
 #   PASS = 0
 #   FAIL = 1

class UpdateFile(Thread):

    _src = None

    _stopEvent = None

    def __init__(self,comm):
        '''Constructor'''
        Thread.__init__(self)
        self._comm = comm
        self._name = "UpdateFile Thread"
        
        if comm != None:
            self._src = Communicate()
            self._src.myGUI_signal.connect(comm)

        self._stopEvent = Event()
        self._stopEvent.clear() 


    def run(self):

        print(self._name + " started")

        #while not self._stopEvent.is_set():
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname='raspberrypi.local', username='pi', password='raspberry')

            '''
            sftp = ssh_client.open_sftp()
            # This will remove a file
            sftp.remove("/home/pi/Documents/New.txt")
            # This will remove a folder
            sftp.rmdir("/home/pi/Documents/New")
            sftp.close()
            '''

            # SCPCLient takes a paramiko transport as an argument
            scp = SCPClient(ssh_client.get_transport())

            # This will copy a file
            #scp.get(remote_path='/home/pi/Documents/New.txt', local_path='')
            # This will copy a whole directory
            scp.get(remote_path='/home/pi/TestLogs/', local_path='', recursive=True)

            scp.close()
            ssh_client.close()
        except Exception as e:
            print("Error : " + str(e))

    #print ("Soy el hilo principal")

    def stop(self):
        print("stop was done in "+ self._name)
        self._stopEvent.set()


if __name__ == '__main__':
    logger.debug("demo")


