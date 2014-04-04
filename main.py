#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""
__author__ = "JIN Kun"
__copyright__   = "Copyright © 2014 CoMeRe.org All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "JIN Kun"
__email__ = "kun.jin@univ-bpclermont.fr"

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtGui,  QtCore

from Ui_main import Ui_Wiki_Tool
from config import Dialog_config
from about import Form_about

from lxml import etree
from bz2 import BZ2File as b2f

import marshal
import os.path

from flykun.wiki import pagename

listArticle = []

class MainWindow(QMainWindow, Ui_Wiki_Tool):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor: 
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pool = []
        self.list_dump = QtCore.QStringList()
        
        
    @pyqtSignature("bool")
    def on_actionConfigure_triggered(self, checked):
        """
        Slot documentation goes here.
        """
        self.openConfig = Dialog_config(self.list_dump)
        self.openConfig.show()
        self.list_dump = self.openConfig.stringlist
    
    @pyqtSignature("bool")
    def on_actionAbout_triggered(self, checked):
        """
        Slot documentation goes here.
        """
        self.openAbout = Form_about()
        self.openAbout.show()
        

#------ Add article name --------
    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        Add article
        """
        self.textEdit_articlelist.append(self.lineEdit_articlename.text())
        self.lineEdit_articlename.clear()
    
    @pyqtSignature("")
    def on_lineEdit_articlename_returnPressed(self):
        """
        Add article
        """
        self.textEdit_articlelist.append(self.lineEdit_articlename.text())
        self.lineEdit_articlename.clear()


#----- Prepare for starting ------
    def get_pagename(self):
        
        list_pagename = []
        titlelistString = str(self.textEdit_articlelist.toPlainText().toUtf8()).decode("utf-8")
        for x in titlelistString.strip().split("\n"):
            if x:
                t = pagename.PageName(x)
                if self.checkBox_main.isChecked():
                    list_pagename.extend(t.get_page_name())
                if self.checkBox_talk.isChecked():
                    list_pagename.extend(t.get_talk_name())
                if self.checkBox_othertalk.isChecked():
                    list_pagename.extend(t.get_othertalks_name())
                if self.checkBox_archives.isChecked():
                    list_pagename.extend(t.get_archive_name())
        return list_pagename
        
    def addText(self, text,  result = False):
        """
        Add text
        """
        if result == True:
            self.textBrowser_result.append(text)
        else:
            self.textBrowser_status.append(text)
            
    def finished(self):
        """
        when finish, change text of button
        """
        for n, thread in enumerate(self.pool):
            thread.stop()
            text = "Thread %s Processus was stopped!"%str(n+1)
            self.addText(text)
        self.actionRun.setText("Run")
        
    @pyqtSignature("bool")      
    def on_actionRun_triggered(self, checked):
        """
        Slot documentation goes here.
        """
        global listArticle
        listArticle = self.get_pagename()
        if self.actionRun.text() == "Run":
            if len(listArticle):
                self.actionRun.setText("Stop")
                for i,  dump in enumerate(self.list_dump):
                    self.pool.append(MyThread(dump, i + 1))
                    self.pool[-1].start()
                    self.connect(self.pool[-1], QtCore.SIGNAL("msg"), self.addText)
                    self.connect(self.pool[-1], QtCore.SIGNAL("end"), self.finished) 
                self.finished()
            else:
                msgstring = "No page to find"
                self.addText(msgstring)
        else:
            self.finished()

class MyThread(QtCore.QThread):
    def __init__(self, dump, n,  parent=None):
        super(self.__class__, self).__init__(parent)    
        self.threadnum = n        
        
    def run(self):
        self.doRecv = True
        while self.doRecv:
            self.findPages()

    def stop(self):
        self.doRecv = False

    def findPages(self):
        """
        Find cible pages, when found, deletet from list, and print out the page.
        """        
        global listArticle
        ns = "http://www.mediawiki.org/xml/export-0.8/"
        node_find = "{%s}%s"%(ns,"page")
        status = 1
        if len(listArticle) != 0 and listArticle[0] != "":  
            if len(listArticle) == 1:
                msgstring = "%s page to find"%len(listArticle)
            else: #if len(listArticle) != 1
                msgstring = "%s pages to find"%len(listArticle)
            self.emit(QtCore.SIGNAL("msg"),msgstring)
            msgstring = "Looking in dump:%s "%self.dump
            self.emit(QtCore.SIGNAL("msg"),msgstring)
            if os.path.splitext(str(self.dump))[1]  == ".bz2":
                fp = b2f(self.dump,"r")
            else:
                fp = open(self.dump, "r")
            tree = etree.iterparse(fp,events=("end",), tag=node_find)
            for event, elem in tree:
                status += 1
                if status % 1000 == 0:
                    msgstring = "Thread %s, Alread found %s pages"%(self.threadnum,status)
                    self.emit(QtCore.SIGNAL("msg"),msgstring)
                if elem[0].text in listArticle:
                    namefile = elem[0].text.replace("/", "-")
                    namefile = namefile.replace(":", "-")
                    OUTF = open("%s.xml"%namefile, "w")
                    OUTF.write(etree.tostring(elem, encoding="utf-8",
                            pretty_print=True))
                    OUTF.close()
                    try:
                        listArticle.remove(elem[0].text)
                        msgstring = "Thread %s found page:%s"%(self.threadnum,elem[0].text)
                        self.emit(QtCore.SIGNAL("msg"),msgstring)
                        self.emit(QtCore.SIGNAL("msg"),msgstring, True)
                    except:
                        pass
                    if len(listArticle) != 0:
                        if len(listArticle) == 1:
                            msgstring = "There was still %s page, please wait... "%len(listArticle)
                        else: #if len(listArticle) == 1
                            msgstring = "There was still %s pages, please wait... "%len(listArticle)
                        self.emit(QtCore.SIGNAL("msg"),msgstring)
                    else: #找到所有的页面后，退出
                        msgstring = "Found all pages, work end"
                        self.emit(QtCore.SIGNAL("msg"),msgstring)
                        self.emit(QtCore.SIGNAL("end"),msgstring)
                        self.doRecv = False #找到所有的页面后，将结束
                        break
                if self.doRecv == False: #在按下停止按钮后，跳出
                    break
                elem.clear()
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
            del tree
            if len(listArticle) != 0: #还有页面没找完，但是DUMP的历遍已经结束
                msgstring = "Finish to find all page in %s, there was still %s page to find."%(self.dump, len(listArticle))
                self.emit(QtCore.SIGNAL("msg"),msgstring)
                msgstring = "Thread %s end"%(self.threadnum)
                self.emit(QtCore.SIGNAL("msg"),msgstring)
                #self.emit(QtCore.SIGNAL("end"),msgstring)
        self.doRecv = False #整个程序跑完后
