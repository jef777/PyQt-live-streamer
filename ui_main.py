# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jeff/Desktop/streamer/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(2200, 1300)
        MainWindow.setMinimumSize(QtCore.QSize(2200, 1300))
        MainWindow.setMaximumSize(QtCore.QSize(2700, 1300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/jeff/Desktop/streamer/img/plhlder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(2200, 1300))
        self.centralwidget.setMaximumSize(QtCore.QSize(0, 0))
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"    background-image: url(:/images/img/bg3.jpg);\n"
"    background-repeat: no-repeat;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.media = QtWidgets.QFrame(self.centralwidget)
        self.media.setMinimumSize(QtCore.QSize(2000, 1200))
        self.media.setMaximumSize(QtCore.QSize(2000, 1200))
        self.media.setStyleSheet("QFrame#media {\n"
"     background-color: rgb(58, 45, 99, 160);\n"
"    border-radius: 15px;\n"
"}")
        self.media.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.media.setFrameShadow(QtWidgets.QFrame.Raised)
        self.media.setObjectName("media")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.media)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.media)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stream_section = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stream_section.setFont(font)
        self.stream_section.setStyleSheet("\n"
"QLabel#stream_section {\n"
"    image: url(:/images/img/plhlder.png);\n"
"    border-radius: 15px;\n"
"}")
        self.stream_section.setText("")
        self.stream_section.setAlignment(QtCore.Qt.AlignCenter)
        self.stream_section.setObjectName("stream_section")
        self.verticalLayout.addWidget(self.stream_section)
        self.horizontalLayout_2.addWidget(self.frame)
        self.controls_section = QtWidgets.QFrame(self.media)
        self.controls_section.setMinimumSize(QtCore.QSize(0, 0))
        self.controls_section.setMaximumSize(QtCore.QSize(150, 16777215))
        self.controls_section.setStyleSheet("QFrame#controls_section {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255, 1), stop:1 rgba(40, 183, 209));\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}")
        self.controls_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.controls_section.setFrameShadow(QtWidgets.QFrame.Plain)
        self.controls_section.setMidLineWidth(0)
        self.controls_section.setObjectName("controls_section")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.controls_section)
        self.verticalLayout_2.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.controls_section)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.start_btn = QtWidgets.QPushButton(self.controls_section)
        self.start_btn.setStyleSheet("QPushButton#start_btn {\n"
"    color: rgb(187, 170, 244);\n"
"    font-weight: bold;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton#start_btn:hover{\n"
"     padding: -5px;\n"
"    border-radius: 25px;\n"
"    background-color: rgb(52, 41, 86);\n"
"}\n"
"")
        self.start_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/img/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_btn.setIcon(icon1)
        self.start_btn.setIconSize(QtCore.QSize(300, 150))
        self.start_btn.setCheckable(False)
        self.start_btn.setChecked(False)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout_2.addWidget(self.start_btn)
        self.stop_btn = QtWidgets.QPushButton(self.controls_section)
        self.stop_btn.setStyleSheet("QPushButton#stop_btn {\n"
"    color: rgb(187, 170, 244);\n"
"    font-weight: bold;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton#stop_btn:hover{\n"
"     padding: -5px;\n"
"    border-radius: 25px;\n"
"    background-color: rgb(52, 41, 86);\n"
"}\n"
"")
        self.stop_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/img/stop-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_btn.setIcon(icon2)
        self.stop_btn.setIconSize(QtCore.QSize(300, 150))
        self.stop_btn.setCheckable(False)
        self.stop_btn.setChecked(False)
        self.stop_btn.setObjectName("stop_btn")
        self.verticalLayout_2.addWidget(self.stop_btn)
        self.label_2 = QtWidgets.QLabel(self.controls_section)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.controls_section)
        self.horizontalLayout_3.addWidget(self.media)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
import imges_rc
import imges_rc_rc
