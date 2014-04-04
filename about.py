# -*- coding: utf-8 -*-

"""
Module implementing Form_about.
"""

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_about import Ui_Form_about

class Form_about(QWidget, Ui_Form_about):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
