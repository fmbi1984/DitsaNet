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

class Ui_WindowCh(object):
	def setupUi(self, WindowCh):
		WindowCh.setObjectName("WindowCh")
		WindowCh.resize(400, 300)
		self.BttnCancel = QtWidgets.QPushButton(WindowCh)
		self.BttnCancel.setGeometry(QtCore.QRect(110, 240, 80, 25))
		self.BttnCancel.setObjectName("BttnCancel")
		self.BttnDone = QtWidgets.QPushButton(WindowCh)
		self.BttnDone.setGeometry(QtCore.QRect(220, 240, 80, 25))
		self.BttnDone.setObjectName("BttnDone")
		self.textPrograms = QtWidgets.QComboBox(WindowCh)
		self.textPrograms.setGeometry(QtCore.QRect(50, 60, 301, 25))
		self.textPrograms.setObjectName("textPrograms")
		self.lblPrograms = QtWidgets.QLabel(WindowCh)
		self.lblPrograms.setGeometry(QtCore.QRect(160, 16, 81, 31))
		self.lblPrograms.setObjectName("lblPrograms")
		self.lblModules = QtWidgets.QLabel(WindowCh)
		self.lblModules.setGeometry(QtCore.QRect(130, 110, 151, 21))
		self.lblModules.setObjectName("lblModules")
		self.widget = QtWidgets.QWidget(WindowCh)
		self.widget.setGeometry(QtCore.QRect(80, 160, 251, 27))
		self.widget.setObjectName("widget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.lineEdit = QtWidgets.QLineEdit(self.widget)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout.addWidget(self.lineEdit)
		self.label = QtWidgets.QLabel(self.widget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.horizontalLayout.addWidget(self.lineEdit_2)

		self.retranslateUi(WindowCh)
		QtCore.QMetaObject.connectSlotsByName(WindowCh)

	def retranslateUi(self, WindowCh):
		_translate = QtCore.QCoreApplication.translate
		WindowCh.setWindowTitle(_translate("WindowCh", "Programas"))
		self.BttnCancel.setText(_translate("WindowCh", "Cancelar"))
		self.BttnDone.setText(_translate("WindowCh", "Hecho"))
		self.lblPrograms.setText(_translate("WindowCh", "Programas"))
		self.lblModules.setText(_translate("WindowCh", "Selección de Módulos"))
		self.label.setText(_translate("WindowCh", "-"))


		#self.sBoxMin.setRange(1,28)
		#self.sBoxMax.setValue(2)

		self.BttnDone.clicked.connect(self.on_bttnDoneClicked)
		self.BttnCancel.clicked.connect(self.on_bttnCancelClicked)
		#self.sBoxMin.valueChanged.connect(self.spinBMn_valueChanged)
		#self.sBoxMax.valueChanged.connect(self.spinBMx_valueChanged)
		self.on_cb_textPrograms()

	def on_cb_textPrograms(self):
		files=self.ls2("/Users/cex/Documents/github/DitsaNetApp/FormationDataFiles/")
		for file in files:
			nf = file.replace('.txt','')
			self.textPrograms.addItem(nf)

	def ls2(self,path): 
		return [obj.name for obj in scandir(path) if obj.is_file()]

	lastV = 0
	#def spinBMn_valueChanged(self):
		#self.firtsV = self.sBoxMin.value()
		#self.sBoxMax.setValue(self.sBoxMin.value()+1)
		#self.sBoxMax.setMinimum(self.sBoxMax.value())
		#if self.lastV > self.firtsV:
			#self.spinBMx_valueChanged()
			#self.sBoxMax.setValue(self.sBoxMin.value()+1)
		#self.lastV = self.firtsV
		#print("valor final:",self.lastV)

	#def spinBMx_valueChanged(self):
		#self.sBoxMax.setRange(self.sBoxMin.value()+1,28)
		

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
		#for i in range(self.sBoxMin.value(),self.sBoxMax.value()+1):
			#print("value_i:",i)
			#BCmb.writeProgramClient(useHostname,i,self.programJson)
		#print(self.programJson)

	def on_bttnCancelClicked(self):
		WindowCh.close()
		#msg = QtWidgets.QMessageBox()
		#msg.about(QtWidgets.QWidget,'Warnig','programa cerrado')

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	WindowCh = QtWidgets.QDialog()
	ui = Ui_WindowCh()
	ui.setupUi(WindowCh)
	WindowCh.show()
	sys.exit(app.exec_())
