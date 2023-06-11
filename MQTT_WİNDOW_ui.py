# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MQTT_WİNDOW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(723, 417)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 701, 401))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.conect_btn = QPushButton(self.frame)
        self.conect_btn.setObjectName(u"conect_btn")
        self.conect_btn.setGeometry(QRect(540, 10, 161, 71))
        self.conect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_btn = QPushButton(self.frame)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setGeometry(QRect(540, 90, 161, 71))
        self.send_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 200, 501, 161))
        self.label.setStyleSheet(u"\n"
"background-color: rgb(191, 191, 191);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(32, 11, 491, 161))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MQTT_V1", None))
        self.conect_btn.setText(QCoreApplication.translate("MainWindow", u"BA\u011eLAN", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"G\u00d6NDER", None))
        self.label.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"dfdf", None))
    # retranslateUi

