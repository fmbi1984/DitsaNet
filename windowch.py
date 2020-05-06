# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from io import open 
from os import scandir

from devicemainboard import BCmb
from appsettings import useHostname

from ordened import NameOrdened


class Ui_WindowCh(QtWidgets.QDialog):
	#def setupUi(self, WindowCh):
	def __init__(self,parent=None):
		super(Ui_WindowCh, self).__init__()
		self.parent = parent

		self.setObjectName("WindowCh")
		self.setFixedSize(392, 421) #self.setFixedSize(392, 384) 533-663
		self.BttnCancel = QtWidgets.QPushButton(self)
		self.BttnCancel.setGeometry(QtCore.QRect(110, 190, 80, 25))
		self.BttnCancel.setObjectName("BttnCancel")
		self.BttnDone = QtWidgets.QPushButton(self)
		self.BttnDone.setGeometry(QtCore.QRect(220, 190, 80, 25))
		self.BttnDone.setObjectName("BttnDone")
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
		self.lineEditMin.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[-A-Za-z\\d]*$"),self))
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
		self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
		self.plainTextEdit.setGeometry(QtCore.QRect(0, 250, 391, 171))
		self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
		self.plainTextEdit.setObjectName("plainTextEdit")
		self.BtnArrowL = QtWidgets.QPushButton(self)
		self.BtnArrowL.setGeometry(QtCore.QRect(0, 220, 89, 25))
		self.BtnArrowL.setObjectName("BtnArrowL")
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setGeometry(QtCore.QRect(0, 420, 391, 241))
		self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(0)
		self.tableWidget.setRowCount(0)

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

		self.newlist = list()
		self.check = list()
		self.data1 = None
		self.data2 = None
		self.flagOutL = False

	def retranslateUi(self, WindowCh):
		_translate = QtCore.QCoreApplication.translate
		WindowCh.setWindowTitle(_translate("WindowCh", "Programas"))
		self.BttnCancel.setText(_translate("WindowCh", "Cancelar"))
		self.BttnDone.setText(_translate("WindowCh", "Hecho"))
		self.lblPrograms.setText(_translate("WindowCh", "Programas"))
		self.lblModules.setText(_translate("WindowCh", "Selección de Módulos"))
		self.label.setText(_translate("WindowCh", "-"))
		self.BtnArrowR.setText(_translate("WindowCh", ">>"))
		self.BtnArrowL.setText(_translate("WindowCh", "<<"))

		self.BtnArrowR.clicked.connect(self.on_bttnArrowR)
		self.BtnArrowL.clicked.connect(self.on_bttnArrowL)
		self.BttnDone.setDefault(True)
		self.lineEditMin.setMaxLength(8)
		self.lineEditMax.setMaxLength(8)
		self.lineEditMin.textChanged.connect(self.on_editMin)
		self.lineEditMax.textChanged.connect(self.on_editMax)
		self.BttnDone.clicked.connect(self.on_bttnDoneClicked)
		self.BttnCancel.clicked.connect(self.on_bttnCancelClicked)


	def showEvent(self,event):
		print("showEventWindowCh")
		self.on_cb_textPrograms()

		for i in range(2,len(self.parent.mylist),4):
			self.newlist.append(self.parent.mylist[i].replace('N=',''))

		ordName = NameOrdened(self.newlist) #manda a llamar la clase NameOrdened
		x = ordName.cod()					#ordena los elementos de la lista de < a >

		print("xW:",x)

		self.newlist.clear()

		for i in range(len(x)):
			for j in range(2,len(self.parent.mylist),4):
				if "N="+str(x[i]) == self.parent.mylist[j]:
					self.newlist.append(self.parent.mylist[j-2])
					self.newlist.append(self.parent.mylist[j-1])
					self.newlist.append(self.parent.mylist[j])
					self.newlist.append(self.parent.mylist[j+1])

		print("new:",self.newlist)
		

	def closeEvent(self,event):
		print("closeEventW")

	def on_editMin(self):
		y = self.lineEditMin.text()
		txt = y.upper()
		self.lineEditMin.setText(txt)
		self.data1 = "N="+txt
		self.on_editMax()

		'''
		for i in range(2,len(self.parent.mylist),4):
			if self.parent.mylist[i] == "N="+y:
				self.addr1 = self.parent.mylist[i+1]
				self.addr1 = int(self.addr1.replace('A=',''))
				print("addr1:",self.addr1)
		'''

	def on_editMax(self):
		y = self.lineEditMax.text()
		txt = y.upper()
		self.lineEditMax.setText(txt)
		self.data2 = "N="+txt
		print("data1:",self.data1)
		print("data2:",self.data2)
		
		try:
			self.flagOutL = False
			value1 = self.newlist.index(self.data1)
			value2 = self.newlist.index(self.data2)

			value1 = value1 - 2
			value2 = value2 + 2

			valF = self.newlist[value1:value2]
			print("valF:",valF)
			self.check.clear()
			for i in range(2,len(valF),4):
				self.check.append(valF[i].replace('N=',''))

			self.btnCheckBox()
			print("self.check:",self.check)
			print("lenValF:",int(len(valF)/4))

		except:
			print("except")
			if self.data1 != None and self.data1 !='N=':
				try:
					val1 = self.newlist.index(self.data1)

					val1 = val1 - 2

					#print("val1:",val1)
					#print("newL:",self.newlist)
					valF = self.newlist[val1:val1+3]
					#print("valF:",valF)
					self.check.clear()
					for i in range(2,len(valF),4):
						self.check.append(valF[i].replace('N=',''))

					print("chek2:",self.check)
					self.btnCheckBox()
				except:
					self.listWidget.clear()
			else:
				self.listWidget.clear()

			if self.data2 != None and self.data2 != 'N=':
				print("no se encuentra")
				self.flagOutL = True
				self.listWidget.clear()
			else:
				print("data2 esta vacio")

	def btnCheckBox(self):
		self.listWidget.clear()
		for i in range(len(self.check)):
			item = QtWidgets.QListWidgetItem(self.check[i])
			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
			item.setCheckState(QtCore.Qt.Checked)
			self.listWidget.addItem(item)

	def on_cb_textPrograms(self):
		files=self.ls2("/Users/cex/Documents/github/DitsaNetApp/ProfileEditorPrograms/")
		for file in files:
			nf = file.replace('.txt','')
			self.textPrograms.addItem(nf)

	def ls2(self,path): 
		return [obj.name for obj in scandir(path) if obj.is_file()]


	def on_clicked_textPrograms(self):
		nameFile = self.textPrograms.currentText()
		print("nameFile:",nameFile)
		openFile = nameFile+".txt"
		archivo_texto = open("/Users/cex/Documents/github/DitsaNetApp/ProfileEditorPrograms/"+openFile,"r")
		self.programJson = archivo_texto.read()
		archivo_texto.close()
		print(self.programJson)

	def on_bttnDoneClicked(self):
		self.on_clicked_textPrograms()

		print("espera que se carguen todos los programas...")
		##realizar un len de cuantos dispositivos seran ejecutados
		

		#for i in range(len()):
		#	print("valueAddr:",i)
			#BCmb.writeProgramClient(useHostname,i,self.programJson)
		#print(self.programJson)

	def on_bttnCancelClicked(self):
		self.close()
		#cambiar este widget estructuralo mejor


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