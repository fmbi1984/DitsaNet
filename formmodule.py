# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formmodule.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormModule(QtWidgets.QWidget):
	#def setupUi(self, FormModule):
	def __init__(self,nameModule,cbOption,parent=None):
		super(Ui_FormModule, self).__init__()
		self.parent = parent
		self.nameModule = nameModule
		self.cbOption = cbOption

		self.setObjectName("FormModule")
		self.resize(73, 70)
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(0, 15, 74, 20))
		font = QtGui.QFont()
		font.setFamily("Ubuntu Light")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setStyleSheet("QLabel { background-color : lightblue; color : black;  border: 1px solid black; }")
		self.label.setFrameShape(QtWidgets.QFrame.Box)
		self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label.setObjectName("label")
		self.pbProgram = QtWidgets.QProgressBar(self)
		self.pbProgram.setGeometry(QtCore.QRect(0, 35, 74, 15))
		self.pbProgram.setStyleSheet("QProgressBar\n"
"{\n"
"	border: 1px solid black;\n"
"	border-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"	background-color: blue;\n"
"	width: 2.15px;\n"
"	margin: 0.5px;\n"
"}")
		self.pbProgram.setProperty("value",0)
		self.pbProgram.setObjectName("pbProgram")
		self.lblmodule = QtWidgets.QLabel(self)
		self.lblmodule.setGeometry(QtCore.QRect(0, 0, 74, 15))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.lblmodule.setFont(font)
		self.lblmodule.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.lblmodule.setStyleSheet("QLabel { background-color : white; }") #color : black;  border: 1px solid black;
		#self.label_2.setFrameShape(QtWidgets.QFrame.Box)
		self.lblmodule.setAlignment(QtCore.Qt.AlignCenter)
		self.lblmodule.setObjectName("lblmodule")

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

		#self.showEvent(self)

	def retranslateUi(self, FormModule):
		_translate = QtCore.QCoreApplication.translate
		FormModule.setWindowTitle(_translate("FormModule", "Form"))
		self.label.setText(_translate("FormModule", "00.0"))
		self.pbProgram.setToolTip(_translate("FormModule", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
		self.lblmodule.setText(_translate("FormModule", "1-01"))

	def showEvent(self,event):
		print("FormShow")
		self.lblmodule.setText(self.nameModule)

		if self.cbOption == 'Current':
			self.label.setText("0.0"+" A")

		if self.cbOption == 'Voltage':
			self.label.setText("00.0"+" V")

		if self.cbOption == 'Temperature':
			self.label.setText("0.0"+" C")

		if self.cbOption == 'Time left':
			self.label.setText("0.0"+" t")

		if self.cbOption == 'Step':
			self.label.setText("0.0"+" S")

		if self.cbOption == 'Address':
			self.label.setText("1"+" #")

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	FormModule = QtWidgets.QWidget()
	ui = Ui_FormModule()
	FormModule.show()
	sys.exit(app.exec_())
'''