from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QGuiApplication


class system_tray(QtWidgets.QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.menu = QtWidgets.QMenu()

        self.setIcon(QtGui.QIcon("resources/icon/tray.svg"))
        self.setToolTip("Paste Client")

        self.quit = QtGui.QAction("Quit", self)
        self.quit.triggered.connect(self.on_quit)
        self.menu.addAction(self.quit)

        self.activated.connect(self.on_activated)

        self.setContextMenu(self.menu)
        self.show()

    def on_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.showMessage()

    def on_quit(self):
        QGuiApplication.quit()

    def showMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Paste Client")
        msg.setInformativeText("Paste Client")
        msg.setWindowTitle("Paste Client")
        msg.setDetailedText("Paste Client")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
