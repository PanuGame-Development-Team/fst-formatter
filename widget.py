# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.log = QtWidgets.QTextEdit(Form)
        self.log.setGeometry(QtCore.QRect(30, 310, 540, 260))
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.eselectfolder = QtWidgets.QLineEdit(Form)
        self.eselectfolder.setGeometry(QtCore.QRect(210, 40, 310, 30))
        self.eselectfolder.setObjectName("eselectfolder")
        self.lselectfolder = QtWidgets.QLabel(Form)
        self.lselectfolder.setGeometry(QtCore.QRect(30, 40, 180, 30))
        self.lselectfolder.setObjectName("lselectfolder")
        self.bselectfolder = QtWidgets.QPushButton(Form)
        self.bselectfolder.setGeometry(QtCore.QRect(520, 40, 50, 30))
        self.bselectfolder.setObjectName("bselectfolder")
        self.fileprogresstable = QtWidgets.QTableWidget(Form)
        self.fileprogresstable.setGeometry(QtCore.QRect(30, 90, 540, 170))
        self.fileprogresstable.setObjectName("fileprogresstable")
        self.fileprogresstable.setColumnCount(5)
        self.fileprogresstable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fileprogresstable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileprogresstable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileprogresstable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileprogresstable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileprogresstable.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 290, 66, 19))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.lselectfolder.setText(_translate("Form", "请选择要处理的文件夹"))
        self.bselectfolder.setText(_translate("Form", "..."))
        item = self.fileprogresstable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.fileprogresstable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "文件"))
        item = self.fileprogresstable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "类型"))
        item = self.fileprogresstable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "进度"))
        item = self.fileprogresstable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "状态"))
        self.label.setText(_translate("Form", "日志"))
