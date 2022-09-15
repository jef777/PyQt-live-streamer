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
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(2200, 1300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/jeff/Desktop/streamer/img/plhlder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(0, 0))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stream_section = QtWidgets.QLabel(self.centralwidget)
        self.stream_section.setGeometry(QtCore.QRect(240, 0, 971, 671))
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
        self.controls_section = QtWidgets.QFrame(self.centralwidget)
        self.controls_section.setGeometry(QtCore.QRect(-10, 0, 231, 801))
        self.controls_section.setStyleSheet("QFrame#controls_section {\n"
"background-color: qlineargradient(spread:pad,y1:0, x1:0, y1:0, x1:1, stop:0 rgb(255, 255, 255, 1), stop:1 rgba(40, 183, 209));\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}")
        self.controls_section.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controls_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controls_section.setObjectName("controls_section")
        self.circularProgressBar_Main_3 = QtWidgets.QFrame(self.controls_section)
        self.circularProgressBar_Main_3.setGeometry(QtCore.QRect(0, 410, 240, 240))
        self.circularProgressBar_Main_3.setStyleSheet("background-color: none;")
        self.circularProgressBar_Main_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_Main_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_Main_3.setObjectName("circularProgressBar_Main_3")
        self.circularProgressRAM = QtWidgets.QFrame(self.circularProgressBar_Main_3)
        self.circularProgressRAM.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularProgressRAM.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(255, 0, 127, 255), stop:0.745 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressRAM.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressRAM.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressRAM.setObjectName("circularProgressRAM")
        self.circularBg_3 = QtWidgets.QFrame(self.circularProgressBar_Main_3)
        self.circularBg_3.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg_3.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_3.setObjectName("circularBg_3")
        self.circularContainer_3 = QtWidgets.QFrame(self.circularBg_3)
        self.circularContainer_3.setGeometry(QtCore.QRect(14, 16, 190, 190))
        self.circularContainer_3.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_3.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_3.setObjectName("circularContainer_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.circularContainer_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 30, 191, 137))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.infoLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_3.setObjectName("infoLayout_3")
        self.labelAplicationName_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(10)
        self.labelAplicationName_3.setFont(font)
        self.labelAplicationName_3.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName_3.setObjectName("labelAplicationName_3")
        self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)
        self.labelCredits_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(8)
        self.labelCredits_3.setFont(font)
        self.labelCredits_3.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits_3.setObjectName("labelCredits_3")
        self.infoLayout_3.addWidget(self.labelCredits_3, 3, 0, 1, 1)
        self.labelPercentageRAM = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(30)
        self.labelPercentageRAM.setFont(font)
        self.labelPercentageRAM.setStyleSheet("color: rgb(255, 44, 174); padding: 0px; background-color: none;")
        self.labelPercentageRAM.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageRAM.setIndent(-1)
        self.labelPercentageRAM.setObjectName("labelPercentageRAM")
        self.infoLayout_3.addWidget(self.labelPercentageRAM, 1, 0, 1, 1)
        self.circularProgressBar_Main = QtWidgets.QFrame(self.controls_section)
        self.circularProgressBar_Main.setGeometry(QtCore.QRect(0, 130, 240, 240))
        self.circularProgressBar_Main.setStyleSheet("background-color: none;")
        self.circularProgressBar_Main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_Main.setObjectName("circularProgressBar_Main")
        self.circularProgressCPU = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularProgressCPU.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularProgressCPU.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressCPU.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressCPU.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressCPU.setObjectName("circularProgressCPU")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.circularContainer = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularContainer.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer.setObjectName("circularContainer")
        self.layoutWidget = QtWidgets.QWidget(self.circularContainer)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 40, 191, 137))
        self.layoutWidget.setObjectName("layoutWidget")
        self.infoLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.labelAplicationName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(10)
        self.labelAplicationName.setFont(font)
        self.labelAplicationName.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName.setObjectName("labelAplicationName")
        self.infoLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)
        self.labelPercentageCPU = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(30)
        self.labelPercentageCPU.setFont(font)
        self.labelPercentageCPU.setStyleSheet("color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageCPU.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCPU.setIndent(-1)
        self.labelPercentageCPU.setObjectName("labelPercentageCPU")
        self.infoLayout.addWidget(self.labelPercentageCPU, 1, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(8)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.infoLayout.addWidget(self.labelCredits, 2, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgressCPU.raise_()
        self.circularContainer.raise_()
        self.label_2 = QtWidgets.QLabel(self.controls_section)
        self.label_2.setGeometry(QtCore.QRect(0, 760, 161, 20))
        self.label_2.setStyleSheet("background-color: none;\n"
"color: rgb(58, 58, 102);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.controls_section)
        self.label.setGeometry(QtCore.QRect(0, 740, 161, 20))
        self.label.setStyleSheet("background-color: none;\n"
"color: rgb(58, 58, 102);\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.controls_section_2 = QtWidgets.QFrame(self.centralwidget)
        self.controls_section_2.setGeometry(QtCore.QRect(230, 680, 991, 121))
        self.controls_section_2.setMinimumSize(QtCore.QSize(0, 0))
        self.controls_section_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.controls_section_2.setStyleSheet("QFrame#controls_section_2 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255, 1), stop:1 rgba(40, 183, 209));\n"
"}")
        self.controls_section_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.controls_section_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.controls_section_2.setMidLineWidth(0)
        self.controls_section_2.setObjectName("controls_section_2")
        self.start_btn = QtWidgets.QPushButton(self.controls_section_2)
        self.start_btn.setGeometry(QtCore.QRect(300, 10, 101, 101))
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
        self.start_btn.setIconSize(QtCore.QSize(100, 100))
        self.start_btn.setCheckable(False)
        self.start_btn.setChecked(False)
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.controls_section_2)
        self.stop_btn.setGeometry(QtCore.QRect(510, 10, 101, 101))
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
        self.stop_btn.setIconSize(QtCore.QSize(100, 100))
        self.stop_btn.setCheckable(False)
        self.stop_btn.setChecked(False)
        self.stop_btn.setObjectName("stop_btn")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(1050, 10, 140, 31))
        self.progressBar_2.setMinimumSize(QtCore.QSize(140, 0))
        self.progressBar_2.setMaximumSize(QtCore.QSize(140, 16777215))
        self.progressBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(58, 58, 102, 120);\n"
"    border-style: none;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    color: #fff;\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: rgb(115, 210, 22);\n"
"    border-radius: 4px;\n"
"    width: 25px;\n"
"    margin: 2px;\n"
"}")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 50)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 9, 291, 51))
        self.frame.setStyleSheet("border: none;\n"
"background: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_3.setStyleSheet("font-size: 34px;\n"
"font-weight: bold;\n"
"color: rgb(39, 192, 221, 70);\n"
"background: none;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(73, 9, 191, 31))
        self.label_4.setStyleSheet("font-size: 40px;\n"
"font-weight: bold;\n"
"color: rgb(39, 192, 221, 40);\n"
"background: none;\n"
"")
        self.label_4.setObjectName("label_4")
        self.stream_section.raise_()
        self.controls_section_2.raise_()
        self.controls_section.raise_()
        self.progressBar_2.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelAplicationName_3.setText(_translate("MainWindow", "<strong>RAM</strong> USAGE"))
        self.labelCredits_3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.labelPercentageRAM.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:50pt;\">25</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>"))
        self.labelAplicationName.setText(_translate("MainWindow", "<strong>CPU</strong> USAGE"))
        self.labelPercentageCPU.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:50pt;\">60</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>"))
        self.labelCredits.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Processor"))
        self.label.setText(_translate("MainWindow", "System"))
        self.label_3.setText(_translate("MainWindow", "Live"))
        self.label_4.setText(_translate("MainWindow", "Streamer"))
import imges_rc
import imges_rc_rc
