# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_copy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#from form import Ui_Form
from paint import Paint
from windowch import Ui_WindowCh
from pausemodule import Ui_pauseModule
from stopmodule import Ui_stopModule
from runmodule import Ui_runModule

from devicemainboard import BCmb
import shared
import time
import threading

from appsettings import useHostname
from ordened import NameOrdened

from datalistenermemory import DataListenerMemory

class Ui_MainWindow(object):
	def __init__(self,MainWindow, parent=None):
	#def setupUi(self, MainWindow):
		object.__init__(parent)

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1280, 523) #1280,700  1476 523
		#MainWindow.setFixedSize(1280,523)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
		self.gridLayout.setContentsMargins(11, 11, 11, 11)
		self.gridLayout.setSpacing(6)
		self.gridLayout.setObjectName("gridLayout")
		self.cmdIniciar = QtWidgets.QPushButton(self.centralWidget) ######
		self.cmdIniciar.setObjectName("cmdIniciar")
		self.gridLayout.addWidget(self.cmdIniciar, 0, 1, 1, 1)

		self.comboBox = QtWidgets.QComboBox(self.centralWidget)
		self.comboBox.setObjectName("comboBox")
		self.gridLayout.addWidget(self.comboBox, 0, 4, 1, 1)  #0,3,1,1
		self.cmdCargar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdCargar.setObjectName("cmdCargar")
		self.gridLayout.addWidget(self.cmdCargar, 0, 0, 1, 1) 

		self.cmbZoom = QtWidgets.QComboBox(self.centralWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.cmbZoom.sizePolicy().hasHeightForWidth())
		self.cmbZoom.setSizePolicy(sizePolicy)
		self.cmbZoom.setObjectName("cmbZoom")
		self.gridLayout.addWidget(self.cmbZoom, 0, 5, 1, 1) #0,4,1,1
		self.cmdDetener = QtWidgets.QPushButton(self.centralWidget)
		self.cmdDetener.setObjectName("cmdDetener")
		self.gridLayout.addWidget(self.cmdDetener, 0, 3, 1, 1) #0,2,1,1
		self.cmdPausar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdPausar.setObjectName("cmdPausar")
		self.gridLayout.addWidget(self.cmdPausar, 0, 2, 1, 1) #0,1,1,1 
		self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
		font = QtGui.QFont()
		#font.setFamily("Ubuntu")
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		self.tabWidget.setFont(font)
		self.tabWidget.setStyleSheet("")
		self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
		self.tabWidget.setObjectName("tabWidget")
	#	self.tab = QtWidgets.QWidget()
	#	self.tab.setObjectName("tab")
	#	self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
	#	self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
	#	self.gridLayout_2.setSpacing(6)
	#	self.gridLayout_2.setObjectName("gridLayout_2")
		#self.tabWidget.addTab(self.tab, "")
		#form = Ui_Form(self)
		#self.tab_2 = QtWidgets.QWidget()
		#self.tab_2.setObjectName("tab_2")
		#self.tabWidget.addTab(self.tab_2, "")
		self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 6) #1,0,1,5
		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 1476, 22))
		self.menuBar.setObjectName("menuBar")
		self.menuArchivo = QtWidgets.QMenu(self.menuBar)
		self.menuArchivo.setObjectName("menuArchivo")
		self.menuVista = QtWidgets.QMenu(self.menuBar)
		self.menuVista.setObjectName("menuVista")
		self.menuCircuito = QtWidgets.QMenu(self.menuBar)
		self.menuCircuito.setObjectName("menuCircuito")
		self.menuHerramientas = QtWidgets.QMenu(self.menuBar)
		self.menuHerramientas.setObjectName("menuHerramientas")
		self.menuReportes = QtWidgets.QMenu(self.menuBar)
		self.menuReportes.setObjectName("menuReportes")
		MainWindow.setMenuBar(self.menuBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)
		self.actionhh = QtWidgets.QAction(MainWindow)
		self.actionhh.setObjectName("actionhh")
		self.actionjjl = QtWidgets.QAction(MainWindow)
		self.actionjjl.setObjectName("actionjjl")
		self.actionhh_2 = QtWidgets.QAction(MainWindow)
		self.actionhh_2.setObjectName("actionhh_2")
		self.actionjjk = QtWidgets.QAction(MainWindow)
		self.actionjjk.setObjectName("actionjjk")
		self.actionjkjkj = QtWidgets.QAction(MainWindow)
		self.actionjkjkj.setObjectName("actionjkjkj")
		self.menuArchivo.addAction(self.actionhh)
		self.menuVista.addAction(self.actionjjl)
		self.menuCircuito.addAction(self.actionhh_2)
		self.menuHerramientas.addAction(self.actionjjk)
		self.menuReportes.addAction(self.actionjkjkj)
		self.menuBar.addAction(self.menuArchivo.menuAction())
		self.menuBar.addAction(self.menuVista.menuAction())
		self.menuBar.addAction(self.menuCircuito.menuAction())
		self.menuBar.addAction(self.menuHerramientas.menuAction())
		self.menuBar.addAction(self.menuReportes.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.comboBox.addItems(['Current','Voltage','Temperature','Step','Time left']) #addr pendiente, tiempo transcurrido
		
		self.cmbZoom.setEditable(True)
		self.cmbZoom.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("\\d\\d\\d?$"),self.centralWidget))
		self.cmbZoom.addItems(['25%','50%','75%','100%','125%','150%','175%','200%'])
		self.cmbZoom.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
		self.cmbZoom.setCurrentIndex(3)

	#	self.comboBox.activated.connect(self.onCombo)
		self.cmbZoom.activated.connect(self.onCmbZoom)

		self.cmdDetener.clicked.connect(self.btnDetener)
		self.cmdPausar.clicked.connect(self.btnPausar)
		self.cmdIniciar.clicked.connect(self.btnIniciar)
		self.cmdCargar.clicked.connect(self.btnCargar)
	
		#self.paint = Paint(self)
		#self.selAllShort = QtWidgets.QShortcut(QtGui.QKeySequence(QtGui.QKeySequence.ZoomIn),self.paint,context= QtCore.Qt.WidgetShortcut,)
		#self.selAllShort.activated.connect(self.zoom_in)
		#self.selAllShort = QtWidgets.QShortcut(QtGui.QKeySequence(QtGui.QKeySequence.ZoomOut),self.paint,context= QtCore.Qt.WidgetShortcut,)
		#self.selAllShort.activated.connect(self.zoom_out)

		MainWindow.showEvent = self.showEvent
		MainWindow.closeEvent = self.closeEvent
		MainWindow.resizeEvent = self.resizeEvent

		self.mylist = list()
		self.mylabel = list()
		self.rowCol = list()

		self.newlist = list()
		self.addrsT = list()
		self.tempAddr = list()

		self.Tabs = list()
		self.maxTabs = list()

		self.valueZoom = list()
		self.listSelect = list() #guarda valores de addr cuando se seleccionan modulos
		self.saveprograms = list() #guarda programs's name 

		self.flagStart = False
		self.flagPage = False
		self.flagNormal = True
		self.flagZoom = False
		self.flagWmin = False 	#Flag para ubuntu
		self.flagClose = False
		self.flagProg = False

		self.flagCircuit = False
		self.tmpTabs = list()
		
		self.labels = list()
		self.progress = list()
		self.lblmodule = list()		

		#self.valueZoomOut = list()
		#self.scaleFactor = 1.0
		self.MainWindow = MainWindow

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Formation Viewer"))
		self.cmdIniciar.setText(_translate("MainWindow", "Start"))
		self.cmdCargar.setText(_translate("MainWindow", "Load Programs / Start"))
		self.cmdDetener.setText(_translate("MainWindow", "Stop"))
		self.cmdPausar.setText(_translate("MainWindow", "Pause"))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
		self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
		self.menuVista.setTitle(_translate("MainWindow", "Vista"))
		self.menuCircuito.setTitle(_translate("MainWindow", "Circuito"))
		self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
		self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
		self.actionhh.setText(_translate("MainWindow", "hh"))
		self.actionjjl.setText(_translate("MainWindow", "jjl"))
		self.actionhh_2.setText(_translate("MainWindow", "hh"))
		self.actionjjk.setText(_translate("MainWindow", "jjk"))
		self.actionjkjkj.setText(_translate("MainWindow", "jkjkj"))

	def showEvent(self,event):
		print("ShowEvent") 
		if self.flagWmin != True: #Para ubuntu se necesito esta bandera
			self.flagWmin = True
		#if MainWindow.isMinimized(): #Para mac
		#	pass
		#else:
			settprog = QtCore.QSettings('/home/ditsa/DitsaNet/Settings/fileprograms.ini', QtCore.QSettings.NativeFormat)
			if settprog.value('/home/ditsa/DitsaNet/Settings/fileprograms.ini') !='':
				tmp = settprog.value("saveprograms")

				if tmp != None and len(tmp) != 0:
					self.saveprograms = tmp[:]
					self.flagProg = True
					print("savePR:",self.saveprograms)

			settings = QtCore.QSettings('/home/ditsa/DitsaNet/Settings/archivo.ini', QtCore.QSettings.NativeFormat)
			if settings.value('/home/ditsa/DitsaNet/Settings/archivo.ini')!='':
				self.settingsList = settings.value("mylist")
				self.settingsLabel = settings.value("mylabel")
				self.settingsRowCol = settings.value("rowcol")

				if self.settingsRowCol != None and len(self.settingsRowCol) !=0:
					self.rowCol = self.settingsRowCol[:]
				else:
					self.rowCol.append('1%')
					self.rowCol.append('R=10 C=10')

				if self.settingsList != None:
					self.mylist = self.settingsList[:] #para que no correspondan con el mismo objeto
					
					for i in range(2,len(self.mylist),4):
						self.newlist.append(self.mylist[i].replace('N=',''))

					ordName = NameOrdened(self.newlist) #manda a llamar la clase NameOrdened
					x = ordName.cod()					#ordena los elementos de la lista de < a >
					self.newlist.clear()
					self.tempAddr.clear()
					self.addrsT.clear()

					for i in range(len(x)):
						for j in range(2,len(self.mylist),4):
							if "N="+str(x[i]) == self.mylist[j]:
								self.newlist.append(self.mylist[j-2])
								self.newlist.append(self.mylist[j-1])
								self.newlist.append(self.mylist[j])
								self.newlist.append(self.mylist[j+1])
								valAddr = self.mylist[j+1].split('A=')
								self.tempAddr.append(valAddr[1])

					self.addrsT.append(str(self.tempAddr))
					

				if self.settingsLabel != None:
					self.mylabel = self.settingsLabel[:] #para que no correspondan con el mismo objeto

				if self.settingsList != None or self.settingsLabel != None: # Populate Tables
					self.populateTabs()

					self.paint = Paint(self)
					self.tabWidget.addTab(self.paint, "Page 1")
					tabC = self.tabWidget.count()

					MainWindow.showMaximized()
					self.paint.setSceneRect(0,0,0,0)

					if (self.settingsList != None  and len(self.settingsList)!=0) or (self.settingsLabel != None and len(self.settingsLabel)!=0):
						for i in range(int(self.numTabT)-tabC):
							self.newPage()

					self.onCmbZoom()

					BCmb.pingDataClient(useHostname,self.addrsT[0]) #envia las addr de los modulos 
					#enviar actualizacion del ultimo program guardado 
					#print("addrT:",self.addrsT[0])
					#print(self.addrsT[1])
					#print(self.addrsT[2])
					#depreferencia que regrese valores addr answer
					#if self.flagProg != False:
					#	for i in range(len(self.addrsT)):
					#		BCmb.writeProgramClient(useHostname,self.addrsT[i],self.programJson)
					
					print("Inicia Poleo") #poleo es lo primero en iniciar despues de llenar screen
					self.threadData(True) #Inicia el poleo
			
					time.sleep(0.3)
					self.valueData() #obtiene los valores del poleo del sever

	def closeEvent(self,event):
		print("closeEvent")
		self.flagClose = True
		time.sleep(0.5)
		self.threadTimer(False)	
		self.threadData(False)

	def threadData(self,flag):
		print("ThreadData")
		if flag == True:
			self.dataThread = None
			self.dataThread = DataListenerMemory(self.testsCallback)
			self.dataThread.start()
		else:
			self.dataThread.stop()

	def threadTimer(self,flag):
		print("ThreadTimer")
		if flag == True:
			self.t = None
			self.t = threading.Timer(1, self.valueData)
			self.t.start()
		else:
			self.t.cancel()

	def populateTabs(self):
		print("populateTabs")
		for i in range(0,len(self.settingsList),4):
			self.maxTabs.append(self.settingsList[i])

		for i in range(0,len(self.settingsLabel),3):
			self.maxTabs.append(self.settingsLabel[i])

		if len(self.maxTabs)!= 0:
			y = max(self.maxTabs)
			self.numTabT = y.replace('%','')
			self.maxTabs.clear()

	def newPage(self): 
		#print("newPage")
		self.flagPage = True
		self.flagNormal = False
		self.paint = Paint(self)
		self.paint.setSceneRect(0,0,0,0)
		self.tabWidget.addTab(self.paint,"Page "+str(self.tabWidget.count()+1))

	#def onCombo(self): #seleccion I,V,T,time,Step,addr
	#	print("comboBox")
		
	def onCmbZoom(self): ###verificar funcionamiento 
		print("cmbZoom") ##se puede cambiar aun no finalizado
		textcmb = self.cmbZoom.currentText()
		y = textcmb.split('%')
		value = ''.join(y)
		det = int(value) / 125
		
		form = self.tabWidget.currentWidget()
		form.zoomCmb(det)

	def testsCallback(self, msg):
		if "DL[PASS]" in msg:
			msg = msg.replace("DL[PASS]:","")
		
			cbText = self.comboBox.currentText()
			cbText2 =  self.comboBox.currentIndex()+1

			if cbText == 'Current':
				pref = " A"

			elif cbText == 'Voltage':
				pref = " V"

			elif cbText == 'Temperature':
				pref = " C"

			elif cbText == 'Time left':
				pref = ''

			elif cbText == 'Step':
				pref = ''
			 
			for i in range(1,len(self.labels),3):
				addr = self.labels[i+1]

				font = QtGui.QFont()
				font.setFamily("Ubuntu Light")
				font.setPointSize(12)
				font.setBold(True)
				font.setWeight(75)

				self.labels[i].setFont(font)
				self.labels[i].setText(shared.DEV[addr][cbText2]+pref)

				if shared.DEV[addr][0] == False: # state - No comm
					font = QtGui.QFont()
					font.setFamily("Ubuntu Light")
					font.setPointSize(10)
					font.setBold(True)
					font.setWeight(75)
					self.labels[i].setFont(font)
					self.labels[i].setText("NO COMM")
					self.labels[i].setStyleSheet("QLabel {background-color : gold; color : black; border: 1px solid black;} ")
					self.labels[i].setAlignment(QtCore.Qt.AlignCenter)

				elif (shared.DEV[addr][8] == 'I') or (shared.DEV[addr][8] == 'S'): #state - Stop or Initial
					self.labels[i].setStyleSheet("QLabel {background-color : lightblue; color : black; border: 1px solid black;} ")
					self.labels[i].setAlignment(QtCore.Qt.AlignCenter)
					self.progress[i].setValue(0)

				elif shared.DEV[addr][8] == 'E': #state - End Program
					self.labels[i].setStyleSheet("QLabel {background-color : orange; color : black; border: 1px solid black;} ")
					self.labels[i].setAlignment(QtCore.Qt.AlignCenter)
					self.progress[i].setValue(0)

				elif shared.DEV[addr][8] == 'R': #state - Running
					self.labels[i].setStyleSheet("QLabel {background-color : limegreen; color : black; border: 1px solid black;} ")
					self.labels[i].setAlignment(QtCore.Qt.AlignCenter)

				elif shared.DEV[addr][8] == 'P': #state - Pause
					self.labels[i].setStyleSheet("QLabel {background-color : mediumpurple; color : black; border: 1px solid black;} ")
					self.labels[i].setAlignment(QtCore.Qt.AlignCenter)

				elif (shared.DEV[addr][8] == 'T') or (shared.DEV[addr][8] == 'W'): #state - temp-hight or current warning
					self.labels[i].setStyleSheet("QLabel {background-color : red; color : black; border: 1px solid black;} ")
					self.labels[i].setAlignment(QtCore.Qt.AlignCenter) #red

			for j in range(1,len(self.progress),3):
				addr = self.progress[j+1]
				
				if shared.DEV[addr][0] != False: 
					if float(shared.DEV[addr][6])*100 == 0:
						self.progress[j].setValue(0)
					else:
						value = float(shared.DEV[addr][6])*100 / float(shared.DEV[addr][7])
						self.progress[j].setValue(value)

	def valueData(self):
		print("VALUEDATA")
		memoryData = BCmb.memoryDataClient(useHostname)
		
		for i in range (len(self.tempAddr)): 
			address = i
			if memoryData!= None:
				#print("ValueM:",memoryData)
				TempData = memoryData[address-1].split(',')
				#print("TempData:",TempData)
				dat1 = str(TempData[0]).replace('{','')
				#print("data1:",dat1)
			
				if dat1 == 'True' and len(TempData) == 9:
					TempData[8] = str(TempData[8]).replace('}','')
					TempData[0] = True

					shared.DEV[address][0] = TempData[0]
					#we store current
					shared.DEV[address][1] = str(TempData[1].replace('I',''))
					#we store voltage
					shared.DEV[address][2] = str(TempData[2].replace('V',''))
					#we store temperature
					shared.DEV[address][3] = str(TempData[3].replace('T',''))
					#we store step number and type
					shared.DEV[address][4] = str(TempData[4].replace('S',''))
					#we store time of current step
					shared.DEV[address][5] = str(TempData[5].replace('t',''))
					#we store current time program
					shared.DEV[address][6] = str(TempData[6].replace('Tt',''))
					#we store the total time program
					shared.DEV[address][7] = str(TempData[7].replace('TT',''))
					#we store the total time program
					shared.DEV[address][8] = str(TempData[8].replace('',''))

				elif dat1 == 'False}':
					TempData[0] = str(TempData[0]).replace('}','')
					shared.DEV[address][0] = False
				
				print("TempData2:",TempData)
		
		if self.flagClose != True:
			self.threadTimer(True)
		else:
			self.threadTimer(False)


	count = 0
	def resizeEvent(self,event): #verificar con ubuntu como trabaja
		print("changeEvent")
		self.count+= 1
		if self.count != 1:

			if MainWindow.isMaximized() and self.flagNormal != True:
				self.flagNormal = True
				#MainWindow.showNormal() #asigna el valor original del resize
				x = self.tabWidget.currentWidget()
				x.showEvent(event)
			
			else:
				#print("else max")
				self.flagPage = False
				self.flagNormal = False
				#MainWindow.showMaximized()
				x = self.tabWidget.currentWidget()
				x.showEvent(event)

	def btnDetener(self):
		print("Detener")
		Ui_stopModule(self).exec_()
		self.threadData(True)

	def btnPausar(self):
		print("Pausar")
		Ui_pauseModule(self).exec_()
		self.threadData(True)

	def btnIniciar(self): 
		print("Iniciar")
		Ui_runModule(self).exec_()
		self.threadData(True)

	def btnCargar(self):
		print("Cargar")
		Ui_WindowCh(self).exec_()

		self.threadData(True)
		self.valueData()

	'''
	def zoom_in(self):
		print("zoom_in")
		scale_tr = QtGui.QTransform()
		scale_tr.scale(Paint.factor, Paint.factor)
		
		tr = self.paint.transform() * scale_tr
		self.paint.setTransform(tr)

		#self.scaleFactor *= Paint.factor
		#print("f1:",self.scaleFactor)
		#self.paint.resize(self.scaleFactor * self.paint.form.size() * 8)
		#print(self.scaleFactor * self.paint.form.size()* 8)

	def zoom_out(self):
		print("zoom_out")
		scale_tr = QtGui.QTransform()
		scale_tr.scale(Paint.factor, Paint.factor)

		scale_inverted, invertible = scale_tr.inverted()
		
		if invertible:
			tr = self.paint.transform() * scale_inverted
			self.paint.setTransform(tr)

		#self.scaleFactor *= 0.8
		#print("f2:",self.scaleFactor)
		#self.paint.resize(self.scaleFactor * self.paint.form.size()* 8)
		#print(self.scaleFactor * self.paint.form.size()* 8)

	'''

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow(MainWindow)
	#ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
