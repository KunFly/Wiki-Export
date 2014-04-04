from PyQt4 import QtGui
from main import MainWindow


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
