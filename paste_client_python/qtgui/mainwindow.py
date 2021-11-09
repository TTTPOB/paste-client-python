from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication
# from system_tray import system_tray
from qtgui.system_tray import system_tray
import random
from PySide6.QtWebSockets import QWebSocket


class clipboard_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["1111", "2222"]
        self.button = QtWidgets.QPushButton("Hello World")
        self.text = QtWidgets.QTextEdit("Hello World___")
        self.clipboard = QGuiApplication.clipboard()
        self.url = "ws://localhost:8000/ws/100"

        # self.tray = QtWidgets.QSystemTrayIcon(QtGui.QIcon("../resources/icon/tray.svg"),self)
        self.tray = system_tray()
        self.tray.show()

        self.ws = QWebSocket()
        self.ws.connected.connect(self.on_ws_connected)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        self.button.clicked.connect(self.on_button_clicked)
        self.clipboard.dataChanged.connect(self.on_clipboard_changed)


    @QtCore.Slot()
    def on_button_clicked(self):
        self.text.setText(random.choice(self.hello))
        self.ws.open(self.url)

    @QtCore.Slot()
    def on_clipboard_changed(self):
        print("clipboard changed")
        self.text.setText(self.clipboard.text())

    @QtCore.Slot()
    def on_ws_connected(self):
        print("websocket connected")
        self.ws.sendTextMessage("Hello World")