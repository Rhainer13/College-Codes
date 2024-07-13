# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'staff.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_StaffPage(object):
    def setupUi(self, StaffPage):
        if not StaffPage.objectName():
            StaffPage.setObjectName(u"StaffPage")
        StaffPage.resize(1007, 600)
        StaffPage.setStyleSheet(u"QWidget{\n"
" background-color: rgb(183, 181, 151);\n"
"}")
        self.horizontalLayout = QHBoxLayout(StaffPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(StaffPage)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(107, 138, 122)\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inventory = QPushButton(self.frame)
        self.inventory.setObjectName(u"inventory")
        self.inventory.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 120px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.inventory)

        self.history = QPushButton(self.frame)
        self.history.setObjectName(u"history")
        self.history.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 120px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.history)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.viewOrder = QPushButton(self.frame)
        self.viewOrder.setObjectName(u"viewOrder")
        self.viewOrder.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 120px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.viewOrder)

        self.service = QPushButton(self.frame)
        self.service.setObjectName(u"service")
        self.service.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 120px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.service)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logOut = QPushButton(self.frame)
        self.logOut.setObjectName(u"logOut")
        self.logOut.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: #e74c3c;\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 120px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #e74c3c;\n"
"}\n"
"\n"
"s")

        self.verticalLayout.addWidget(self.logOut)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(StaffPage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QWidget{\n"
"background-color: rgb(107, 138, 122)\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.productSearch = QLineEdit(self.page)
        self.productSearch.setObjectName(u"productSearch")
        self.productSearch.setStyleSheet(u"QLineEdit{\n"
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
        self.productSearch.setMaxLength(50)

        self.horizontalLayout_2.addWidget(self.productSearch)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.inventoryTable = QTableWidget(self.page)
        if (self.inventoryTable.columnCount() < 6):
            self.inventoryTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.inventoryTable.setObjectName(u"inventoryTable")
        self.inventoryTable.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(183, 181, 151);\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.inventoryTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inventoryTable.setCornerButtonEnabled(False)
        self.inventoryTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.inventoryTable.horizontalHeader().setStretchLastSection(True)
        self.inventoryTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.inventoryTable)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget{\n"
"background-color: rgb(107, 138, 122)\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.staffSearch = QLineEdit(self.page_2)
        self.staffSearch.setObjectName(u"staffSearch")
        self.staffSearch.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout_3.addWidget(self.staffSearch)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.staffTable = QTableWidget(self.page_2)
        if (self.staffTable.columnCount() < 5):
            self.staffTable.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.staffTable.setObjectName(u"staffTable")
        self.staffTable.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(183, 181, 151);\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.staffTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.staffTable.horizontalHeader().setStretchLastSection(True)
        self.staffTable.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.staffTable)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QWidget{\n"
"background-color: rgb(107, 138, 122)\n"
"\n"
"}")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(183, 181, 151);\n"
"    font: 700 ;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.purchaseHistoryTable = QTableWidget(self.tab)
        if (self.purchaseHistoryTable.columnCount() < 3):
            self.purchaseHistoryTable.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.purchaseHistoryTable.setObjectName(u"purchaseHistoryTable")
        self.purchaseHistoryTable.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(183, 181, 151);\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.purchaseHistoryTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.purchaseHistoryTable.horizontalHeader().setDefaultSectionSize(200)
        self.purchaseHistoryTable.horizontalHeader().setStretchLastSection(True)
        self.purchaseHistoryTable.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.purchaseHistoryTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.serviceHistory = QTableWidget(self.tab_2)
        if (self.serviceHistory.columnCount() < 8):
            self.serviceHistory.setColumnCount(8)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.serviceHistory.setHorizontalHeaderItem(7, __qtablewidgetitem21)
        self.serviceHistory.setObjectName(u"serviceHistory")
        self.serviceHistory.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(183, 181, 151);\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.serviceHistory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.serviceHistory.horizontalHeader().setStretchLastSection(True)
        self.serviceHistory.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.serviceHistory, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(StaffPage)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StaffPage)
    # setupUi

    def retranslateUi(self, StaffPage):
        StaffPage.setWindowTitle(QCoreApplication.translate("StaffPage", u"Staff Page", None))
        self.inventory.setText(QCoreApplication.translate("StaffPage", u"Inventory", None))
        self.history.setText(QCoreApplication.translate("StaffPage", u"History", None))
        self.viewOrder.setText(QCoreApplication.translate("StaffPage", u"View Orders", None))
        self.service.setText(QCoreApplication.translate("StaffPage", u"Service", None))
        self.logOut.setText(QCoreApplication.translate("StaffPage", u"Log Out", None))
        self.productSearch.setPlaceholderText(QCoreApplication.translate("StaffPage", u"Search", None))
        ___qtablewidgetitem = self.inventoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StaffPage", u"Category", None));
        ___qtablewidgetitem1 = self.inventoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StaffPage", u"Brand", None));
        ___qtablewidgetitem2 = self.inventoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StaffPage", u"Name", None));
        ___qtablewidgetitem3 = self.inventoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StaffPage", u"Price", None));
        ___qtablewidgetitem4 = self.inventoryTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StaffPage", u"Quantity", None));
        ___qtablewidgetitem5 = self.inventoryTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StaffPage", u"Actions", None));
        self.staffSearch.setPlaceholderText(QCoreApplication.translate("StaffPage", u"Search", None))
        ___qtablewidgetitem6 = self.staffTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("StaffPage", u"First Name", None));
        ___qtablewidgetitem7 = self.staffTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("StaffPage", u"Last Name", None));
        ___qtablewidgetitem8 = self.staffTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("StaffPage", u"Mobile Number", None));
        ___qtablewidgetitem9 = self.staffTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("StaffPage", u"Address", None));
        ___qtablewidgetitem10 = self.staffTable.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("StaffPage", u"Date Hired", None));
        ___qtablewidgetitem11 = self.purchaseHistoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("StaffPage", u"Date", None));
        ___qtablewidgetitem12 = self.purchaseHistoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("StaffPage", u"Customer", None));
        ___qtablewidgetitem13 = self.purchaseHistoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("StaffPage", u"Actions", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StaffPage", u"Purchase History", None))
        ___qtablewidgetitem14 = self.serviceHistory.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("StaffPage", u"Date", None));
        ___qtablewidgetitem15 = self.serviceHistory.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("StaffPage", u"Customer", None));
        ___qtablewidgetitem16 = self.serviceHistory.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("StaffPage", u"Technician", None));
        ___qtablewidgetitem17 = self.serviceHistory.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("StaffPage", u"Device Type", None));
        ___qtablewidgetitem18 = self.serviceHistory.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("StaffPage", u"Service Type", None));
        ___qtablewidgetitem19 = self.serviceHistory.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("StaffPage", u"Total", None));
        ___qtablewidgetitem20 = self.serviceHistory.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("StaffPage", u"Status", None));
        ___qtablewidgetitem21 = self.serviceHistory.horizontalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("StaffPage", u"Actions", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StaffPage", u"Service History", None))
    # retranslateUi

