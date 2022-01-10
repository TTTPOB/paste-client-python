from .window import Ui_config_page
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget
from nacl.public import PrivateKey, PublicKey
from nacl.encoding import HexEncoder

# wrap the config_page.py in a class
# add code to make it a QWidget
class config_page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_config_page()
        self.ui.setupUi(self)
        self.ui.generate_new_keypair_botton.clicked.connect(self.generate_new_keypair)

    def generate_new_keypair(self):
        key_pair = PrivateKey.generate()
        self.ui.pubkey_content.setText(
            key_pair.public_key.encode(encoder=HexEncoder).decode()
        )
        self.ui.privkey_content.setText(key_pair.encode(encoder=HexEncoder).decode())
