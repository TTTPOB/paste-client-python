__package__ = "paste_client_python"
from yaml import safe_load
import time
from pathlib import Path
from .qtgui.main_window.mainwindow import clipboard_window
from .qtgui.system_tray import system_tray
from .qtgui.config_page.config_page import config_page
from PySide6.QtWebSockets import QWebSocket
from PySide6 import QtWidgets, QtCore
from nacl.public import PublicKey, PrivateKey
from nacl.encoding import HexEncoder
from PySide6.QtCore import QThread, QThreadPool, QObject, Signal, Slot


class paste_client_config:
    def __init__(self, file_path) -> None:
        if Path(file_path).is_file():
            with open(file_path, "r") as f:
                # print("Loading config file: " + file_path)
                self.config = safe_load(f)
                config = self.config
                self.server_address = config["server_address"]
                self.uid = config["uid"]
                self.cid = config["cid"]
                self.pubkey = config["pubkey"]
                self.privkey = config["privkey"]
        else:
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w") as f:
                f.write("")
                self.server_address = ""
                self.uid = ""
                self.cid = ""
                self.pubkey = ""
                self.privkey = ""

    def update_from_config_page(self, config_page):
        self.server_address = config_page.ui.server_address_content.text()
        self.uid = config_page.ui.uid_content.text()
        self.cid = config_page.ui.cid_content.text()
        self.pubkey = config_page.ui.pubkey_content.text()
        self.privkey = config_page.ui.privkey_content.text()


class paste_client:
    def __init__(self, config) -> None:
        for key in config.keys():
            setattr(self, key, config[key])
        self.main_window = clipboard_window()
        self.ws_thread = QThread()
        self.tray = system_tray(self)
        self.config_page = config_page()
        self.config_page.set_parent(self)

        if self.server_address:
            # https://forum.qt.io/topic/85768/errors-facing-while-running-qwebsocket-in-different-thread-than-the-main-thread/3
            self.ws = QWebSocket()

            self.ws_retry_max = 10
            self.ws_retry_count = 1

            self.ws.connected.connect(self.on_ws_connected)
            self.ws.textMessageReceived.connect(self.on_ws_received)
            self.ws.error.connect(self.on_ws_error)
            self.ws.disconnected.connect(self.on_ws_disconnected)

            self.ws.moveToThread(self.ws_thread)
            print("connecting to " + self.server_address)
            self.ws.open(self.server_address)
            print("connected")

        self.clipboard = QtWidgets.QApplication.clipboard()
        print("clipboard initialized")
        self.clipboard.dataChanged.connect(self.on_clipboard_changed)

    @QtCore.Slot()
    def on_ws_connected(self):
        print("websocket connected")
        self.ws.sendTextMessage("Hello World")
        self.ws_retry_count = 1

    @QtCore.Slot()
    def on_ws_disconnected(self):
        print("websocket disconnected")
        for i in range(self.ws_retry_max):
            time.sleep(1)
            print(f"retry {i}")
            if not self.ws.isValid():
                self.ws.open(self.server_address)
            else:
                break

    @QtCore.Slot(Exception)
    def on_ws_error(self, error):
        print(f"websocket error: {error}")

    @QtCore.Slot(str)
    def on_ws_received(self, message):
        print("websocket received: " + message)

    @QtCore.Slot()
    def on_clipboard_changed(self):
        print("clipboard changed")
        self.main_window.ui.current_clipboard_textview.setText(self.clipboard.text())
        self.ws.sendTextMessage(self.clipboard.text())

    @QtCore.Slot()
    def generate_new_keypair(self):
        print("button clicked")
        key_pair = PrivateKey.generate()
        self.key_pair = key_pair

        self.config_page.ui.pubkey_content.setText(
            key_pair.public_key.encode(encoder=HexEncoder).decode()
        )
        self.config_page.ui.privkey_content.setText(
            key_pair.encode(encoder=HexEncoder).decode()
        )
