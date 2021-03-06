from .qtgui.main_window.mainwindow import clipboard_window
from PySide6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = clipboard_window()
    tray = widget.tray
    # tray.show()
    widget.show()
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())
