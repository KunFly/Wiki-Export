# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fly/eric/about.ui'
#
# Created: Thu Apr  3 14:54:10 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form_about(object):
    def setupUi(self, Form_about):
        Form_about.setObjectName(_fromUtf8("Form_about"))
        Form_about.resize(365, 171)
        self.gridLayout = QtGui.QGridLayout(Form_about)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(Form_about)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.retranslateUi(Form_about)
        QtCore.QMetaObject.connectSlotsByName(Form_about)

    def retranslateUi(self, Form_about):
        Form_about.setWindowTitle(QtGui.QApplication.translate("Form_about", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form_about", "<html><head/><body><p align=\"center\">Wiki tools version: 1.0</p><p align=\"center\">Copyright © 2014 CoMeRe.org All Rights Reserved.</p><p align=\"center\">Site: <a href=\"http://www.comere.org\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.comere.org</span></a></p><p align=\"center\">Powered By Kun JIN - <a href=\"http://www.flykun.ccom\"><span style=\" text-decoration: underline; color:#0000ff;\">flykun.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_about = QtGui.QWidget()
    ui = Ui_Form_about()
    ui.setupUi(Form_about)
    Form_about.show()
    sys.exit(app.exec_())

