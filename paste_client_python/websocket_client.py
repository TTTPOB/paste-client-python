from PySide6 import QtCore
from PySide6.QtWebSockets import QWebSocket
from PySide6.QtCore import QObject
from typing import Optional

# make a new websocket client class to enable websockt to be run in
# a separate thread
class websocket_client(QObject):
    def __init__(self, url: str, max_retry: int = 5) -> None:
        super().__init__()
        self.url = url
        self.max_retry = max_retry

    def start_connection(self):
        self.ws = QWebSocket()
        self.ws.textMessageReceived.connect(self.on_text_message_received)
        self.ws.connected.connect(self.on_connected)
        self.ws.disconnected.connect(self.on_disconnected)
        self.ws.open(self.url)
        print(f"ws thread id: {QtCore.QThread.currentThread()}")

    @QtCore.Slot(str)
    def on_text_message_received(self, message):
        print("websocket received: " + message)

    @QtCore.Slot()
    def on_connected(self):
        print("websocket connected")
        self.ws.sendTextMessage("Hello World")

    @QtCore.Slot()
    def on_disconnected(self):
        # auto retry
        for i in range(self.max_retry):
            print("websocket disconnected, retry: " + str(i))
            self.start_connection()
            if self.ws.state() == QWebSocket.ConnectedState:
                break

    def sendTextMessage(self, message):
        self.ws.sendTextMessage(message)