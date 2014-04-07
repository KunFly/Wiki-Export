# -*- coding: utf-8 -*-

"""
Module implementing Dialog_config.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtGui,  QtCore

from Ui_config import Ui_Dialog_config

class Dialog_config(QDialog, Ui_Dialog_config):
    """
    Class documentation goes here.
    """
    def __init__(self, stringlist, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.stringlist = QtCore.QStringList()
        self.listWidget_dump.addItems(stringlist)
    
    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        list_dump = QtGui.QFileDialog.getOpenFileNames(
                    self,
                    "Select Dumps", "", "Dump files(*.xml *.bz2)")
        self.listWidget_dump.addItems (list_dump)
    
    @pyqtSignature("")
    def on_pushButton_del_clicked(self):
        """
        Slot documentation goes here.
        """
        row = self.listWidget_dump.currentRow()
        item = self.listWidget_dump.item(row)
        if item is None:
            return
        else:
            item = self.listWidget_dump.takeItem(row)
            del item
    
    @pyqtSignature("")
    def on_buttonBox_final_accepted(self):
        """
        Slot documentation goes here.
        """
        for row in range(self.listWidget_dump.count()):
            self.stringlist.append(self.listWidget_dump.item(row).text())
#        self.emit(SIGNAL("acceptedList(QStringList)"), self.stringlist)
        QDialog.accept(self)
    
    @pyqtSignature("")
    def on_buttonBox_final_rejected(self):
        """
        Slot documentation goes here.
        """
        self.on_buttonBox_final_accepted()
