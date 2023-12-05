from module.enumItem import Status
from PyQt5.QtCore import QObject, pyqtSignal

from common.logger import Logger
from common import uuh_protocol

class test(QObject):
    test_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.log = Logger(__name__)
        self.status = Status.INIT

    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.log.info("Change Status to ", Status(status))
        if self.status == Status.INIT and status == Status.STOP:
            self.send_signal(0, "text")
        self.status = status

    def send_signal(self, index, text):
        self.test_signal.emit(uuh_protocol.uuh_code(index, text))

    def init(self):
        self.set_status(Status.STOP)