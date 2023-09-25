# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_resize_task_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(804, 71)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 0, 741, 71))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelFileName = QLabel(self.layoutWidget)
        self.labelFileName.setObjectName(u"labelFileName")
        self.labelFileName.setLineWidth(3)
        self.labelFileName.setAlignment(Qt.AlignCenter)
        self.labelFileName.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelFileName)

        self.labelVideoInfo = QLabel(self.layoutWidget)
        self.labelVideoInfo.setObjectName(u"labelVideoInfo")
        self.labelVideoInfo.setAlignment(Qt.AlignCenter)
        self.labelVideoInfo.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelVideoInfo)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.checkBoxKeepRatio = QCheckBox(self.layoutWidget)
        self.checkBoxKeepRatio.setObjectName(u"checkBoxKeepRatio")

        self.horizontalLayout_3.addWidget(self.checkBoxKeepRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBoxRatio = QComboBox(self.layoutWidget)
        self.comboBoxRatio.setObjectName(u"comboBoxRatio")

        self.horizontalLayout.addWidget(self.comboBoxRatio)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditResizeW = QLineEdit(self.layoutWidget)
        self.lineEditResizeW.setObjectName(u"lineEditResizeW")

        self.horizontalLayout_2.addWidget(self.lineEditResizeW)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEditResizeH = QLineEdit(self.layoutWidget)
        self.lineEditResizeH.setObjectName(u"lineEditResizeH")

        self.horizontalLayout_2.addWidget(self.lineEditResizeH)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.pgsBar = QProgressBar(self.layoutWidget)
        self.pgsBar.setObjectName(u"pgsBar")
        self.pgsBar.setValue(24)

        self.horizontalLayout_3.addWidget(self.pgsBar)

        self.btnStart = QPushButton(self.layoutWidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout_3.addWidget(self.btnStart)

        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 3)
        self.horizontalLayout_3.setStretch(4, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelFileName.setText(QCoreApplication.translate("Form", u"filename", None))
        self.labelVideoInfo.setText(QCoreApplication.translate("Form", u"filename", None))
        self.checkBoxKeepRatio.setText(QCoreApplication.translate("Form", u"\u4fdd\u6301\u7eb5\u6a2a\u6bd4", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7f29\u653e\u6bd4", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"x", None))
        self.btnStart.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
    # retranslateUi

