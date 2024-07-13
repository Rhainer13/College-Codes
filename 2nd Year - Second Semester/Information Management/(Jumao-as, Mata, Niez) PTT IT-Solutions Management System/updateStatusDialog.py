# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateStatusDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_UpdateStatusDialog(object):
    def setupUi(self, UpdateStatusDialog):
        if not UpdateStatusDialog.objectName():
            UpdateStatusDialog.setObjectName(u"UpdateStatusDialog")
        UpdateStatusDialog.resize(285, 141)
        UpdateStatusDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.gridLayout = QGridLayout(UpdateStatusDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.completed = QPushButton(UpdateStatusDialog)
        self.completed.setObjectName(u"completed")
        self.completed.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"margin-left: 25px;\n"
"margin-right:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"                    background-color: #2980b9; /* Darker blue on hover */\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: #1f618d; /* Even darker blue when pressed */\n"
"                }")

        self.verticalLayout.addWidget(self.completed)

        self.cancelled = QPushButton(UpdateStatusDialog)
        self.cancelled.setObjectName(u"cancelled")
        self.cancelled.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"margin-left: 25px;\n"
"margin-right:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #e74c3c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #e74c3c;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.cancelled)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(UpdateStatusDialog)

        QMetaObject.connectSlotsByName(UpdateStatusDialog)
    # setupUi

    def retranslateUi(self, UpdateStatusDialog):
        UpdateStatusDialog.setWindowTitle(QCoreApplication.translate("UpdateStatusDialog", u"Dialog", None))
        self.completed.setText(QCoreApplication.translate("UpdateStatusDialog", u"Completed", None))
        self.cancelled.setText(QCoreApplication.translate("UpdateStatusDialog", u"Cancelled", None))
    # retranslateUi

