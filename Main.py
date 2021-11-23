from Ui_win import *
from methods import *
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
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