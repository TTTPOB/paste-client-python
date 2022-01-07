# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_config_page(object):
    def setupUi(self, config_page):
        if not config_page.objectName():
            config_page.setObjectName(u"config_page")
        config_page.resize(419, 584)
        self.verticalLayoutWidget = QWidget(config_page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 40, 311, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.server_address_label = QLabel(self.verticalLayoutWidget)
        self.server_address_label.setObjectName(u"server_address_label")

        self.verticalLayout.addWidget(self.server_address_label)

        self.server_address_textbox = QLineEdit(self.verticalLayoutWidget)
        self.server_address_textbox.setObjectName(u"server_address_textbox")

        self.verticalLayout.addWidget(self.server_address_textbox)

        self.uid_label = QLabel(self.verticalLayoutWidget)
        self.uid_label.setObjectName(u"uid_label")

        self.verticalLayout.addWidget(self.uid_label)

        self.user_id_textbox = QLineEdit(self.verticalLayoutWidget)
        self.user_id_textbox.setObjectName(u"user_id_textbox")

        self.verticalLayout.addWidget(self.user_id_textbox)

        self.cid_label = QLabel(self.verticalLayoutWidget)
        self.cid_label.setObjectName(u"cid_label")

        self.verticalLayout.addWidget(self.cid_label)

        self.client_id_textbox = QLineEdit(self.verticalLayoutWidget)
        self.client_id_textbox.setObjectName(u"client_id_textbox")

        self.verticalLayout.addWidget(self.client_id_textbox)

        self.pubkey_label = QLabel(self.verticalLayoutWidget)
        self.pubkey_label.setObjectName(u"pubkey_label")

        self.verticalLayout.addWidget(self.pubkey_label)

        self.pubkey_content = QLabel(self.verticalLayoutWidget)
        self.pubkey_content.setObjectName(u"pubkey_content")

        self.verticalLayout.addWidget(self.pubkey_content)

        self.priv_key_label = QLabel(self.verticalLayoutWidget)
        self.priv_key_label.setObjectName(u"priv_key_label")

        self.verticalLayout.addWidget(self.priv_key_label)

        self.privkey_content = QLabel(self.verticalLayoutWidget)
        self.privkey_content.setObjectName(u"privkey_content")

        self.verticalLayout.addWidget(self.privkey_content)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh_config_button = QPushButton(self.verticalLayoutWidget)
        self.refresh_config_button.setObjectName(u"refresh_config_button")

        self.horizontalLayout.addWidget(self.refresh_config_button)

        self.generate_new_keypair_botton = QPushButton(self.verticalLayoutWidget)
        self.generate_new_keypair_botton.setObjectName(u"generate_new_keypair_botton")

        self.horizontalLayout.addWidget(self.generate_new_keypair_botton)

        self.save_config_button = QPushButton(self.verticalLayoutWidget)
        self.save_config_button.setObjectName(u"save_config_button")

        self.horizontalLayout.addWidget(self.save_config_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(config_page)

        QMetaObject.connectSlotsByName(config_page)
    # setupUi

    def retranslateUi(self, config_page):
        config_page.setWindowTitle(QCoreApplication.translate("config_page", u"config page", None))
        self.server_address_label.setText(QCoreApplication.translate("config_page", u"server address", None))
        self.uid_label.setText(QCoreApplication.translate("config_page", u"user id", None))
        self.cid_label.setText(QCoreApplication.translate("config_page", u"client id", None))
        self.pubkey_label.setText(QCoreApplication.translate("config_page", u"client pub key", None))
        self.pubkey_content.setText(QCoreApplication.translate("config_page", u"empty pub key", None))
        self.priv_key_label.setText(QCoreApplication.translate("config_page", u"client priv key", None))
        self.privkey_content.setText(QCoreApplication.translate("config_page", u"empty priv key", None))
        self.refresh_config_button.setText(QCoreApplication.translate("config_page", u"Load Config", None))
        self.generate_new_keypair_botton.setText(QCoreApplication.translate("config_page", u"Generate Key Pair", None))
        self.save_config_button.setText(QCoreApplication.translate("config_page", u"Save Config", None))
    # retranslateUi

