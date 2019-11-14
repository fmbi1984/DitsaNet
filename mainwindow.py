# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from datalistener import DataListener
#from datalistenerserver import DataListenerServer
from devicemainboard import BCmb
import shared
import time
import threading
from datetime import timedelta

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 553)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 871, 431))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(470, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel { background-color : red; color : white; border: 1px solid black; }")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(90, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(280, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(470, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pbProgram1 = QtWidgets.QProgressBar(self.tab)
        self.pbProgram1.setGeometry(QtCore.QRect(90, 170, 141, 31))
        self.pbProgram1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
        self.pbProgram1.setProperty("value", 24)
        self.pbProgram1.setObjectName("pbProgram1")
        self.pbProgram2 = QtWidgets.QProgressBar(self.tab)
        self.pbProgram2.setGeometry(QtCore.QRect(280, 170, 141, 31))
        self.pbProgram2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
        self.pbProgram2.setProperty("value", 24)
        self.pbProgram2.setObjectName("pbProgram2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
        self.progressBar_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.cmdDisplay1 = QtWidgets.QPushButton(self.tab)
        self.cmdDisplay1.setGeometry(QtCore.QRect(90, 140, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdDisplay1.setFont(font)
        self.cmdDisplay1.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdDisplay1.setFlat(True)
        self.cmdDisplay1.setObjectName("cmdDisplay1")
        self.cmdIniciar1 = QtWidgets.QPushButton(self.tab)
        self.cmdIniciar1.setGeometry(QtCore.QRect(750, 290, 91, 32))
        self.cmdIniciar1.setObjectName("cmdIniciar1")
        self.cmdPausar1 = QtWidgets.QPushButton(self.tab)
        self.cmdPausar1.setGeometry(QtCore.QRect(750, 320, 91, 32))
        self.cmdPausar1.setObjectName("cmdPausar1")
        self.cmdDetener1 = QtWidgets.QPushButton(self.tab)
        self.cmdDetener1.setGeometry(QtCore.QRect(750, 350, 91, 32))
        self.cmdDetener1.setObjectName("cmdDetener1")
        self.cmdDisplay2 = QtWidgets.QPushButton(self.tab)
        self.cmdDisplay2.setGeometry(QtCore.QRect(280, 140, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cmdDisplay2.setFont(font)
        self.cmdDisplay2.setStyleSheet("QPushButton { background-color : yellow; color : black; border: 1px solid black; }")
        self.cmdDisplay2.setFlat(True)
        self.cmdDisplay2.setObjectName("cmdDisplay2")
        self.txtProgram = QtWidgets.QTextEdit(self.tab)
        self.txtProgram.setGeometry(QtCore.QRect(210, 360, 341, 21))
        self.txtProgram.setObjectName("txtProgram")
        self.cmdProgram1 = QtWidgets.QPushButton(self.tab)
        self.cmdProgram1.setGeometry(QtCore.QRect(560, 350, 141, 32))
        self.cmdProgram1.setObjectName("cmdProgram1")
        self.check1 = QtWidgets.QCheckBox(self.tab)
        self.check1.setGeometry(QtCore.QRect(70, 120, 86, 20))
        self.check1.setText("")
        self.check1.setObjectName("check1")
        self.check2 = QtWidgets.QCheckBox(self.tab)
        self.check2.setGeometry(QtCore.QRect(260, 120, 86, 20))
        self.check2.setText("")
        self.check2.setObjectName("check2")
        self.cmdGroup = QtWidgets.QPushButton(self.tab)
        self.cmdGroup.setGeometry(QtCore.QRect(750, 260, 91, 32))
        self.cmdGroup.setObjectName("cmdGroup")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.cmdIniciarActualizar = QtWidgets.QPushButton(self.centralWidget)
        self.cmdIniciarActualizar.setGeometry(QtCore.QRect(600, 10, 141, 32))
        self.cmdIniciarActualizar.setObjectName("cmdIniciarActualizar")
        self.cmdDetenerActualizar = QtWidgets.QPushButton(self.centralWidget)
        self.cmdDetenerActualizar.setGeometry(QtCore.QRect(750, 10, 141, 32))
        self.cmdDetenerActualizar.setObjectName("cmdDetenerActualizar")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 902, 22))
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
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
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

        
        self.cmdIniciar1.clicked.connect(self.on_cmdIniciar1_clicked)

        self.cmdPausar1.clicked.connect(self.on_cmdPausar1_clicked)

        self.cmdDetener1.clicked.connect(self.on_cmdDetener1_clicked)

        self.cmdDisplay1.clicked.connect(self.on_cmdDisplay1_clicked)

        self.cmdIniciarActualizar.clicked.connect(self.on_cmdIniciarActualizar_clicked)
        self.cmdDetenerActualizar.clicked.connect(self.on_cmdDetenerActualizar_clicked)

        self.cmdGroup.clicked.connect(self.on_cmdGroup_clicked)

        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pantalla de Formación"))
        self.label.setText(_translate("MainWindow", "Mesa 1"))
        self.label_4.setToolTip(_translate("MainWindow", "Thisis a tooltip"))
        self.label_4.setText(_translate("MainWindow", "Falla"))
        self.label_8.setText(_translate("MainWindow", "MF1"))
        self.label_9.setText(_translate("MainWindow", "MF2"))
        self.label_10.setText(_translate("MainWindow", "MF3"))
        self.pbProgram1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
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
        self.cmdDisplay1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
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
        self.cmdDisplay1.setText(_translate("MainWindow", "Voltage: 12.6V"))
        self.cmdIniciar1.setText(_translate("MainWindow", "Iniciar"))
        self.cmdPausar1.setText(_translate("MainWindow", "Pausar"))
        self.cmdDetener1.setText(_translate("MainWindow", "Detener"))
        self.cmdDisplay2.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
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
        self.cmdDisplay2.setText(_translate("MainWindow", "Apagar"))
        self.cmdProgram1.setText(_translate("MainWindow", "Cargar Programa"))
        self.cmdGroup.setText(_translate("MainWindow", "Selecionar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mesa 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mesa 2"))
        self.cmdIniciarActualizar.setText(_translate("MainWindow", "Iniciar Actualizar"))
        self.cmdDetenerActualizar.setText(_translate("MainWindow", "Detener Actualizar"))
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

    def unitializeCheckbox(self):
        self.check1.setVisible(False)
        self.check1.setCheckState(QtCore.Qt.Unchecked)

        self.check2.setVisible(False)
        self.check2.setCheckState(QtCore.Qt.Unchecked)

    def initializeCheckbox(self):
        self.check1.setVisible(True)
        self.check1.setCheckState(QtCore.Qt.Unchecked)

        self.check2.setVisible(True)
        self.check2.setCheckState(QtCore.Qt.Unchecked)

    def showEvent(self, event):
        print("show")
        self.display()

        self.unitializeCheckbox()

        self.fillWithSettings()


    def on_cmdGroup_clicked(self):  
        self.initializeCheckbox()
    
    def closeEvent(self, event):
        print("close")

    def on_cmdIniciar1_clicked(self):
        print("Iniciar")
        if self.check1.checkState == QtCore.Qt.Checked:
            print("hola")
            #BCmb.runClient('ditsa-Lenovo-C20-00.local', 1)
        if self.check2.checkState == QtCore.Qt.Checked:
            BCmb.runClient('ditsa-Lenovo-C20-00.local', 2)
    
    def on_cmdIniciar2_clicked(self):
        print("Iniciar")
        if self.check1.checkState == QtCore.Qt.Checked:
            print("hola")
            #BCmb.runClient('ditsa-Lenovo-C20-00.local', 1)
        if self.check2.checkState == QtCore.Qt.Checked:
            BCmb.runClient('ditsa-Lenovo-C20-00.local', 2)
    

    def on_cmdPausar1_clicked(self):
        print("Pausar")
        if self.check1.checkState == QtCore.Qt.Checked:
            BCmb.pauseClient('ditsa-Lenovo-C20-00.local', 1)
        if self.check2.checkState == QtCore.Qt.Checked:
            BCmb.pauseClient('ditsa-Lenovo-C20-00.local', 2)
    

    def on_cmdDetener1_clicked(self):
        print("Detener")
        #if self.check1.checkState == QtCore.Qt.Checked:
        BCmb.stopClient('ditsa-Lenovo-C20-00.local', 1)
        #if self.check2.checkState == QtCore.Qt.Checked:
        BCmb.stopClient('ditsa-Lenovo-C20-00.local', 2)
    


    WAIT_SECONDS = 1

    def display(self):
        print(time.ctime())
        
        if shared.DEV[1][0] == True:
            newstr1 = ""
            if self.stateDisplay1 == 1:
                #current
                newstr1 = str(shared.DEV[1][1])+" A"
            if self.stateDisplay1 == 2:
                #voltage
                newstr1 = str(shared.DEV[1][2]) + " V"
            if self.stateDisplay1 == 3:
                #temperature
                newstr1 = str(shared.DEV[1][3]) + " °C"
            self.cmdDisplay1.setText(str(newstr1))

        

        if shared.DEV[2][0] == True:
            newstr2 = ""
            if self.stateDisplay2 == 1:
                #current
                newstr2 = str(shared.DEV[2][1])+" A"
            if self.stateDisplay2 == 2:
                #voltage
                newstr2 = str(shared.DEV[2][2]) + " V"
            if self.stateDisplay2 == 3:
                #temperature
                newstr2 = str(shared.DEV[2][3])+ " °C"
            self.cmdDisplay2.setText(str(newstr2))

        threading.Timer(self.WAIT_SECONDS, self.display).start()
        
        
    

    stateDisplay1 = 1
    def on_cmdDisplay1_clicked(self):
        print("Display 1")
        self.stateDisplay1 = self.stateDisplay1 + 1
        if self.stateDisplay1==4 :
            self.stateDisplay1 = 1
        print(self.stateDisplay1)


    stateDisplay2 = 1
    def on_cmdDisplay2_clicked(self):
        print("Display 2")
        self.stateDisplay2 = self.stateDisplay2 + 1
        if self.stateDisplay2==4 :
            self.stateDisplay2 = 1
        print(self.stateDisplay2)

    def testsCallback(self, msg):

        address = 1
        if "DL["+str(address)+"]" in msg:
            msg = msg.replace("DL["+str(address)+"]:","")

            #self.cmdDisplay1.setText(str(newstr1))
            self.cmdDisplay1.repaint()
            self.cmdDisplay1.update()
            self.cmdDisplay1.setUpdatesEnabled(True)
            
            #self.cmdDisplay2.setText(str(newstr2))
            self.cmdDisplay2.repaint()
            self.cmdDisplay2.update()
            self.cmdDisplay2.setUpdatesEnabled(True)
        '''

            newstr = msg
            print (newstr)


            self.cmdDisplay1.setText(str(newstr))
            self.cmdDisplay1.repaint()
            self.cmdDisplay1.update()
            self.cmdDisplay1.setUpdatesEnabled(True)
        '''

    def on_cmdIniciarActualizar_clicked(self):
        print("Iniciar Actualizar")
        #self.dataThread = DataListener(self.testsCallback)
        self.dataThread = DataListener(self.testsCallback)
        self.dataThread.start()

    def on_cmdDetenerActualizar_clicked(self):
        print("Detener Actualizar")
        self.dataThread.stop()


    def pingForDevicesPresent(self):
        # we do ping to the devices 
        devStart = 1
        devStop = 2
        for i in range(devStart, devStop+1):
            address=i
            print("Doing ping to device No."+str(address))
            readData = BCmb.pingClient('ditsa-Lenovo-C20-00.local', address)
            print("VALUE:")
            print(str(readData))
            shared.DEV[i][0] = False
            if readData!= None:
                if readData == True:
                    shared.DEV[i][0] = True
                    print("DEV"+str(address)+" is Present!")  
                else:
                    print("DEV"+str(address)+" is not Present!")
            else:
                print("DEV"+str(address)+" is not Present!")

    def fillWithSettings(self):
        for i in range(1, 9):

            print(shared.DEV[0][8])

            myName = self.MainWindow.findChild(QtWidgets.QLabel, "label")
            myName.setText("Viri")

            myName = self.MainWindow.findChild(QtWidgets.QLabel, "label_8")
            myName.setText("Viri")

            #myDisplay = self.MainWindow.findChild(QtWidgets.QPushButton, "cmdDisplay1")
            #myDisplay.setText("Page 34")

            myProgress = self.MainWindow.findChild(QtWidgets.QProgressBar, "pbProgram1")
            #myProgress.setValue(10)

            myTab = self.MainWindow.findChild(QtWidgets.QWidget, "tab_2")
            self.tabWidget.setTabText(self.tabWidget.indexOf(myTab), "Mesa 2")

            #self.set

            print("Page "+str(i))
        for i in range(0,28):
            print("Name "+str(i))
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

