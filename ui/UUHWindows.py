from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QDesktopWidget
from PyQt5 import QtCore
from common import logger
from module.hdmiout.Tmain import test
from module.enumItem import Status
from common import uuh_protocol

class UUHWindows(QWidget):
    # INIT
    def __init__(self):
        super().__init__()
        self.screen = QDesktopWidget().screenGeometry()
        self.test = test()
        self.log = logger.Logger(__name__)
        self.initUI()
        self.initConnect()
        self.test.init()


    def initUI(self):
        self.setWindowTitle("Helper")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        self.label_0 = QLabel("Button")
        self.layout.addWidget(self.label_0)

        self.button = QPushButton("Initializing")
        self.layout.addWidget(self.button)
        
    def initConnect(self):
        self.test.test_signal.connect(self.slot_flush_text)
        self.button.clicked.connect(self.buttonClicked)

    # ACTIVE
    def buttonClicked(self):
        # print (self.test.get_status())
        if self.test.get_status() == Status.STOP:
            self.test.set_status(Status.RUNNING)
            self.button.setText('Start')
        elif self.test.get_status() == Status.RUNNING:
            self.test.set_status(Status.STOP)
            self.button.setText('Stop')

    @QtCore.pyqtSlot(str)
    def slot_flush_text(self, msg):
        msg = uuh_protocol.uuh_decode(msg)
        print (msg)
        # if index == 0:
        #     self.label_0.setText(text)
        # else :
        #     self.log.error("unKnow index:"+str(index)+", text:"+str(text))

        
        

