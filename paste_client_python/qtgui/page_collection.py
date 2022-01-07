from .config_page import Ui_config_page
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget

# wrap the config_page.py in a class
# add code to make it a QWidget
class config_page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_config_page()
        self.ui.setupUi(self)