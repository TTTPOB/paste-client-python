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
from .websocket_client import websocket_client


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
        print(f"main thread id {QtCore.QThread.currentThread()}")

        if self.server_address:
            self.ws = websocket_client(self.server_address)

            self.ws.moveToThread(self.ws_thread)
            print("connecting to " + self.server_address)
            self.ws.start_connection()
            print(f"connection state: {self.ws.ws.isValid()}")

        self.clipboard = QtWidgets.QApplication.clipboard()
        print("clipboard initialized")
        self.clipboard.dataChanged.connect(self.on_clipboard_changed)

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
