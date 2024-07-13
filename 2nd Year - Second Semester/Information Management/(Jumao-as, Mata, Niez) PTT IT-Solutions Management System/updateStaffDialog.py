# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateStaffDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_UpdateStaffDialog(object):
    def setupUi(self, UpdateStaffDialog):
        if not UpdateStaffDialog.objectName():
            UpdateStaffDialog.setObjectName(u"UpdateStaffDialog")
        UpdateStaffDialog.resize(379, 300)
        UpdateStaffDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(UpdateStaffDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(UpdateStaffDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLineEdit(UpdateStaffDialog)
        self.fname.setObjectName(u"fname")
        self.fname.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"\n"
"")
        self.fname.setMaxLength(25)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_2 = QLabel(UpdateStaffDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lname = QLineEdit(UpdateStaffDialog)
        self.lname.setObjectName(u"lname")
        self.lname.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"\n"
"")
        self.lname.setMaxLength(25)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lname)

        self.label_3 = QLabel(UpdateStaffDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.mobileNum = QLineEdit(UpdateStaffDialog)
        self.mobileNum.setObjectName(u"mobileNum")
        self.mobileNum.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"\n"
"")
        self.mobileNum.setMaxLength(11)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.mobileNum)

        self.label_4 = QLabel(UpdateStaffDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.address = QLineEdit(UpdateStaffDialog)
        self.address.setObjectName(u"address")
        self.address.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")
        self.address.setMaxLength(50)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.address)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.frame = QFrame(UpdateStaffDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
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


        self.retranslateUi(UpdateStaffDialog)

        QMetaObject.connectSlotsByName(UpdateStaffDialog)
    # setupUi

    def retranslateUi(self, UpdateStaffDialog):
        UpdateStaffDialog.setWindowTitle(QCoreApplication.translate("UpdateStaffDialog", u"Edit Staff", None))
        self.label.setText(QCoreApplication.translate("UpdateStaffDialog", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("UpdateStaffDialog", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("UpdateStaffDialog", u"Mobile Number", None))
        self.label_4.setText(QCoreApplication.translate("UpdateStaffDialog", u"Address", None))
        self.confirm.setText(QCoreApplication.translate("UpdateStaffDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("UpdateStaffDialog", u"Cancel", None))
    # retranslateUi

