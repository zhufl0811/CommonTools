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
        Form.resize(804, 67)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 751, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelFileName = QLabel(self.widget)
        self.labelFileName.setObjectName(u"labelFileName")
        self.labelFileName.setLineWidth(3)
        self.labelFileName.setAlignment(Qt.AlignCenter)
        self.labelFileName.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.labelFileName)

        self.labelVideoInfo = QLabel(self.widget)
        self.labelVideoInfo.setObjectName(u"labelVideoInfo")
        self.labelVideoInfo.setAlignment(Qt.AlignCenter)
        self.labelVideoInfo.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.labelVideoInfo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBoxRatio = QComboBox(self.widget)
        self.comboBoxRatio.setObjectName(u"comboBoxRatio")

        self.horizontalLayout.addWidget(self.comboBoxRatio)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditResizeW = QLineEdit(self.widget)
        self.lineEditResizeW.setObjectName(u"lineEditResizeW")

        self.horizontalLayout_2.addWidget(self.lineEditResizeW)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEditResizeH = QLineEdit(self.widget)
        self.lineEditResizeH.setObjectName(u"lineEditResizeH")

        self.horizontalLayout_2.addWidget(self.lineEditResizeH)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.labelState = QLabel(self.widget)
        self.labelState.setObjectName(u"labelState")

        self.horizontalLayout_3.addWidget(self.labelState)

        self.btnStart = QPushButton(self.widget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout_3.addWidget(self.btnStart)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(6, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelFileName.setText(QCoreApplication.translate("Form", u"filename", None))
        self.labelVideoInfo.setText(QCoreApplication.translate("Form", u"filename", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7f29\u653e\u6bd4", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"x", None))
        self.labelState.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btnStart.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
    # retranslateUi

