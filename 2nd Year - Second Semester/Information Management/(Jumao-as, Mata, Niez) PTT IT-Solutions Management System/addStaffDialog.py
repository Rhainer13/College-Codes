# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addStaffDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddStaffDialog(object):
    def setupUi(self, AddStaffDialog):
        if not AddStaffDialog.objectName():
            AddStaffDialog.setObjectName(u"AddStaffDialog")
        AddStaffDialog.resize(391, 386)
        AddStaffDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(AddStaffDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(AddStaffDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLineEdit(AddStaffDialog)
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

        self.label_2 = QLabel(AddStaffDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lname = QLineEdit(AddStaffDialog)
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
"")
        self.lname.setMaxLength(25)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lname)

        self.label_3 = QLabel(AddStaffDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.mobileNum = QLineEdit(AddStaffDialog)
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
"")
        self.mobileNum.setMaxLength(11)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.mobileNum)

        self.label_4 = QLabel(AddStaffDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.address = QLineEdit(AddStaffDialog)
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
"\n"
"")
        self.address.setMaxLength(50)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.address)

        self.label_5 = QLabel(AddStaffDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.dateHired = QDateEdit(AddStaffDialog)
        self.dateHired.setObjectName(u"dateHired")
        self.dateHired.setStyleSheet(u"QDateEdit{\n"
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
"")
        self.dateHired.setDateTime(QDateTime(QDate(2024, 6, 1), QTime(0, 0, 0)))
        self.dateHired.setMaximumDate(QDate(2024, 6, 30))

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.dateHired)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.frame = QFrame(AddStaffDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 120))
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


        self.retranslateUi(AddStaffDialog)

        QMetaObject.connectSlotsByName(AddStaffDialog)
    # setupUi

    def retranslateUi(self, AddStaffDialog):
        AddStaffDialog.setWindowTitle(QCoreApplication.translate("AddStaffDialog", u"Add Staff", None))
        self.label.setText(QCoreApplication.translate("AddStaffDialog", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("AddStaffDialog", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("AddStaffDialog", u"Mobile Number", None))
        self.label_4.setText(QCoreApplication.translate("AddStaffDialog", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("AddStaffDialog", u"Date Hired", None))
        self.confirm.setText(QCoreApplication.translate("AddStaffDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("AddStaffDialog", u"Cancel", None))
    # retranslateUi

