# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formmodule.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormModule(QtWidgets.QWidget):
	def __init__(self,parent=None):
		super(Ui_FormModule, self).__init__()
		self.parent = parent
		#def setupUi(self, FormModule):
		self.setObjectName("FormModule")
		self.resize(139, 59)
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(0, 0,140,30))
		font = QtGui.QFont()
		font.setFamily("Ubuntu Light")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setStyleSheet("QLabel { background-color : lightblue; color : black;  border: 1px solid black; }")
		self.label.setFrameShape(QtWidgets.QFrame.Box)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.pbProgram = QtWidgets.QProgressBar(self)
		self.pbProgram.setGeometry(QtCore.QRect(0,30,140,20))
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
		self.pbProgram.setProperty("value", 20)
		self.pbProgram.setObjectName("pbProgram")

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, FormModule):
		_translate = QtCore.QCoreApplication.translate
		FormModule.setWindowTitle(_translate("FormModule", "Form"))
		self.label.setText(_translate("FormModule", "Voltaje:12.6V"))
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

	def showEvent(self,event):
		print("showEFM")

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	FormModule = QtWidgets.QWidget()
	ui = Ui_FormModule()
	ui.setupUi(FormModule)
	FormModule.show()
	sys.exit(app.exec_())
'''