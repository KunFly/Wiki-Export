# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fly\Documents\GitHub\Wiki-Export\about.ui'
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
        Form_about.setWindowTitle(_translate("Form_about", "About", None))
        self.label_5.setText(_translate("Form_about", "<html><head/><body><p align=\"center\">Wiki Export Tool version: 1.0</p><p align=\"center\">Copyright © 2014 CoMeRe.org All Rights Reserved.</p><p align=\"center\">Site: <a href=\"http://www.comere.org\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.comere.org</span></a></p><p align=\"center\">Powered By Kun JIN - <a href=\"http://www.flykun.ccom\"><span style=\" text-decoration: underline; color:#0000ff;\">flykun.com</span></a></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_about = QtGui.QWidget()
    ui = Ui_Form_about()
    ui.setupUi(Form_about)
    Form_about.show()
    sys.exit(app.exec_())

