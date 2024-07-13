# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchaseReceiptDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QDoubleSpinBox,
    QFormLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_PurchaseReceiptDialog(object):
    def setupUi(self, PurchaseReceiptDialog):
        if not PurchaseReceiptDialog.objectName():
            PurchaseReceiptDialog.setObjectName(u"PurchaseReceiptDialog")
        PurchaseReceiptDialog.resize(715, 567)
        PurchaseReceiptDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(PurchaseReceiptDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.purchaseReceiptTable = QTableWidget(PurchaseReceiptDialog)
        if (self.purchaseReceiptTable.columnCount() < 6):
            self.purchaseReceiptTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.purchaseReceiptTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.purchaseReceiptTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.purchaseReceiptTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.purchaseReceiptTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.purchaseReceiptTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.purchaseReceiptTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.purchaseReceiptTable.setObjectName(u"purchaseReceiptTable")
        self.purchaseReceiptTable.setStyleSheet(u"QWidget {\n"
"\n"
"    background-color: rgb(218, 211, 190);\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.purchaseReceiptTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.purchaseReceiptTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.purchaseReceiptTable)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setContentsMargins(470, -1, -1, -1)
        self.label_2 = QLabel(PurchaseReceiptDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font: 700 ;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.total = QDoubleSpinBox(PurchaseReceiptDialog)
        self.total.setObjectName(u"total")
        self.total.setMaximumSize(QSize(1677, 16777215))
        self.total.setStyleSheet(u"QDoubleSpinBox{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 13px;\n"
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
"")
        self.total.setReadOnly(True)
        self.total.setMaximum(99999.990000000005239)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.total)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.close = QPushButton(PurchaseReceiptDialog)
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

        self.verticalLayout.addWidget(self.close)


        self.retranslateUi(PurchaseReceiptDialog)

        QMetaObject.connectSlotsByName(PurchaseReceiptDialog)
    # setupUi

    def retranslateUi(self, PurchaseReceiptDialog):
        PurchaseReceiptDialog.setWindowTitle(QCoreApplication.translate("PurchaseReceiptDialog", u"Purchase Receipt", None))
        ___qtablewidgetitem = self.purchaseReceiptTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Brand", None));
        ___qtablewidgetitem1 = self.purchaseReceiptTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Name", None));
        ___qtablewidgetitem2 = self.purchaseReceiptTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Category", None));
        ___qtablewidgetitem3 = self.purchaseReceiptTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Price", None));
        ___qtablewidgetitem4 = self.purchaseReceiptTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Quantity", None));
        ___qtablewidgetitem5 = self.purchaseReceiptTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Subtotal", None));
        self.label_2.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Total", None))
        self.close.setText(QCoreApplication.translate("PurchaseReceiptDialog", u"Close", None))
    # retranslateUi

