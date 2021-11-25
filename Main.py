from Ui_win import Ui_MainWindow
from methods import meth
from PyQt5.QtWidgets import QLabel, QMainWindow,QMessageBox,QApplication, QVBoxLayout, QWidget
import sys


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lex_button.clicked.connect(lambda:meth.pushlex(meth))
        self.ui.synt_button.clicked.connect(lambda:meth.pushsyn(meth))
        self.ui.bar_openfile.triggered.connect(lambda:meth.openfile(meth))
        self.ui.bar_newfile.triggered.connect(lambda:meth.newfile(meth))
        self.ui.bar_savefile.triggered.connect(lambda:meth.save(meth))
        self.ui.bar_copy.triggered.connect(lambda:meth.ctrl_c(meth))
        self.ui.bar_cut.triggered.connect(lambda:meth.cut(meth))
        self.ui.bar_paste.triggered.connect(lambda:meth.paste(meth))
        self.ui.bar_new_window.triggered.connect(lambda:meth.neww(MainWindow()))  
    def closeEvent(self,event):
        if(meth.data!=self.ui.TInput.toPlainText()):
            rp= QMessageBox.question(self,'Close Window','Do you want to save',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if rp == QMessageBox.Yes:
                self.ui.save()
            event.accept()



        
if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        sys.exit(app.exec())