
import sys
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

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.resize(500, 350)
        self.center()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


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

