from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QGuiApplication
import random


class clipboard_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["1111", "2222"]
        self.button = QtWidgets.QPushButton("Hello World")
        self.text = QtWidgets.QTextEdit("Hello World___")
        self.clipboard = QGuiApplication.clipboard()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        self.button.clicked.connect(self.on_button_clicked)
        self.clipboard.dataChanged.connect(self.on_clipboard_changed)

    @QtCore.Slot()
    def on_button_clicked(self):
        self.text.setText(random.choice(self.hello))

    @QtCore.Slot()
    def on_clipboard_changed(self):
        print("clipboard changed")
        self.text.setText(self.clipboard.text())
