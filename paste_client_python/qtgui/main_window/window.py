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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(631, 608)
        self.verticalLayoutWidget = QWidget(main_window)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 100, 341, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.clipboard_text_label = QLabel(self.verticalLayoutWidget)
        self.clipboard_text_label.setObjectName(u"clipboard_text_label")

        self.verticalLayout.addWidget(self.clipboard_text_label)

        self.current_clipboard_textview = QTextBrowser(self.verticalLayoutWidget)
        self.current_clipboard_textview.setObjectName(u"current_clipboard_textview")
        self.current_clipboard_textview.setReadOnly(False)

        self.verticalLayout.addWidget(self.current_clipboard_textview)


        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Form", None))
        self.clipboard_text_label.setText(QCoreApplication.translate("main_window", u"Current Clipboard Text", None))
    # retranslateUi

