# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderDialog.ui'
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
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        if not OrderDialog.objectName():
            OrderDialog.setObjectName(u"OrderDialog")
        OrderDialog.resize(942, 577)
        OrderDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(OrderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(OrderDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font: 700 ;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.customerName = QLineEdit(OrderDialog)
        self.customerName.setObjectName(u"customerName")
        self.customerName.setStyleSheet(u"QLineEdit{\n"
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

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.customerName)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.cartTable = QTableWidget(OrderDialog)
        if (self.cartTable.columnCount() < 7):
            self.cartTable.setColumnCount(7)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.cartTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.cartTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.cartTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.cartTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.cartTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.cartTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.cartTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.cartTable.setObjectName(u"cartTable")
        self.cartTable.setStyleSheet(u"QWidget {\n"
"\n"
"    background-color: rgb(218, 211, 190);\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.cartTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cartTable.horizontalHeader().setDefaultSectionSize(100)
        self.cartTable.horizontalHeader().setStretchLastSection(True)
        self.cartTable.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.cartTable)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setContentsMargins(600, -1, 40, -1)
        self.label_2 = QLabel(OrderDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QSize(1677215, 16777215))
        self.label_2.setStyleSheet(u"QLabel {\n"
"                font-weight: bold; /* Sets the font weight to bold */\n"
"                color: black; /* Sets the font color to black */\n"
"                margin-left: center; /* Aligns to the right by pushing it to the right */\n"
"            }")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.total = QDoubleSpinBox(OrderDialog)
        self.total.setObjectName(u"total")
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
        self.total.setMaximum(999999.989999999990687)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.total)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame = QFrame(OrderDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirmOrder = QPushButton(self.frame)
        self.confirmOrder.setObjectName(u"confirmOrder")
        self.confirmOrder.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.confirmOrder)

        self.cancelOrder = QPushButton(self.frame)
        self.cancelOrder.setObjectName(u"cancelOrder")
        self.cancelOrder.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.cancelOrder)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(OrderDialog)

        QMetaObject.connectSlotsByName(OrderDialog)
    # setupUi

    def retranslateUi(self, OrderDialog):
        OrderDialog.setWindowTitle(QCoreApplication.translate("OrderDialog", u"Ongoing Orders", None))
        self.label.setText(QCoreApplication.translate("OrderDialog", u"Customer Name", None))
        ___qtablewidgetitem = self.cartTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OrderDialog", u"Brand", None));
        ___qtablewidgetitem1 = self.cartTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OrderDialog", u"Name", None));
        ___qtablewidgetitem2 = self.cartTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("OrderDialog", u"Category", None));
        ___qtablewidgetitem3 = self.cartTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("OrderDialog", u"Price", None));
        ___qtablewidgetitem4 = self.cartTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("OrderDialog", u"Quantity", None));
        ___qtablewidgetitem5 = self.cartTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("OrderDialog", u"Subtotal", None));
        ___qtablewidgetitem6 = self.cartTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("OrderDialog", u"Actions", None));
        self.label_2.setText(QCoreApplication.translate("OrderDialog", u"Total", None))
        self.confirmOrder.setText(QCoreApplication.translate("OrderDialog", u"Confirm Order", None))
        self.cancelOrder.setText(QCoreApplication.translate("OrderDialog", u"Cancel Order", None))
    # retranslateUi

