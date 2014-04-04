# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fly/eric/config.ui'
#
# Created: Thu Apr  3 14:54:09 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
        Dialog_config.setWindowTitle(QtGui.QApplication.translate("Dialog_config", "Select dump", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_config", "Wikipedia dump", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add.setText(QtGui.QApplication.translate("Dialog_config", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_del.setText(QtGui.QApplication.translate("Dialog_config", "Remove", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_config = QtGui.QDialog()
    ui = Ui_Dialog_config()
    ui.setupUi(Dialog_config)
    Dialog_config.show()
    sys.exit(app.exec_())

