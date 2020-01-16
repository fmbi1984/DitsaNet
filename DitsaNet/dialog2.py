# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 230, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(160, 10, 81, 31))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Dialog2)
        self.spinBox.setGeometry(QtCore.QRect(60, 50, 281, 26))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 61, 41))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog2)
        self.textEdit.setGeometry(QtCore.QRect(60, 130, 281, 70))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog"))
        self.pushButton.setText(_translate("Dialog2", "Cancelar"))
        self.pushButton_2.setText(_translate("Dialog2", "Cargar"))
        self.label.setText(_translate("Dialog2", "Programas"))
        self.label_2.setText(_translate("Dialog2", "Equipos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())
