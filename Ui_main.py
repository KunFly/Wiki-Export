# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fly\Documents\GitHub\Wiki-Export\main.ui'
#
# Created: Sat Apr 05 21:45:36 2014
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

class Ui_Wiki_Tool(object):
    def setupUi(self, Wiki_Tool):
        Wiki_Tool.setObjectName(_fromUtf8("Wiki_Tool"))
        Wiki_Tool.resize(691, 659)
        self.centralWidget = QtGui.QWidget(Wiki_Tool)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_articlename = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_articlename.setText(_fromUtf8(""))
        self.lineEdit_articlename.setObjectName(_fromUtf8("lineEdit_articlename"))
        self.horizontalLayout.addWidget(self.lineEdit_articlename)
        self.pushButton_add = QtGui.QPushButton(self.centralWidget)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_clear = QtGui.QPushButton(self.centralWidget)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.textEdit_articlelist = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_articlelist.setObjectName(_fromUtf8("textEdit_articlelist"))
        self.gridLayout.addWidget(self.textEdit_articlelist, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.checkBox_main = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_main.setAcceptDrops(False)
        self.checkBox_main.setChecked(True)
        self.checkBox_main.setObjectName(_fromUtf8("checkBox_main"))
        self.verticalLayout.addWidget(self.checkBox_main)
        self.checkBox_talk = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_talk.setObjectName(_fromUtf8("checkBox_talk"))
        self.verticalLayout.addWidget(self.checkBox_talk)
        self.checkBox_othertalk = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_othertalk.setObjectName(_fromUtf8("checkBox_othertalk"))
        self.verticalLayout.addWidget(self.checkBox_othertalk)
        self.checkBox_archives = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_archives.setObjectName(_fromUtf8("checkBox_archives"))
        self.verticalLayout.addWidget(self.checkBox_archives)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.tabWidget_status = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget_status.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_status.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_status.setAutoFillBackground(False)
        self.tabWidget_status.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidget_status.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_status.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_status.setObjectName(_fromUtf8("tabWidget_status"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textBrowser_status = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser_status.setAutoFillBackground(False)
        self.textBrowser_status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_status.setAcceptRichText(True)
        self.textBrowser_status.setObjectName(_fromUtf8("textBrowser_status"))
        self.gridLayout_2.addWidget(self.textBrowser_status, 0, 0, 1, 1)
        self.tabWidget_status.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.textBrowser_result = QtGui.QTextBrowser(self.tab_4)
        self.textBrowser_result.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser_result.setAutoFillBackground(False)
        self.textBrowser_result.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_result.setObjectName(_fromUtf8("textBrowser_result"))
        self.gridLayout_3.addWidget(self.textBrowser_result, 0, 0, 1, 1)
        self.tabWidget_status.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_status, 2, 0, 1, 2)
        Wiki_Tool.setCentralWidget(self.centralWidget)
        self.toolBar = QtGui.QToolBar(Wiki_Tool)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Wiki_Tool.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRun = QtGui.QAction(Wiki_Tool)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionConfigure = QtGui.QAction(Wiki_Tool)
        self.actionConfigure.setObjectName(_fromUtf8("actionConfigure"))
        self.actionAbout = QtGui.QAction(Wiki_Tool)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionConfigure)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(Wiki_Tool)
        self.tabWidget_status.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit_articlelist.clear)
        QtCore.QMetaObject.connectSlotsByName(Wiki_Tool)

    def retranslateUi(self, Wiki_Tool):
        Wiki_Tool.setWindowTitle(_translate("Wiki_Tool", "Wiki Export Tool", None))
        self.pushButton_add.setText(_translate("Wiki_Tool", "Add", None))
        self.pushButton_clear.setText(_translate("Wiki_Tool", "Clear", None))
        self.label.setText(_translate("Wiki_Tool", "Select Page", None))
        self.checkBox_main.setText(_translate("Wiki_Tool", "Main", None))
        self.checkBox_talk.setText(_translate("Wiki_Tool", "Talk", None))
        self.checkBox_othertalk.setText(_translate("Wiki_Tool", "Other Talk", None))
        self.checkBox_archives.setText(_translate("Wiki_Tool", "Archive", None))
        self.textBrowser_status.setHtml(_translate("Wiki_Tool", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\';\">Press F5 to start program</span></p></body></html>", None))
        self.tabWidget_status.setTabText(self.tabWidget_status.indexOf(self.tab_3), _translate("Wiki_Tool", "Status", None))
        self.textBrowser_result.setHtml(_translate("Wiki_Tool", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>", None))
        self.tabWidget_status.setTabText(self.tabWidget_status.indexOf(self.tab_4), _translate("Wiki_Tool", "Result", None))
        self.toolBar.setWindowTitle(_translate("Wiki_Tool", "toolBar", None))
        self.actionRun.setText(_translate("Wiki_Tool", "Run", None))
        self.actionRun.setToolTip(_translate("Wiki_Tool", "Run", None))
        self.actionRun.setShortcut(_translate("Wiki_Tool", "F5", None))
        self.actionConfigure.setText(_translate("Wiki_Tool", "Configure", None))
        self.actionConfigure.setShortcut(_translate("Wiki_Tool", "Ctrl+O", None))
        self.actionAbout.setText(_translate("Wiki_Tool", "About", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Wiki_Tool = QtGui.QMainWindow()
    ui = Ui_Wiki_Tool()
    ui.setupUi(Wiki_Tool)
    Wiki_Tool.show()
    sys.exit(app.exec_())

