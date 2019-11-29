from time import sleep, time

from threading import Thread, Event

import logging
from enum import Enum
from communicate import Communicate

from shared import lock_uart, lock_memory,devStart,devStop,DEV,DEV_PAGE
#import shared
import appsettings

from devicemainboard import BCmb
from report import IndividualReport

logger = logging.getLogger(__name__)


ireport = IndividualReport()

class ACTION(Enum):
    PASS = 0
    FAIL = 1

class DataListenerServer(Thread):


    mySrc = None

    _stop_event = None
    _pause_event = None
    

    def __init__(self, args):
        '''Constructor'''
        Thread.__init__(self)
        self._args = args
        self._name = "DataListenerServer Thread"
        if args != None:
            self.mySrc = Communicate()
            self.mySrc.myGUI_signal.connect(args)
        
        self._stop_event = Event()
        self._stop_event.clear()
        
        self._pause_event = Event()
        self._pause_event.clear()
        
        
    def run(self):

        #try:
        print(self._name+" started")
        
        self.pingForDevicesPresent()
        
        while not self._stop_event.is_set():
            
            # we do ping to the devices 
            lock_memory.acquire()
            for i in range(devStart, devStop+1):
                address = i

                if DEV[address][0] == True:
                    print("Doing asking data to device No."+str(address))
                   
                    readData = BCmb.readData(address)
                    print("ValueDLS:")
                    print(readData)
                    
                    
                    if readData!= None:                        
                        #we store current
                        DEV[address][1] = str(readData[0].replace('I',''))
                        #we store voltage
                        DEV[address][2] = str(readData[1].replace('V',''))
                        #we store temperature
                        DEV[address][3] = str(readData[2].replace('T',''))
                        #we store step number and type
                        DEV[address][4] = str(readData[3].replace('P',''))
                        #we store time of current step
                        DEV[address][5] = str(readData[4].replace('t',''))
                        #we store current time program
                        DEV[address][6] = str(readData[5].replace('Tt',''))
                        #we store the total time program
                        DEV[address][7] = str(readData[6].replace('TT',''))
                        #we store the total time program
                        DEV[address][8] = str(readData[7].replace('',''))
                        '''
                        print("Current Value:")
                        print(DEV[address][1])
                        print(DEV[address][2])
                        print(DEV[address][3])
                        print(DEV[address][4])
                        print(DEV[address][5])
                        print(DEV[address][6])
                        print(DEV[address][7])
                        print(DEV[address][8]) 
                        '''
                        if (DEV[address][8] == 'S' or DEV[address][8] == 'E') and DEV[address][9] == True:
                            print(DEV[address][9])
                            DEV[address][9] = False
                            ireport.appendWithTimeStampUsingFile(","+ DEV[address][1] + "," + DEV[address][2] + "," +\
                                                    DEV[address][3] + "," + DEV[address][4] + "," +\
                                                    DEV[address][5] + "," + DEV[address][6] + "," +\
                                                    DEV[address][7] + "," + DEV[address][8], str(address))

                        if DEV[address][8] == 'R' or DEV[address][8] == 'P':
                            DEV[address][9] = True
                            ireport.appendWithTimeStampUsingFile(","+ DEV[address][1] + "," + DEV[address][2] + "," +\
                                                    DEV[address][3] + "," + DEV[address][4] + "," +\
                                                    DEV[address][5] + "," + DEV[address][6] + "," +\
                                                    DEV[address][7] + "," + DEV[address][8], str(address))
                        
                    
                        #self.dataStr = str(readData[0])
                
                    #['VALUE', 'I0.27,V-0.98,T27.21']

                    
                
            sleep(.3)
            self.stop()
            lock_memory.release()
            #while not self._stop_event.is_set():
            #    print("stop_event")
            #    sleep(.2)
            #print(self._name+" stopped")
        '''
        except:
            print("ERROR SERVER WHEN ASKING DATA")
            self.stop()
 
        '''
        
    def pause(self):
        print("pause was done in "+self._name)
        self._pause_event.set()
    def resume(self):
        print("resume was done in "+self._name)
        self._pause_event.clear()
    def stop(self):
        print("stop was done in "+self._name)
        self._stop_event.set()

    def join(self, *args, **kwargs):
        #self.stop()
        super(DataListenerServer,self).join(*args, **kwargs)

    def pingForDevicesPresent(self):
        # we do ping to the devices 
        for i in range( devStart, devStop+1):
            address=i

            if DEV[i][0] == False:
                print("Doing ping to device No."+str(address))
                readData = BCmb.ping(address)
                print("VALUE:")
                print(str(readData))
                DEV[i][0] = False
                if readData!= None:
                    if readData == True:
                        DEV[i][0] = True
                        print("DEV"+str(address)+" is Present!")  
                    else:
                        print("DEV"+str(address)+" is not Present!")
                        #ireport.end()
                else:
                    print("DEV"+str(address)+" is not Present!")
                    #ireport.end()
        
        

if __name__ == '__main__':
    logger.debug("demo")
    #main.daemon = True
    main = DataListenerServer(None)
    main.start()
    main.stop()