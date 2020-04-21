# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_copy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from form import Ui_Form


class Ui_MainWindow(object):
	def __init__(self,MainWindow, parent=None):
	#def setupUi(self, MainWindow):
		object.__init__(parent)

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1476, 523)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
		self.gridLayout.setContentsMargins(11, 11, 11, 11)
		self.gridLayout.setSpacing(6)
		self.gridLayout.setObjectName("gridLayout")
		self.cmdIniciar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdIniciar.setObjectName("cmdIniciar")
		self.gridLayout.addWidget(self.cmdIniciar, 0, 1, 1, 1)
		self.comboBox = QtWidgets.QComboBox(self.centralWidget)
		self.comboBox.setObjectName("comboBox")
		self.gridLayout.addWidget(self.comboBox, 0, 4, 1, 1)
		self.cmdCargar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdCargar.setObjectName("cmdCargar")
		self.gridLayout.addWidget(self.cmdCargar, 0, 0, 1, 1)
		self.spinBox = QtWidgets.QSpinBox(self.centralWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
		self.spinBox.setSizePolicy(sizePolicy)
		self.spinBox.setObjectName("spinBox")
		self.gridLayout.addWidget(self.spinBox, 0, 5, 1, 1)
		self.cmdDetener = QtWidgets.QPushButton(self.centralWidget)
		self.cmdDetener.setObjectName("cmdDetener")
		self.gridLayout.addWidget(self.cmdDetener, 0, 3, 1, 1)
		self.cmdPausar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdPausar.setObjectName("cmdPausar")
		self.gridLayout.addWidget(self.cmdPausar, 0, 2, 1, 1)
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
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
		self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
		self.gridLayout_2.setSpacing(6)
		self.gridLayout_2.setObjectName("gridLayout_2")
		#self.tabWidget.addTab(self.tab, "")
		form = Ui_Form(self)
		#self.tab_2 = QtWidgets.QWidget()
		#self.tab_2.setObjectName("tab_2")
		#self.tabWidget.addTab(self.tab_2, "")
		self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 6)
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

		self.comboBox.addItems(['Current','Voltage','Temperature','Time left','Step','Address'])
		
		MainWindow.showEvent = self.showEvent
		MainWindow.closeEvent = self.closeEvent
		

		self.mylist = list()
		self.mylabel = list()
		self.rowCol = list()

		self.Tabs = list()
		self.maxTabs = list()

		self.MainWindow = MainWindow

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Formation Viewer"))
		self.cmdIniciar.setText(_translate("MainWindow", "Start"))
		self.cmdCargar.setText(_translate("MainWindow", "Load Programs"))
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
		settings = QtCore.QSettings('/Users/cex/Documents/github/DitsaNetEditorApp/Settings/archivo.ini', QtCore.QSettings.NativeFormat)
		if settings.value('/Users/cex/Documents/github/DitsaNetEditorApp/Settings/archivo.ini')!='':
			self.settingsList = settings.value("mylist")
			self.settingsLabel = settings.value("mylabel")
			self.settingsRowCol = settings.value("rowcol")

			if self.settingsRowCol != None and len(self.settingsRowCol) !=0:
				self.rowCol = self.settingsRowCol[:]
			else:
				self.rowCol.append('1%')
				self.rowCol.append('R=10 C=10')

			if self.settingsList != None:
				self.mylist = self.settingsList[:] #para que no se corresponden con el mismo objeto

			if self.settingsLabel != None:
				self.mylabel = self.settingsLabel[:] #para que no se corresponden con el mismo objeto

			if self.settingsList != None or self.settingsLabel != None:
				self.populateTabs()

				form = Ui_Form(self)
				self.tabWidget.addTab(form, "Page 1")
				tabC = self.tabWidget.count()
				#print("tabC:",tabC)

				if (self.settingsList != None  and len(self.settingsList)!=0) or (self.settingsLabel != None and len(self.settingsLabel)!=0):
					for i in range(int(self.numTabT)-tabC):
						#print("i",i)
						self.newPage()

	def closeEvent(self,event):
		print("closeEvent")

	def populateTabs(self):
		print("populateTabs")
		for i in range(0,len(self.settingsList),4):
			self.maxTabs.append(self.settingsList[i])

		for i in range(0,len(self.settingsLabel),3):
			self.maxTabs.append(self.settingsLabel[i])

		if len(self.maxTabs)!= 0:
			#print("max")
			y = max(self.maxTabs)
			self.numTabT = y.replace('%','')
			#print(self.numTabT)
			self.maxTabs.clear()

	def newPage(self): 
		print("newPage")
		form = Ui_Form(self)
		self.tabWidget.addTab(form,"Page "+str(self.tabWidget.count()+1))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow(MainWindow)
	#ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
