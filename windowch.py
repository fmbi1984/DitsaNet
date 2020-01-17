# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowCh(object):
    def setupUi(self, WindowCh):
        WindowCh.setObjectName("WindowCh")
        WindowCh.resize(400, 300)
        self.BttnCancel = QtWidgets.QPushButton(WindowCh)
        self.BttnCancel.setGeometry(QtCore.QRect(90, 240, 89, 25))
        self.BttnCancel.setObjectName("BttnCancel")
        self.BttnDone = QtWidgets.QPushButton(WindowCh)
        self.BttnDone.setGeometry(QtCore.QRect(220, 240, 89, 25))
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
        self.lineEdit = QtWidgets.QLineEdit(WindowCh)
        self.lineEdit.setGeometry(QtCore.QRect(80, 140, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(WindowCh)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 140, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(WindowCh)
        QtCore.QMetaObject.connectSlotsByName(WindowCh)

    def retranslateUi(self, WindowCh):
        _translate = QtCore.QCoreApplication.translate
        WindowCh.setWindowTitle(_translate("WindowCh", "Programas"))
        self.BttnCancel.setText(_translate("WindowCh", "Cancelar"))
        self.BttnDone.setText(_translate("WindowCh", "Hecho"))
        self.lblPrograms.setText(_translate("WindowCh", "Programas"))
        self.lblModules.setText(_translate("WindowCh", "Seleccion de Módulos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowCh = QtWidgets.QDialog()
    ui = Ui_WindowCh()
    ui.setupUi(WindowCh)
    WindowCh.show()
    sys.exit(app.exec_())
