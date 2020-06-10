# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadProgress.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_downloadProgress(QtWidgets.QDialog):
	#def setupUi(self, downloadProgress):
	def __init__(self,parent=None):
		super(Ui_downloadProgress, self).__init__()
		self.parent = parent

		self.setObjectName("downloadProgress")
		#downloadProgress.resize(344, 176)
		self.setFixedSize(344,176)
		self.progressBar = QtWidgets.QProgressBar(self)
		self.progressBar.setGeometry(QtCore.QRect(50, 90, 241, 31))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setObjectName("progressBar")
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(110, 50, 111, 20))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setObjectName("label")

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, downloadProgress):
		_translate = QtCore.QCoreApplication.translate
		downloadProgress.setWindowTitle(_translate("downloadProgress", "Dialog"))
		self.label.setText(_translate("downloadProgress", "Loads Program"))



'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	downloadProgress = QtWidgets.QDialog()
	ui = Ui_downloadProgress()
	ui.setupUi(downloadProgress)
	downloadProgress.show()
	sys.exit(app.exec_())
'''