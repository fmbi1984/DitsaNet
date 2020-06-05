# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopmodule.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_stopModule(QtWidgets.QDialog):
	#def setupUi(self, stopModule):
	def __init__(self,parent=None):
		super(Ui_stopModule, self).__init__()
		self.parent = parent

		self.setObjectName("stopModule")
		self.resize(472, 331)
		self.buttonBox = QtWidgets.QDialogButtonBox(self)
		self.buttonBox.setGeometry(QtCore.QRect(80, 120, 161, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.listWidget = QtWidgets.QListWidget(self)
		self.listWidget.setGeometry(QtCore.QRect(331, 0, 141, 331))
		self.listWidget.setObjectName("listWidget")
		self.lineEditMin = QtWidgets.QLineEdit(self)
		self.lineEditMin.setGeometry(QtCore.QRect(60, 60, 80, 25))
		self.lineEditMin.setObjectName("lineEditMin")
		self.lineEditMax = QtWidgets.QLineEdit(self)
		self.lineEditMax.setGeometry(QtCore.QRect(180, 60, 80, 25))
		self.lineEditMax.setObjectName("lineEditMax")
		self.textEdit = QtWidgets.QTextEdit(self)
		self.textEdit.setGeometry(QtCore.QRect(0, 180, 331, 151))
		self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
		self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.textEdit.setObjectName("textEdit")
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(150, 60, 20, 25))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setGeometry(QtCore.QRect(85, 20, 150, 20))
		self.label_2.setObjectName("label_2")
		self.widget = QtWidgets.QWidget(self)
		self.widget.setGeometry(QtCore.QRect(20, 150, 311, 27))
		self.widget.setObjectName("widget")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.BtnArrowR = QtWidgets.QPushButton(self.widget)
		self.BtnArrowR.setObjectName("BtnArrowR")
		self.horizontalLayout_2.addWidget(self.BtnArrowR)

		self.retranslateUi(self)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, stopModule):
		_translate = QtCore.QCoreApplication.translate
		stopModule.setWindowTitle(_translate("stopModule", "Stop"))
		self.label.setText(_translate("stopModule", "-"))
		self.label_2.setText(_translate("stopModule", "Selection of Modules"))
		self.BtnArrowR.setText(_translate("stopModule", ">>"))

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	pauseModule = QtWidgets.QDialog()
	ui = Ui_pauseModule()
	ui.setupUi(pauseModule)
	pauseModule.show()
	sys.exit(app.exec_())
'''