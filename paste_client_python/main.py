from qtgui import clipboard_window
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = clipboard_window()
    widget.show()
    sys.exit(app.exec())
