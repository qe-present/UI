# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloi.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 313)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 60, 301, 161))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "hello world"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#220eff;\">hello world</span></p></body></html>"))
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    ui_form=Ui_Form()
    ui_form.setupUi(w)
    w.show()
    app.exec_()