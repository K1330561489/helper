import sys
from ui.UUHWindows import UUHWindows
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UUHWindows()
    window.show()
    sys.exit(app.exec_())
