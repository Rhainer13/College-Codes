# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteProductDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DeleteProductDialog(object):
    def setupUi(self, DeleteProductDialog):
        if not DeleteProductDialog.objectName():
            DeleteProductDialog.setObjectName(u"DeleteProductDialog")
        DeleteProductDialog.resize(367, 134)
        DeleteProductDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(DeleteProductDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.notification = QLabel(DeleteProductDialog)
        self.notification.setObjectName(u"notification")
        self.notification.setStyleSheet(u"QLabel {\n"
"    font: 700 ;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.notification.setAlignment(Qt.AlignCenter)
        self.notification.setWordWrap(True)

        self.verticalLayout.addWidget(self.notification)

        self.frame = QFrame(DeleteProductDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirm = QPushButton(self.frame)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.confirm)

        self.cancel = QPushButton(self.frame)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DeleteProductDialog)

        QMetaObject.connectSlotsByName(DeleteProductDialog)
    # setupUi

    def retranslateUi(self, DeleteProductDialog):
        DeleteProductDialog.setWindowTitle(QCoreApplication.translate("DeleteProductDialog", u"Delete Product", None))
        self.notification.setText(QCoreApplication.translate("DeleteProductDialog", u"Are you sure you want to delete [product name]?", None))
        self.confirm.setText(QCoreApplication.translate("DeleteProductDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("DeleteProductDialog", u"Cancel", None))
    # retranslateUi

