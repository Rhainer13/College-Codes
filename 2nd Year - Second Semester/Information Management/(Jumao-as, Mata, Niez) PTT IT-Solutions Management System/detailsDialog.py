# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailsDialog.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_DetailsDialog(object):
    def setupUi(self, DetailsDialog):
        if not DetailsDialog.objectName():
            DetailsDialog.setObjectName(u"DetailsDialog")
        DetailsDialog.resize(383, 382)
        DetailsDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(DetailsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DetailsDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.category = QLineEdit(DetailsDialog)
        self.category.setObjectName(u"category")
        self.category.setStyleSheet(u"QLineEdit{\n"
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
        self.category.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.category)

        self.label_3 = QLabel(DetailsDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.name = QLineEdit(DetailsDialog)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"QLineEdit{\n"
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
        self.name.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)

        self.label_4 = QLabel(DetailsDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.price = QLineEdit(DetailsDialog)
        self.price.setObjectName(u"price")
        self.price.setStyleSheet(u"QLineEdit{\n"
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
        self.price.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.price)


        self.verticalLayout.addLayout(self.formLayout)

        self.stackedWidget = QStackedWidget(DetailsDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.cpuBrand = QLineEdit(self.page)
        self.cpuBrand.setObjectName(u"cpuBrand")
        self.cpuBrand.setStyleSheet(u"QLineEdit{\n"
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
        self.cpuBrand.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cpuBrand)

        self.coreCount = QLineEdit(self.page)
        self.coreCount.setObjectName(u"coreCount")
        self.coreCount.setStyleSheet(u"QLineEdit{\n"
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
        self.coreCount.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.coreCount)


        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.ramBrand = QLineEdit(self.page_2)
        self.ramBrand.setObjectName(u"ramBrand")
        self.ramBrand.setStyleSheet(u"QLineEdit{\n"
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
        self.ramBrand.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.ramBrand)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.ramSize = QLineEdit(self.page_2)
        self.ramSize.setObjectName(u"ramSize")
        self.ramSize.setStyleSheet(u"QLineEdit{\n"
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
        self.ramSize.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.ramSize)


        self.gridLayout_2.addLayout(self.formLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.mbBrand = QLineEdit(self.page_3)
        self.mbBrand.setObjectName(u"mbBrand")
        self.mbBrand.setStyleSheet(u"QLineEdit{\n"
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
        self.mbBrand.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.mbBrand)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.mbSize = QLineEdit(self.page_3)
        self.mbSize.setObjectName(u"mbSize")
        self.mbSize.setStyleSheet(u"QLineEdit{\n"
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
        self.mbSize.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.mbSize)


        self.gridLayout_3.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_4 = QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.storageBrand = QLineEdit(self.page_4)
        self.storageBrand.setObjectName(u"storageBrand")
        self.storageBrand.setStyleSheet(u"QLineEdit{\n"
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
        self.storageBrand.setReadOnly(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.storageBrand)

        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.storageSize = QLineEdit(self.page_4)
        self.storageSize.setObjectName(u"storageSize")
        self.storageSize.setStyleSheet(u"QLineEdit{\n"
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
        self.storageSize.setReadOnly(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.storageSize)

        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.storageType = QLineEdit(self.page_4)
        self.storageType.setObjectName(u"storageType")
        self.storageType.setStyleSheet(u"QLineEdit{\n"
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
        self.storageType.setReadOnly(True)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.storageType)


        self.gridLayout_4.addLayout(self.formLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_5 = QGridLayout(self.page_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.psuBrand = QLineEdit(self.page_5)
        self.psuBrand.setObjectName(u"psuBrand")
        self.psuBrand.setStyleSheet(u"QLineEdit{\n"
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
        self.psuBrand.setReadOnly(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.psuBrand)

        self.label_14 = QLabel(self.page_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.psuWatts = QLineEdit(self.page_5)
        self.psuWatts.setObjectName(u"psuWatts")
        self.psuWatts.setStyleSheet(u"QLineEdit{\n"
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
        self.psuWatts.setReadOnly(True)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.psuWatts)


        self.gridLayout_5.addLayout(self.formLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(DetailsDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.close = QPushButton(self.frame)
        self.close.setObjectName(u"close")
        self.close.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.close)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DetailsDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DetailsDialog)
    # setupUi

    def retranslateUi(self, DetailsDialog):
        DetailsDialog.setWindowTitle(QCoreApplication.translate("DetailsDialog", u"Product Details", None))
        self.label.setText(QCoreApplication.translate("DetailsDialog", u"Category", None))
        self.label_3.setText(QCoreApplication.translate("DetailsDialog", u"Name", None))
        self.name.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("DetailsDialog", u"Price", None))
        self.label_5.setText(QCoreApplication.translate("DetailsDialog", u"Core Count", None))
        self.label_6.setText(QCoreApplication.translate("DetailsDialog", u"Brand", None))
        self.label_2.setText(QCoreApplication.translate("DetailsDialog", u"Brand", None))
        self.label_7.setText(QCoreApplication.translate("DetailsDialog", u"Size (GB)", None))
        self.label_8.setText(QCoreApplication.translate("DetailsDialog", u"Brand", None))
        self.label_9.setText(QCoreApplication.translate("DetailsDialog", u"Form Factor", None))
        self.label_10.setText(QCoreApplication.translate("DetailsDialog", u"Brand", None))
        self.label_11.setText(QCoreApplication.translate("DetailsDialog", u"Size (GB)", None))
        self.label_12.setText(QCoreApplication.translate("DetailsDialog", u"Type", None))
        self.label_13.setText(QCoreApplication.translate("DetailsDialog", u"Brand", None))
        self.label_14.setText(QCoreApplication.translate("DetailsDialog", u"Wattage", None))
        self.close.setText(QCoreApplication.translate("DetailsDialog", u"Close", None))
    # retranslateUi

