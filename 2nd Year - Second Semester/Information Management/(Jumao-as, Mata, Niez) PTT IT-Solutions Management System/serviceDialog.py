# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serviceDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ServiceDialog(object):
    def setupUi(self, ServiceDialog):
        if not ServiceDialog.objectName():
            ServiceDialog.setObjectName(u"ServiceDialog")
        ServiceDialog.resize(480, 374)
        ServiceDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(ServiceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(ServiceDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.customer = QLineEdit(ServiceDialog)
        self.customer.setObjectName(u"customer")
        self.customer.setStyleSheet(u"QLineEdit{\n"
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
        self.customer.setMaxLength(50)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.customer)

        self.label_2 = QLabel(ServiceDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.device = QComboBox(ServiceDialog)
        self.device.setObjectName(u"device")
        self.device.setStyleSheet(u"QComboBox{\n"
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
"QComboBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.device)

        self.label_3 = QLabel(ServiceDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.technician = QComboBox(ServiceDialog)
        self.technician.setObjectName(u"technician")
        self.technician.setStyleSheet(u"QComboBox{\n"
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
"QComboBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.technician)

        self.label_4 = QLabel(ServiceDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.serviceType = QComboBox(ServiceDialog)
        self.serviceType.setObjectName(u"serviceType")
        self.serviceType.setStyleSheet(u"QComboBox{\n"
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
"QComboBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.serviceType)

        self.label_5 = QLabel(ServiceDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(ServiceDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
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
"QLabel:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_6)

        self.label_7 = QLabel(ServiceDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.additionalFee = QDoubleSpinBox(ServiceDialog)
        self.additionalFee.setObjectName(u"additionalFee")
        self.additionalFee.setStyleSheet(u"QDoubleSpinBox{\n"
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
"QDoubleSpinBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"\n"
"")
        self.additionalFee.setMaximum(9999.989999999999782)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.additionalFee)


        self.verticalLayout.addLayout(self.formLayout)

        self.frame = QFrame(ServiceDialog)
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


        self.retranslateUi(ServiceDialog)

        QMetaObject.connectSlotsByName(ServiceDialog)
    # setupUi

    def retranslateUi(self, ServiceDialog):
        ServiceDialog.setWindowTitle(QCoreApplication.translate("ServiceDialog", u"Service", None))
        self.label.setText(QCoreApplication.translate("ServiceDialog", u"Customer Name", None))
        self.label_2.setText(QCoreApplication.translate("ServiceDialog", u"Device", None))
        self.label_3.setText(QCoreApplication.translate("ServiceDialog", u"Technician", None))
        self.label_4.setText(QCoreApplication.translate("ServiceDialog", u"Service Type", None))
        self.label_5.setText(QCoreApplication.translate("ServiceDialog", u"Base Fee", None))
        self.label_6.setText(QCoreApplication.translate("ServiceDialog", u"Php 100.00", None))
        self.label_7.setText(QCoreApplication.translate("ServiceDialog", u"Additional Fee", None))
        self.confirm.setText(QCoreApplication.translate("ServiceDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("ServiceDialog", u"Cancel", None))
    # retranslateUi

