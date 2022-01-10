from PySide6 import QtCore, QtWidgets, QtGui
# from system_tray import system_tray
from .window import Ui_main_window


class clipboard_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
