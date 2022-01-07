from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QGuiApplication
from .config_page.config_page import config_page


class system_tray(QtWidgets.QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.menu = QtWidgets.QMenu()

        self.setIcon(QtGui.QIcon("resources/icon/tray.svg"))
        self.setToolTip("Paste Client")

        self.quit = QtGui.QAction("Quit", self)
        self.quit.triggered.connect(self.on_quit)
        self.menu.addAction(self.quit)

        self.show_config_page = QtGui.QAction("Show Config Page", self)
        self.show_config_page.triggered.connect(self.on_config_page)
        self.menu.addAction(self.show_config_page)

        self.activated.connect(self.on_activated)

        self.setContextMenu(self.menu)
        self.show()

    def on_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.showMessage()

    def on_quit(self):
        QGuiApplication.quit()
    
    def on_config_page(self):
        self.config_page = config_page()
        self.config_page.show()

    def showMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Paste Client")
        msg.setInformativeText("Paste Client")
        msg.setWindowTitle("Paste Client")
        msg.setDetailedText("Paste Client")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
