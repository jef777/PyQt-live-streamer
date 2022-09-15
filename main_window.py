
import sys
import platform
import psutil
# import some PyQt5 modules
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

from ui_splash_screen import *
from ui_main import *
from imges_rc import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.resize(200, 250)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_system_stats(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.start_btn.clicked.connect(self.startStream)
        self.ui.stop_btn.clicked.connect(self.stopStream)


    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        width = int(image.shape[1] * 2.5)
        height = int(image.shape[0] * 2)
        dimensions = (width, height)
        image2 = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)

        # convert image to RGB format
        image = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.stream_section.setPixmap(QPixmap.fromImage(qImg))

    def rescale_frame(image):    # works for image, video, live video
        width = int(image.shape[1] * 2)
        height = int(image.shape[0] * 2)
        dimensions = (width, height)
        return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)

    # start stream
    def startStream(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # print(self.cap)
            self.cap.set(3, 1440)
            # start timer
            self.timer.start(20)


    def stopStream(self):
        if  self.timer.isActive():
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    #CPU stats
    def init_system_stats(self, arg):
        self.cpu_percent = 0
        self.ram_percent = 0
        self.traces = dict()

        self.ui.label.setText(f"{platform.system()} {platform.machine()}")
        self.ui.label_2.setText(f"Processor: {platform.processor()}")
        self.current_timer_systemStat = QtCore.QTimer()
        self.current_timer_systemStat.timeout.connect(
        self.getsystemStatpercent)
        self.current_timer_systemStat.start(1000)


    def getsystemStatpercent(self):
        self.cpu_percent = psutil.cpu_percent()
        self.ram_percent = psutil.virtual_memory().percent
        self.setValue(self.cpu_percent, self.ui.labelPercentageCPU,
                      self.ui.circularProgressCPU, "rgba(85, 170, 255, 255)")
        self.setValue(self.ram_percent, self.ui.labelPercentageRAM,
                      self.ui.circularProgressRAM, "rgba(255, 0, 127, 255)")


    def setValue(self, value, labelPercentage, progressBarName, color):

        sliderValue = value

        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace(
            "{VALUE}", f"{sliderValue:.1f}"))

        # CALL DEF progressBarValue
        self.progressBarValue(sliderValue, progressBarName, color)

    def progressBarValue(self, value, widget, color):
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace(
            "{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)



# SPLASH SCREEN
class SplashScreen(QtWidgets.QMainWindow):
    counter = 0

    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent=parent)
        self.resize(500, 350)
        self.center()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # Change Texts
        QtCore.QTimer.singleShot(500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        self.show()

    def progress(self):

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.counter > 100:
                # STOP TIMER
                self.timer.stop()

                # SHOW MAIN WINDOW
                self.main = MainWindow()
                self.main.setWindowTitle('Live Stream')
                self.main.setWindowIcon(QtGui.QIcon(':/images/img/plhlder.png'))
                self.main.show()

                # CLOSE SPLASH SCREEN
                self.close()

            # INCREASE COUNTER
        self.counter += 1

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = SplashScreen()
    widget.show()
    sys.exit(app.exec_())

