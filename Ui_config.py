# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fly\Documents\GitHub\Wiki-Export\config.ui'
#
# Created: Sat Apr 05 21:45:37 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_config(object):
    def setupUi(self, Dialog_config):
        Dialog_config.setObjectName(_fromUtf8("Dialog_config"))
        Dialog_config.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Dialog_config)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog_config)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_add = QtGui.QPushButton(Dialog_config)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_del = QtGui.QPushButton(Dialog_config)
        self.pushButton_del.setObjectName(_fromUtf8("pushButton_del"))
        self.horizontalLayout.addWidget(self.pushButton_del)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.listWidget_dump = QtGui.QListWidget(Dialog_config)
        self.listWidget_dump.setObjectName(_fromUtf8("listWidget_dump"))
        self.gridLayout.addWidget(self.listWidget_dump, 1, 0, 1, 2)
        self.buttonBox_final = QtGui.QDialogButtonBox(Dialog_config)
        self.buttonBox_final.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_final.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_final.setObjectName(_fromUtf8("buttonBox_final"))
        self.gridLayout.addWidget(self.buttonBox_final, 2, 0, 1, 1)

        self.retranslateUi(Dialog_config)
        QtCore.QObject.connect(self.buttonBox_final, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_config.accept)
        QtCore.QObject.connect(self.buttonBox_final, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_config.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_config)

    def retranslateUi(self, Dialog_config):
        Dialog_config.setWindowTitle(_translate("Dialog_config", "Select dump", None))
        self.label.setText(_translate("Dialog_config", "Wikipedia dump", None))
        self.pushButton_add.setText(_translate("Dialog_config", "Add", None))
        self.pushButton_del.setText(_translate("Dialog_config", "Remove", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_config = QtGui.QDialog()
    ui = Ui_Dialog_config()
    ui.setupUi(Dialog_config)
    Dialog_config.show()
    sys.exit(app.exec_())

