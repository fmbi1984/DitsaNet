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

		MainWindow.showEvent = self.showEvent
		MainWindow.closeEvent = self.closeEvent

		self.mylist = list()
		self.mylabel = list()
		self.rowCol = list()

		self.Tabs = list()
		self.maxTabs = list()

		self.newList = list()
		self.newLabel = list()

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

			print("settingslist:",self.settingsList)
			if self.settingsList !=None:
				self.currentList()

			if self.settingsLabel != None:
				self.currentLabel()

			if self.settingsRowCol != None and len(self.settingsRowCol) !=0:
				self.rowCol = self.settingsRowCol[:]
			else:
				self.rowCol.append('1%')
				self.rowCol.append('R=10 C=10')

			if self.settingsList != None:
				self.mylist = self.newList[:] #para que no se corresponden con el mismo objeto
				self.newList.clear()

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

	def currentList(self):
		for i in range(0,len(self.settingsList),4):
			if self.settingsList[i] not in self.Tabs:
				self.Tabs.append(self.settingsList[i])
		
		print("tb:",self.Tabs)
		minCoord = []
		comp1 = []
		comp2 = []
		compxy = []
		for j in range(len(self.Tabs)):
			for i in range(0,len(self.settingsList),4):
				if self.settingsList[i] == self.Tabs[j]:
					minCoord.append(self.settingsList[i])
					minCoord.append(self.settingsList[i+1])
					minCoord.append(self.settingsList[i+2])
					minCoord.append(self.settingsList[i+3])
			t = 0
			x = int(len(minCoord)/4)
			while t<x:
				t += 1
				for i in range(1,len(minCoord),4):
					tmp = minCoord[i].split()
					for i in range(2):
						if i == 0:
							y = tmp[0].partition('X=')
							coordx = y[2]
							comp1.append(int(coordx))
						else:
							y = tmp[1].partition('Y=')
							coordy = y[2]
							comp2.append(int(coordy))

				print("comp1:",comp1)
				print("comp2:",comp2)

				for k in range(len(comp1)):
					comp = str(comp1[k]) + str(comp2[k])
					compxy.append(int(comp))
				print("compxy:",compxy)

				compT = min(compxy)
				print("compT:",compT)

				for n in range(len(comp1)):
					if str(compT) == str(comp1[n])+str(comp2[n]):
						val1 = str(comp1[n])
						val2 = str(comp2[n])

						for r in range(1,len(self.newList),4):
							if self.newList[r] == "X="+str(comp1[n])+" Y="+str(comp2[n]):
								for i in range(1,len(minCoord),4):
									if minCoord[i] == "X="+val1+" Y="+val2:
										minCoord.append(minCoord[i-1])
										minCoord.append("X="+str(comp1[n]+1)+" Y="+str(comp2[n]))
										minCoord.append(minCoord[i+1])
										minCoord.append(minCoord[i+2])
										minCoord.pop(i+2)
										minCoord.pop(i+1)
										minCoord.pop(i)
										minCoord.pop(i-1)
										val1 = str(comp1[n]+1)
										val2 = str(comp2[n])
										break
						
						#print("miCrd:",minCoord)
						self.newList.append(self.Tabs[j])
						self.newList.append("X="+str(int(val1)+1)+" Y="+ str(comp2[n]))
						self.newList.append("Progress")
						self.newList.append("Bar")

						for h in range(1,len(minCoord),4):
							if minCoord[h] == "X="+val1+" Y="+val2:
								self.newList.append(minCoord[h-1])
								self.newList.append(minCoord[h])
								self.newList.append(minCoord[h+1])
								self.newList.append(minCoord[h+2])
						break
				#print("newList:",self.newList)
				for m in range(1,len(minCoord),4):
					if minCoord[m] == "X="+val1+" Y="+val2:
						minCoord.pop(m+2)
						minCoord.pop(m+1)
						minCoord.pop(m)
						minCoord.pop(m-1)
						comp1.clear()
						comp2.clear()
						compxy.clear()
						break
				print("self.newList:",self.newList)

	def currentLabel(self):
		print("pass")
		
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow(MainWindow)
	#ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
