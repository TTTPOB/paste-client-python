from PySide6 import QtCore
from PySide6.QtWebSockets import QWebSocket
from PySide6.QtCore import QObject
from typing import Optional
from time import sleep

# make a new websocket client class to enable websockt to be run in
# a separate thread
class websocket_client(QObject):
    def __init__(self, url: str, max_retry: int = 5) -> None:
        super().__init__()
        self.url = url
        self.max_retry = max_retry

    def start_connection(self):
        self.ws = QWebSocket()
        self.ws.open(self.url)
        print(f"ws thread id: {self.thread()}")
        self.ws.connected.connect(lambda: self.on_connected())
        self.ws.disconnected.connect(lambda: self.on_disconnected())

    def on_text_message_received(self, message):
        print("websocket received: " + message)

    def on_connected(self):
        print("websocket connected")
        self.ws.sendTextMessage("Hello World")

    def on_disconnected(self):
        print(f"ws disconnected")
        self.reconnect()
    
    def reconnect(self):
        print(f"trying to reconnect to {self.url}")
        self.ws.open(self.url)
        print(f"connection status: {self.ws.isValid()}")


    def sendTextMessage(self, message):
        self.ws.sendTextMessage(message)
