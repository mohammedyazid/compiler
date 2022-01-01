from compiler import Ui_MainWindow
from methods import meth
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QApplication
import sys


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LEXICAL.clicked.connect(lambda:meth.pushlex(meth))
        self.ui.SYNTAX.clicked.connect(lambda:meth.pushsyn(meth))
        self.ui.actionOpen_File.triggered.connect(lambda:meth.openfile(meth))
        self.ui.actionNew_File.triggered.connect(lambda:meth.newfile(meth))
        self.ui.actionSave_File .triggered.connect(lambda:meth.save(meth))
        self.ui.actionCopy.triggered.connect(lambda:meth.ctrl_c(meth))
        self.ui.actionCut.triggered.connect(lambda:meth.cut(meth))
        self.ui.actionPaste.triggered.connect(lambda:meth.paste(meth))
        self.ui.actionNew_Windows.triggered.connect(lambda:meth.neww(MainWindow()))  
    def closeEvent(self,event):
        if(meth.data!=self.ui.INPUT.toPlainText()):
            rp= QMessageBox.question(self,'Close Window','Do you want to save',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if rp == QMessageBox.Yes:
                meth.save(meth)
            event.accept()



        
if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        sys.exit(app.exec())