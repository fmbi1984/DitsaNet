# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from io import open 
from os import scandir
import time 

from devicemainboard import BCmb
from appsettings import useIp,usePort,useAddr
from Opath import pathPrograms
import shared

#from ordened import NameOrdened

class Ui_WindowCh(QtWidgets.QDialog):
	#def setupUi(self, WindowCh):
	def __init__(self,parent=None):
		super(Ui_WindowCh, self).__init__()
		self.parent = parent

		self.setObjectName("WindowCh")
		self.setFixedSize(392, 421) #self.setFixedSize(392, 384) 533-663
		self.BttnCancel = QtWidgets.QPushButton(self)
		self.BttnCancel.setGeometry(QtCore.QRect(100, 180, 80, 25))
		self.BttnCancel.setObjectName("BttnCancel")
		#self.BttnLoad = QtWidgets.QPushButton(self)
		#self.BttnLoad.setGeometry(QtCore.QRect(170, 180, 80, 25))
		#self.BttnLoad.setObjectName("BttnLoad")
		self.BttnStart = QtWidgets.QPushButton(self)
		self.BttnStart.setGeometry(QtCore.QRect(230, 180, 80, 25)) #(280, 180, 80, 25))
		self.BttnStart.setObjectName("BttnStart")

		self.textPrograms = QtWidgets.QComboBox(self)
		self.textPrograms.setGeometry(QtCore.QRect(50, 60, 301, 25))
		self.textPrograms.setObjectName("textPrograms")
		self.lblPrograms = QtWidgets.QLabel(self)
		self.lblPrograms.setGeometry(QtCore.QRect(160, 16, 81, 31))
		self.lblPrograms.setObjectName("lblPrograms")
		self.lblModules = QtWidgets.QLabel(self)
		self.lblModules.setGeometry(QtCore.QRect(130, 100, 151, 21))
		self.lblModules.setObjectName("lblModules")
		self.layoutWidget = QtWidgets.QWidget(self)
		self.layoutWidget.setGeometry(QtCore.QRect(80, 140, 251, 27))
		self.layoutWidget.setObjectName("layoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.lineEditMin = QtWidgets.QLineEdit(self.layoutWidget)
		self.lineEditMin.setObjectName("lineEditMin")
		#self.lineEditMin.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[-A-Za-z\\d]*$"),self))
		self.lineEditMin.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[-A-Za-z\\d]*,[0-9]{1,2}$"),self))
		self.horizontalLayout.addWidget(self.lineEditMin)
		self.label = QtWidgets.QLabel(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.lineEditMax = QtWidgets.QLineEdit(self.layoutWidget)
		self.lineEditMax.setObjectName("lineEditMax")
		self.lineEditMax.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[-A-Za-z\\d]*$"),self))
		self.horizontalLayout.addWidget(self.lineEditMax)
		self.listWidget = QtWidgets.QListWidget(self)
		self.listWidget.setGeometry(QtCore.QRect(391, 0, 141, 421))
		self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
		self.listWidget.setObjectName("listWidget")
		self.BtnArrowR = QtWidgets.QPushButton(self)
		self.BtnArrowR.setGeometry(QtCore.QRect(300, 220, 89, 25))
		self.BtnArrowR.setObjectName("BtnArrowR")
		self.textEdit = QtWidgets.QTextEdit(self)
		self.textEdit.setGeometry(QtCore.QRect(0, 250, 391, 171))
		self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
		self.textEdit.setObjectName("textEdit")
		self.BtnArrowL = QtWidgets.QPushButton(self)
		self.BtnArrowL.setGeometry(QtCore.QRect(0, 220, 89, 25))
		self.BtnArrowL.setObjectName("BtnArrowL")
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setGeometry(QtCore.QRect(0, 420, 391, 241))
		self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
		self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget.setAlternatingRowColors(True)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(5)
		self.tableWidget.setRowCount(0)
		self.tableWidget.setHorizontalHeaderLabels(('Operation','Nominal','Time','Temp Max','Temp Min'))

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

		self.loadProg = list()
		self.addrs = list()
		self.check = list()
		self.tempList = list()
		self.prueba = list()

		self.data1 = None
		self.data2 = None
		self.stepAddrs = None
		self.flagOutL = False
		self.flagChange = False

		self.flagFail = False	#flag para controlar el cierre de windowch
		self.intentos = 0

	def retranslateUi(self, WindowCh):
		_translate = QtCore.QCoreApplication.translate
		WindowCh.setWindowTitle(_translate("WindowCh", "Programs"))
		self.BttnCancel.setText(_translate("WindowCh", "Cancel"))
	#	self.BttnLoad.setText(_translate("WindowCh", "Load"))
		self.BttnStart.setText(_translate("WindowCh", "Start"))
		self.lblPrograms.setText(_translate("WindowCh", "Programs"))
		self.lblModules.setText(_translate("WindowCh", "Selection of Modules"))
		self.label.setText(_translate("WindowCh", "-"))
		self.BtnArrowR.setText(_translate("WindowCh", ">>"))
		self.BtnArrowL.setText(_translate("WindowCh", "<<"))

		self.BtnArrowR.clicked.connect(self.on_bttnArrowR)
		self.BtnArrowL.clicked.connect(self.on_bttnArrowL)
		self.BttnStart.setDefault(True)
		self.lineEditMin.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditMax.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditMin.setMaxLength(8)
		self.lineEditMax.setMaxLength(8)
		self.lineEditMin.textChanged.connect(self.on_editMin)
		self.lineEditMax.textChanged.connect(self.on_editMax)
	#	self.BttnLoad.clicked.connect(self.on_BttnLoadClicked)
		self.BttnCancel.clicked.connect(self.on_bttnCancelClicked)
		self.BttnStart.clicked.connect(self.on_BttnStart)

		self.textPrograms.addItem('')
		self.textPrograms.activated.connect(self.loadTableW)
		#self.listWidget.itemClicked.connect(self.uncheck_check)
		#self.textEdit.textChanged.connect(self.chtext)

		self.lineEditMin.setFocus(True)
		#self.parent.lblmodule.editingFinished.connect(self.prueba) OJO!!

	def showEvent(self,event):
		print("showEventWindowCh1")
		for i in range(1,len(self.parent.lblmodule),3):
			if self.parent.lblmodule[i].isDown():
				self.lineEditMin.setText(self.parent.lblmodule[i].text())
				break

		self.on_cb_textPrograms()

	def closeEvent(self,event):
		print("closeEventW")

	def prueba(self):
		print("PRUEBA")

	def on_editMin(self):
		y = self.lineEditMin.text()
		txt = y.upper()
		self.lineEditMin.setText(txt)

		self.stepAddrs = ""
		if txt.count(',')==1:  
			txt0 = txt.partition(",")
			self.data1 = "N="+txt0[0]
			self.stepAddrs = txt0[2]
		else:
			self.data1 = "N="+txt
		
		self.on_editMax()

	def on_editMax(self):
		y = self.lineEditMax.text()
		txt = y.upper()
		self.lineEditMax.setText(txt)
		self.data2 = "N="+txt
		self.flagChange = False
		
		try:
			self.flagOutL = False
			value1 = self.parent.newlist.index(self.data1)
			value2 = self.parent.newlist.index(self.data2)

			self.flagChange = True
			value1 = value1 - 2
			value2 = value2 + 2

			valF = self.parent.newlist[value1:value2]
			self.check.clear()
			for i in range(2,len(valF),4):
				self.check.append(valF[i].replace('N=',''))
				self.check.append(valF[i+1].replace('A=',''))

			self.btnCheckBox()

		except:
			self.flagChange = True
			if self.data1 != None and self.data1 !='N=':
				try:
					val1 = self.parent.newlist.index(self.data1)

					val1 = val1 - 2
					valF = self.parent.newlist[val1:val1+4]
					self.check.clear()
					for i in range(2,len(valF),4):
						self.check.append(valF[i].replace('N=',''))
						self.check.append(valF[i+1].replace('A=',''))

					self.btnCheckBox()
				except:
					self.listWidget.clear()
			else:
				self.listWidget.clear()

			if self.data2 != None and self.data2 != 'N=':
				self.flagOutL = True
				self.listWidget.clear()

	def uncheck_check(self):
		self.tempList.clear()
		for index in range(self.listWidget.count()):
			if self.listWidget.item(index).checkState() == QtCore.Qt.Checked:
				self.tempList.append(self.listWidget.item(index).text())

		self.loadProg.clear()
		for i in range(2,len(self.parent.newlist),4):
			for j in range(len(self.tempList)):
				if 'N='+self.tempList[j] == self.parent.newlist[i]:
					self.loadProg.append(self.parent.newlist[i-2])
					self.loadProg.append(self.parent.newlist[i-1])
					self.loadProg.append(self.parent.newlist[i])
					self.loadProg.append(self.parent.newlist[i+1])

	def btnCheckBox(self):
		if self.flagChange != False:
			self.flagChange = False
			self.listWidget.clear()

			for i in range(0,len(self.check),2):
				item = QtWidgets.QListWidgetItem(self.check[i])

				if shared.DEV[int(self.check[i+1])][0] == False:
					item.setFlags(QtCore.Qt.ItemIsUserCheckable)
					item.setCheckState(QtCore.Qt.Unchecked)
				else:
					item.setFlags(item.flags()|QtCore.Qt.ItemIsUserCheckable)
					item.setCheckState(QtCore.Qt.Checked)	

				self.listWidget.addItem(item)

	def on_cb_textPrograms(self):
		files=self.ls2(pathPrograms)			#"/home/digitek/DitsaNet/ProfileEditorPrograms/"
		for file in files:
			nf = file.replace('.txt','')
			self.textPrograms.addItem(nf)

	def ls2(self,path): 
		return [obj.name for obj in scandir(path) if obj.is_file()]


	programJson = ""
	def on_clicked_textPrograms(self):
		self.nameFile = self.textPrograms.currentText()
		if self.nameFile != '':
			openFile = self.nameFile+".txt"
			#print("nameFile:",self.nameFile)
			archivo_texto = open(pathPrograms+openFile,"r")
			self.programJson = archivo_texto.read()
			archivo_texto.close()
			#print("json:",self.programJson)

	def chtext(self,flag,addr):
		if flag == 'msg':
			self.textEdit.setText('Send programs ...')
			#self.textEdit.append("Send programs...")
		elif flag == 'msgP':
			self.textEdit.setText("...")
		elif flag == 'None':
			self.textEdit.append("ERROR COMMUNICATION: "+addr)
		elif flag == 'PASS':
			self.textEdit.append("Load successful in name: "+addr)
		elif flag == 'FAIL':
			self.textEdit.append("Fail Load name: "+addr)
		elif flag == 'PASS,RUN':
			self.textEdit.append("run successful in name: "+addr)
		elif flag == 'FAIL,RUN':
			self.textEdit.append("Fail run Addr: "+addr)

		QtGui.QGuiApplication.processEvents()

	'''
	def on_BttnLoadClicked(self):
		print("ClickLoad")
		#----------------------------- Detiene thread -----------------------------#
		#self.parent.threadTimer(False)
		#if self.flagFail != True:
		#print("thData: ",self.parent.threadData)
		self.parent.threadData(False)
		time.sleep(1)
		#---------------------------- Extrae valor Addr ---------------------------#
		self.uncheck_check()
		self.addrs.clear()
		
		if len(self.tempList)!=0:  #indica que hay equipos conectados
			if self.flagFail != True:
				self.prueba.clear()
				for i in range(3,len(self.loadProg),4):
					addr = self.loadProg[i].split('A=')
					self.addrs.append(addr[1])
				self.loadProg.clear()
			else:
				self.addrs = self.prueba[:]
				self.prueba.clear()

			self.textEdit.clear()
			self.flagFail = False
			#---------------------------- Envia json a xmegas -------------------------#
			self.chtext("msg","None")
			if self.textPrograms.currentText() != '':
				for j in range(len(useIp)):
					section = useAddr[j]
					for k in range(len(self.addrs)):
						if section == self.addrs[k]:
							t = self.check.index(self.addrs[k])
							self.intentos = 0
							while self.intentos < 4: #Hace 3 intentos 
								print("Intentos:",self.intentos)
								
								for i in range(17):
									x = BCmb.writeProgramClient(useIp[j],usePort,self.step[i])
									time.sleep(0.1)
									#agregar timeout posible solucion
									if x == None:
										self.flagFail = True
										self.intentos+=1
										print("primer")
										if self.prueba.count(self.addrs[k]) == 0:
											self.prueba.append(self.addrs[k])
										break
										#time.sleep(0.3)
							
								#if x != None:
								if x == 'ACTION.PASS':
									time.sleep(8)
									self.chtext('PASS',self.check[t-1])
									#self.BttnStart.setEnabled(True)
									self.intentos = 4
									if len(self.prueba) != 0:
										self.prueba.remove(self.addrs[k])	
								else:
									self.intentos+=1
									print("Segundo") #checar esta parte

							print("A esta altura falta otro")
							#simplificar
							#hacer pruebas en esta parte y checar si se puede quitar boton load 
							#se identifique load si esta cargado un archivo si no ,solo es start
							#si esta cargado archivo es load y despues start
							
							#self.chtext('FAIL',self.check[t-1])
							#print("Intenta Nuevamente")
							#if self.flagFail != True:
							#	self.flagFail = True
							#	if self.prueba.count(self.addrs[k]) == 0:
							#		self.prueba.append(self.addrs[k])
							
							#else:
							#	print("Error Intenta")
							#	intentos+=1
							#	self.chtext('None',self.check[t-1])
							#	if self.flagFail != True:
							#		self.flagFail = True
							#		if self.prueba.count(self.addrs[k]) == 0:
							#			self.prueba.append(self.addrs[k])
							
		else:
			self.chtext("None","---")

	def on_BttnStart(self):
		print("Start")
		if self.flagFail != True:
			self.addrs.clear()
			self.prueba.clear()
			for x in range(1,len(self.check),2):
				self.addrs.append(self.check[x])
		else:
			self.addrs = self.prueba[:]
			self.prueba.clear()

		self.flagFail = False
		for j in range(len(useIp)):
			section = useAddr[j]
			for k in range(len(self.addrs)):
				if section == self.addrs[k]:
					t = self.check.index(self.addrs[k])
					run = BCmb.runClient(useIp[j],usePort,self.stepAddrs)
					time.sleep(0.1)
					print("RUN-ACTION-PASS")

					if run != None:
						if run == 'PASS,RUN':
							self.chtext(run,self.check[t-1])
							#time.sleep(3)
							#self.close()
						else:
							self.chtext('None',self.check[t-1])
							if self.prueba.count(self.addrs[k]) == 0:
								self.prueba.append(self.addrs[k])
							self.flagFail = True
					else:
						self.chtext('FAIL',self.check[t-1])
						if self.prueba.count(self.addrs[k]) == 0:
							self.prueba.append(self.addrs[k])
						self.flagFail = True

		if self.flagFail != True and (self.intentos == 4 or self.intentos == 0):
				time.sleep(2)
				self.close()
	'''
	def on_BttnStart(self):
		print("Start")
		#----------------------------- Detiene thread -----------------------------#
		self.parent.threadData(False)
		time.sleep(1)
		#---------------------------- Extrae valor Addr ---------------------------#
		self.uncheck_check()
		self.addrs.clear()

		if len(self.tempList)!=0:  #indica que hay equipos conectados
			if self.flagFail != True:
				self.prueba.clear()
				for i in range(3,len(self.loadProg),4):
					addr = self.loadProg[i].split('A=')
					self.addrs.append(addr[1])
				self.loadProg.clear()
			else:
				self.addrs = self.prueba[:]
				self.prueba.clear()

			self.textEdit.clear()
			self.flagFail = False
			#---------------------------- Envia json a xmegas -------------------------#
			self.chtext("msg","None")
			if self.textPrograms.currentText() != '':
				for j in range(len(useIp)):
					section = useAddr[j]
					for k in range(len(self.addrs)):
						if section == self.addrs[k]:
							t = self.check.index(self.addrs[k])
							self.intentos = 0
							while self.intentos < 4: #Hace 3 intentos 
								
								for i in range(17):
									x = BCmb.writeProgramClient(useIp[j],usePort,self.step[i])
									time.sleep(0.1)
									if x == None:
										self.flagFail = True
										self.intentos+=1
										print("primer")
										if self.prueba.count(self.addrs[k]) == 0:
											self.prueba.append(self.addrs[k])
										break

								if x == 'ACTION.PASS':
									time.sleep(8)
									self.chtext('PASS',self.check[t-1])
									self.intentos = 4
									if len(self.prueba) != 0:
										self.prueba.remove(self.addrs[k])	

									time.sleep(2)
									self.onlyStart()
									break
								else:
									self.intentos+=1
									print("Segundo") #checar esta parte
							
								print("Intentos:",self.intentos)

							self.chtext('None',self.check[t-1])
			else:
				self.onlyStart()

	def onlyStart(self):
		print("Only start")
		if self.flagFail != True:
			self.addrs.clear()
			self.prueba.clear()
			for x in range(1,len(self.check),2):
				self.addrs.append(self.check[x])
		else:
			self.addrs = self.prueba[:]
			self.prueba.clear()

		self.flagFail = False
		for j in range(len(useIp)):
			section = useAddr[j]
			for k in range(len(self.addrs)):
				if section == self.addrs[k]:
					t = self.check.index(self.addrs[k])
					run = BCmb.runClient(useIp[j],usePort,self.stepAddrs)
					time.sleep(0.1)

					if run != None:
						if run == 'PASS,RUN':
							self.chtext(run,self.check[t-1])

						else:
							self.chtext('None',self.check[t-1])
							if self.prueba.count(self.addrs[k]) == 0:
								self.prueba.append(self.addrs[k])
							self.flagFail = True
					else:
						self.chtext('FAIL',self.check[t-1])
						if self.prueba.count(self.addrs[k]) == 0:
							self.prueba.append(self.addrs[k])
						self.flagFail = True

		if self.flagFail != True and (self.intentos == 4 or self.intentos == 0):
				time.sleep(2)
				self.close()
		else:
			self.chtext("None","---")
				
	def checkPrograms(self,addr):
		print("checkPrograms")
		if self.parent.saveprograms!= None:
			if len(self.parent.saveprograms) != 0:
				for j in range(1,len(self.parent.saveprograms),2):
					if 'A='+addr == self.parent.saveprograms[j]:
						self.parent.saveprograms.pop(j)
						self.parent.saveprograms.pop(j-1)
						break
			
	def on_bttnCancelClicked(self):
		self.close()
		#cambiar este widget estructuralo mejor

	def loadTableW(self):
		print("loadProgramsTable")
		self.on_clicked_textPrograms()
		xx = ""
		self.step = list()

		for i in range(len(self.programJson)):
			if self.programJson[i] == '"':
				if xx != "":
					xx += "\"" 
			else:
				if (self.programJson[i] == "," and self.programJson[i-1] != "}" and self.programJson[i-1] != ",") or (self.programJson[i] != "," and self.programJson[i-1] != "}"):
					xx += self.programJson[i]
			
				if self.programJson[i] == "}" and (self.programJson[i+1] == "," or self.programJson[i+1] == "]"):
					xx += self.programJson[i+1]
					self.step.append(xx)
					xx = ""
		
		self.tableWidget.setRowCount(15)
		self.st = 0
		for i in range(len(self.step)):
			comp = self.step[i].split("'")
			compAux = comp[0].split('{')
			final = compAux[1].split(',')
			
			for j in range(len(final)):
				if final[0] == '"T":"Ch"':
					self.st += 1
					comp0 = final[j+1].split('"C":')
					comp1 = final[j+2].split('"A":')
					comp2 = final[j+3].split('"M":')
					comp3 = final[j+4].split('"m":')

					comp5 = comp3[1].split('}')

					self.tabItem('Charge',self.st-1,j)
					self.tabItem(str(float(comp0[1].split('"')[1])),self.st-1,j+1) #current

					if len(comp1) == 1:
						comp1 = final[j+2].split('"H":')
						self.tabItem(str(float(comp1[1].split('"')[1]))+'   T',self.st-1,j+2) # H
					else:
						self.tabItem(str(float(comp1[1].split('"')[1]))+'    AH',self.st-1,j+2) # ampH

					self.tabItem(str(float(comp2[1].split('"')[1])),self.st-1,j+3) #maxTmp
					self.tabItem(str(float(comp5[0].split('"')[1])),self.st-1,j+4) #minTmp
					
					break
					
				elif final[0] == '"T":"Pa"':
					self.st +=1
					self.tabItem('Pause',self.st-1,j)
					comp4 = final[j+1].split('"           H":')
				
					self.tabItem('-',self.st-1,j+1)
					self.tabItem(str(float(comp4[1].split('"')[1]))+'    T',self.st-1,j+2) #time
					self.tabItem('-',self.st-1,j+3)
					self.tabItem('-',self.st-1,j+4)
					break

	def tabItem(self,name,rw,col):
		lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
		item = QtWidgets.QTableWidgetItem(name)
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		item.setFont(lblt)
		#item.setBackground(QtGui.QColor('lightblue'))
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
		self.tableWidget.setItem(rw,col,item)

	flagClickR = False
	def on_bttnArrowR(self):
		#print("arrowR")
		if self.flagClickR != True and self.flagClickL !=True:
			self.flagClickR = True
			self.setFixedSize(533, 421)

		elif self.flagClickR != False and self.flagClickL !=False:
			self.flagClickR = False
			self.setFixedSize(392, 663)

		elif self.flagClickR != True and self.flagClickL !=False:
			self.flagClickR = True
			self.setFixedSize(533, 663)

		elif self.flagClickR != False and self.flagClickL !=True:
			self.flagClickR = False
			self.setFixedSize(392, 421)

		if self.flagOutL != True:
			self.btnCheckBox()


	flagClickL = False
	def on_bttnArrowL(self):
		#print("arrowL")
		if self.flagClickL != True and self.flagClickR != True:
			self.flagClickL = True
			self.setFixedSize(392, 663)

		elif self.flagClickL != False and self.flagClickR != False:
			self.flagClickL = False
			self.setFixedSize(533, 421)

		elif self.flagClickL != True and self.flagClickR !=False:
			self.flagClickL = True
			self.setFixedSize(533, 663)

		elif self.flagClickL != False and self.flagClickR !=True:
			self.flagClickL = False
			self.setFixedSize(392, 421)

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	WindowCh = QtWidgets.QDialog()
	ui = Ui_WindowCh()
	ui.setupUi(WindowCh)
	WindowCh.show()
	sys.exit(app.exec_())
'''