# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'protyper.ui'
#
# Created: Sat Aug 13 10:37:13 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 331)
        MainWindow.setStyleSheet("")
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtGui.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 521, 331))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/images/background.png"))
        self.Background.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Background.setMargin(0)
        self.Background.setObjectName("Background")
        self.plain_text = QtGui.QPlainTextEdit(self.centralwidget)
        self.plain_text.setGeometry(QtCore.QRect(20, 340, 461, 51))
        self.plain_text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.plain_text.setStyleSheet("QPlainTextEdit{\n"
"background-color:rgba(255,255,255,150);\n"
"border:     1px solid gray; \n"
"\n"
"}")
        self.plain_text.setObjectName("plain_text")
        self.pix_key_text_3 = QtGui.QLabel(self.centralwidget)
        self.pix_key_text_3.setGeometry(QtCore.QRect(180, 80, 141, 141))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pix_key_text_3.sizePolicy().hasHeightForWidth())
        self.pix_key_text_3.setSizePolicy(sizePolicy)
        self.pix_key_text_3.setMaximumSize(QtCore.QSize(256, 256))
        self.pix_key_text_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pix_key_text_3.setText("")
        self.pix_key_text_3.setPixmap(QtGui.QPixmap(":/images/key.png"))
        self.pix_key_text_3.setScaledContents(True)
        self.pix_key_text_3.setObjectName("pix_key_text_3")
        self.pix_key_enter_3 = QtGui.QLabel(self.centralwidget)
        self.pix_key_enter_3.setGeometry(QtCore.QRect(530, 80, 141, 151))
        self.pix_key_enter_3.setMaximumSize(QtCore.QSize(256, 256))
        self.pix_key_enter_3.setText("")
        self.pix_key_enter_3.setPixmap(QtGui.QPixmap(":/images/key_enter.png"))
        self.pix_key_enter_3.setScaledContents(True)
        self.pix_key_enter_3.setObjectName("pix_key_enter_3")
        self.label_start = QtGui.QLabel(self.centralwidget)
        self.label_start.setGeometry(QtCore.QRect(150, 410, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_start.setFont(font)
        self.label_start.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.label_start.setObjectName("label_start")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_start.setText(QtGui.QApplication.translate("MainWindow", "PRESS F12 TO START", None, QtGui.QApplication.UnicodeUTF8))

import main_rc
