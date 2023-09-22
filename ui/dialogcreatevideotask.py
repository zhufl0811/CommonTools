# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogcreatevideotask.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogCreateVideoTask(object):
    def setupUi(self, DialogCreateVideoTask):
        if not DialogCreateVideoTask.objectName():
            DialogCreateVideoTask.setObjectName(u"DialogCreateVideoTask")
        DialogCreateVideoTask.resize(733, 719)
        self.groupBox_2 = QGroupBox(DialogCreateVideoTask)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 260, 641, 91))
        self.checkBoxOpenResize = QCheckBox(self.groupBox_2)
        self.checkBoxOpenResize.setObjectName(u"checkBoxOpenResize")
        self.checkBoxOpenResize.setGeometry(QRect(430, 0, 51, 16))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 421, 56))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_14.addWidget(self.label_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBoxKeepRatioYes = QCheckBox(self.layoutWidget)
        self.checkBoxKeepRatioYes.setObjectName(u"checkBoxKeepRatioYes")

        self.horizontalLayout_9.addWidget(self.checkBoxKeepRatioYes)

        self.checkBoxKeepRatioNo = QCheckBox(self.layoutWidget)
        self.checkBoxKeepRatioNo.setObjectName(u"checkBoxKeepRatioNo")

        self.horizontalLayout_9.addWidget(self.checkBoxKeepRatioNo)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 8)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_13.addWidget(self.label_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkBoxRatioHalf = QCheckBox(self.layoutWidget)
        self.checkBoxRatioHalf.setObjectName(u"checkBoxRatioHalf")

        self.horizontalLayout_12.addWidget(self.checkBoxRatioHalf)

        self.checkBoxRatioThree = QCheckBox(self.layoutWidget)
        self.checkBoxRatioThree.setObjectName(u"checkBoxRatioThree")

        self.horizontalLayout_12.addWidget(self.checkBoxRatioThree)

        self.checkBoxRatioQuarter = QCheckBox(self.layoutWidget)
        self.checkBoxRatioQuarter.setObjectName(u"checkBoxRatioQuarter")

        self.horizontalLayout_12.addWidget(self.checkBoxRatioQuarter)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEditCustomX = QLineEdit(self.layoutWidget)
        self.lineEditCustomX.setObjectName(u"lineEditCustomX")

        self.horizontalLayout_10.addWidget(self.lineEditCustomX)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.lineEditCustomY = QLineEdit(self.layoutWidget)
        self.lineEditCustomY.setObjectName(u"lineEditCustomY")

        self.horizontalLayout_10.addWidget(self.lineEditCustomY)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13.setStretch(0, 2)
        self.horizontalLayout_13.setStretch(1, 5)
        self.horizontalLayout_13.setStretch(2, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.layoutWidget_3 = QWidget(DialogCreateVideoTask)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(470, 540, 158, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCancelCreateTask = QPushButton(self.layoutWidget_3)
        self.btnCancelCreateTask.setObjectName(u"btnCancelCreateTask")

        self.horizontalLayout.addWidget(self.btnCancelCreateTask)

        self.btnConfirmCreateTask = QPushButton(self.layoutWidget_3)
        self.btnConfirmCreateTask.setObjectName(u"btnConfirmCreateTask")

        self.horizontalLayout.addWidget(self.btnConfirmCreateTask)

        self.layoutWidget_4 = QWidget(DialogCreateVideoTask)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 20, 641, 61))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label = QLabel(self.layoutWidget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_16.addWidget(self.label)

        self.lineEditVideoSrc = QLineEdit(self.layoutWidget_4)
        self.lineEditVideoSrc.setObjectName(u"lineEditVideoSrc")

        self.horizontalLayout_16.addWidget(self.lineEditVideoSrc)

        self.btnSelectSrc = QPushButton(self.layoutWidget_4)
        self.btnSelectSrc.setObjectName(u"btnSelectSrc")

        self.horizontalLayout_16.addWidget(self.btnSelectSrc)

        self.horizontalLayout_16.setStretch(0, 3)
        self.horizontalLayout_16.setStretch(1, 18)
        self.horizontalLayout_16.setStretch(2, 5)

        self.horizontalLayout_18.addLayout(self.horizontalLayout_16)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_2 = QLabel(self.layoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_17.addWidget(self.label_2)

        self.lineEditVideoDst = QLineEdit(self.layoutWidget_4)
        self.lineEditVideoDst.setObjectName(u"lineEditVideoDst")

        self.horizontalLayout_17.addWidget(self.lineEditVideoDst)

        self.btnSelectDst = QPushButton(self.layoutWidget_4)
        self.btnSelectDst.setObjectName(u"btnSelectDst")

        self.horizontalLayout_17.addWidget(self.btnSelectDst)

        self.btnUseSrc = QPushButton(self.layoutWidget_4)
        self.btnUseSrc.setObjectName(u"btnUseSrc")

        self.horizontalLayout_17.addWidget(self.btnUseSrc)

        self.horizontalLayout_17.setStretch(0, 2)
        self.horizontalLayout_17.setStretch(1, 10)
        self.horizontalLayout_17.setStretch(2, 3)
        self.horizontalLayout_17.setStretch(3, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.groupBox_3 = QGroupBox(DialogCreateVideoTask)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 370, 641, 71))
        self.checkBoxFpsOpen = QCheckBox(self.groupBox_3)
        self.checkBoxFpsOpen.setObjectName(u"checkBoxFpsOpen")
        self.checkBoxFpsOpen.setGeometry(QRect(430, 0, 51, 16))
        self.layoutWidget1 = QWidget(self.groupBox_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 131, 22))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_19.addWidget(self.label_17)

        self.spinBoxToFps = QSpinBox(self.layoutWidget1)
        self.spinBoxToFps.setObjectName(u"spinBoxToFps")
        self.spinBoxToFps.setMinimum(1)
        self.spinBoxToFps.setMaximum(500)

        self.horizontalLayout_19.addWidget(self.spinBoxToFps)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_19.addWidget(self.label_18)

        self.groupBox = QGroupBox(DialogCreateVideoTask)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 90, 641, 81))
        self.layoutWidget_2 = QWidget(self.groupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 20, 411, 52))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(24)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.labelResolution = QLabel(self.layoutWidget_2)
        self.labelResolution.setObjectName(u"labelResolution")

        self.horizontalLayout_2.addWidget(self.labelResolution)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.labelFps = QLabel(self.layoutWidget_2)
        self.labelFps.setObjectName(u"labelFps")

        self.horizontalLayout_3.addWidget(self.labelFps)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.labelFormat = QLabel(self.layoutWidget_2)
        self.labelFormat.setObjectName(u"labelFormat")

        self.horizontalLayout_4.addWidget(self.labelFormat)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7.setStretch(0, 6)
        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(24)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.labelBitRate = QLabel(self.layoutWidget_2)
        self.labelBitRate.setObjectName(u"labelBitRate")

        self.horizontalLayout_5.addWidget(self.labelBitRate)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_6.addWidget(self.label_15)

        self.labelFileSize = QLabel(self.layoutWidget_2)
        self.labelFileSize.setObjectName(u"labelFileSize")

        self.horizontalLayout_6.addWidget(self.labelFileSize)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalLayout.setStretch(1, 6)
        self.groupBox_4 = QGroupBox(DialogCreateVideoTask)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 180, 641, 61))
        self.checkBoxFormatOpen = QCheckBox(self.groupBox_4)
        self.checkBoxFormatOpen.setObjectName(u"checkBoxFormatOpen")
        self.checkBoxFormatOpen.setGeometry(QRect(430, 0, 51, 16))
        self.layoutWidget_5 = QWidget(self.groupBox_4)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 20, 181, 22))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget_5)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_20.addWidget(self.label_19)

        self.comboBoxChangeFormat = QComboBox(self.layoutWidget_5)
        self.comboBoxChangeFormat.setObjectName(u"comboBoxChangeFormat")

        self.horizontalLayout_20.addWidget(self.comboBoxChangeFormat)

        self.groupBox_5 = QGroupBox(DialogCreateVideoTask)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 490, 371, 151))
        self.groupBox_5.setCheckable(True)
        self.gridLayout = QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.groupBox_5)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(True)
        self.pushButton_7.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox_5)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_11, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)


        self.retranslateUi(DialogCreateVideoTask)

        QMetaObject.connectSlotsByName(DialogCreateVideoTask)
    # setupUi

    def retranslateUi(self, DialogCreateVideoTask):
        DialogCreateVideoTask.setWindowTitle(QCoreApplication.translate("DialogCreateVideoTask", u"\u521b\u5efa\u89c6\u9891\u4efb\u52a1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogCreateVideoTask", u"\u7f29\u653e", None))
        self.checkBoxOpenResize.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u5f00\u542f", None))
        self.label_3.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u4fdd\u6301\u7eb5\u6a2a\u6bd4", None))
        self.checkBoxKeepRatioYes.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u662f", None))
        self.checkBoxKeepRatioNo.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u5426", None))
        self.label_4.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u6bd4\u4f8b", None))
        self.checkBoxRatioHalf.setText(QCoreApplication.translate("DialogCreateVideoTask", u"1/2", None))
        self.checkBoxRatioThree.setText(QCoreApplication.translate("DialogCreateVideoTask", u"1/3", None))
        self.checkBoxRatioQuarter.setText(QCoreApplication.translate("DialogCreateVideoTask", u"1/4", None))
        self.label_5.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u81ea\u5b9a\u4e49", None))
        self.label_16.setText(QCoreApplication.translate("DialogCreateVideoTask", u"x", None))
        self.btnCancelCreateTask.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u53d6\u6d88", None))
        self.btnConfirmCreateTask.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u89c6\u9891", None))
        self.btnSelectSrc.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.btnSelectDst.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u9009\u62e9", None))
        self.btnUseSrc.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u6e90\u6587\u4ef6\u5939", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DialogCreateVideoTask", u"\u8c03\u6574\u5e27\u7387", None))
        self.checkBoxFpsOpen.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u5f00\u542f", None))
        self.label_17.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u8c03\u6574\u5230", None))
        self.label_18.setText(QCoreApplication.translate("DialogCreateVideoTask", u"fps", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogCreateVideoTask", u"\u89c6\u9891\u4fe1\u606f", None))
        self.label_6.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u5206\u8fa8\u7387", None))
        self.labelResolution.setText(QCoreApplication.translate("DialogCreateVideoTask", u"-*-", None))
        self.label_7.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u5e27\u7387", None))
        self.labelFps.setText(QCoreApplication.translate("DialogCreateVideoTask", u"n fps", None))
        self.label_10.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u683c\u5f0f", None))
        self.labelFormat.setText(QCoreApplication.translate("DialogCreateVideoTask", u"mp4", None))
        self.label_12.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u7801\u7387", None))
        self.labelBitRate.setText(QCoreApplication.translate("DialogCreateVideoTask", u"x mbps", None))
        self.label_15.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u5927\u5c0f", None))
        self.labelFileSize.setText(QCoreApplication.translate("DialogCreateVideoTask", u"xxx mb", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("DialogCreateVideoTask", u"\u683c\u5f0f\u8f6c\u6362", None))
        self.checkBoxFormatOpen.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u5f00\u542f", None))
        self.label_19.setText(QCoreApplication.translate("DialogCreateVideoTask", u"\u8f6c\u6362\u4e3a", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("DialogCreateVideoTask", u"Buttons", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("DialogCreateVideoTask", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("DialogCreateVideoTask", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("DialogCreateVideoTask", u"Checked", None))
        self.pushButton_6.setText(QCoreApplication.translate("DialogCreateVideoTask", u"Disabled", None))
        self.pushButton_7.setText(QCoreApplication.translate("DialogCreateVideoTask", u"Disable checked", None))
        self.pushButton_11.setText(QCoreApplication.translate("DialogCreateVideoTask", u"Flat", None))
        self.pushButton_5.setText(QCoreApplication.translate("DialogCreateVideoTask", u"Flat checkeable", None))
        self.pushButton_4.setText(QCoreApplication.translate("DialogCreateVideoTask", u"Flat disabled", None))
    # retranslateUi

