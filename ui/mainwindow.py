# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(10, 10, 161, 710))
        font = QFont()
        font.setPointSize(16)
        self.toolBox.setFont(font)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setLineWidth(5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 161, 578))
        self.gridLayout_14 = QGridLayout(self.page)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.btnNavVideoResize = QPushButton(self.page)
        self.btnNavVideoResize.setObjectName(u"btnNavVideoResize")
        self.btnNavVideoResize.setMaximumSize(QSize(80, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.btnNavVideoResize.setFont(font1)

        self.gridLayout_14.addWidget(self.btnNavVideoResize, 0, 0, 1, 1)

        self.btnNavVideoAudio = QPushButton(self.page)
        self.btnNavVideoAudio.setObjectName(u"btnNavVideoAudio")
        self.btnNavVideoAudio.setMaximumSize(QSize(80, 30))
        self.btnNavVideoAudio.setFont(font1)

        self.gridLayout_14.addWidget(self.btnNavVideoAudio, 2, 0, 1, 1)

        self.btnNavVideoFormat = QPushButton(self.page)
        self.btnNavVideoFormat.setObjectName(u"btnNavVideoFormat")
        self.btnNavVideoFormat.setMaximumSize(QSize(80, 30))
        self.btnNavVideoFormat.setFont(font1)

        self.gridLayout_14.addWidget(self.btnNavVideoFormat, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.toolBox.addItem(self.page, u">\u89c6\u9891\u5904\u7406")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 161, 578))
        self.gridLayout_9 = QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.toolBox.addItem(self.page_3, u">\u56fe\u50cf\u5904\u7406")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 161, 578))
        self.gridLayout_21 = QGridLayout(self.page_4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.toolBox.addItem(self.page_4, u">\u811a\u672c")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 0, 840, 720))
        self.pageVideoResize = QWidget()
        self.pageVideoResize.setObjectName(u"pageVideoResize")
        self.widget = QWidget(self.pageVideoResize)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 801, 701))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCreateVideoTask = QPushButton(self.widget)
        self.btnCreateVideoTask.setObjectName(u"btnCreateVideoTask")
        self.btnCreateVideoTask.setFont(font)

        self.horizontalLayout.addWidget(self.btnCreateVideoTask)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.pageVideoResize)
        self.pageVideoFormat = QWidget()
        self.pageVideoFormat.setObjectName(u"pageVideoFormat")
        self.pushButton = QPushButton(self.pageVideoFormat)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 400, 75, 23))
        self.stackedWidget.addWidget(self.pageVideoFormat)
        self.pageVideo2Audio = QWidget()
        self.pageVideo2Audio.setObjectName(u"pageVideo2Audio")
        self.pushButton_2 = QPushButton(self.pageVideo2Audio)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(380, 330, 75, 23))
        self.stackedWidget.addWidget(self.pageVideo2Audio)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(9)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnNavVideoResize.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7f29\u653e", None))
        self.btnNavVideoAudio.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u97f3\u9891", None))
        self.btnNavVideoFormat.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u8f6c\u6362", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u">\u89c6\u9891\u5904\u7406", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u">\u56fe\u50cf\u5904\u7406", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u">\u811a\u672c", None))
        self.btnCreateVideoTask.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u89c6\u9891", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u8f6c\u6362", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u97f3\u9891", None))
    # retranslateUi

