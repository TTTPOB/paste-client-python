from paste_client import paste_client
from paste_client import paste_client_config
from PySide6 import QtWidgets
import sys


if __name__ == "__main__":
    __package__ = 'paste_client_python'
    app = QtWidgets.QApplication(sys.argv)
    config = paste_client_config("config.yaml").config
    tray = paste_client(config).tray
    # tray.show()
    # widget.show()
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())
