# # from Ui_win import U
# from Main import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction, QMainWindow,QApplication,QFileDialog,QMessageBox
from PyQt5.QtCore import QDir
import sys
class meth():
    window=[]
    file_name=[]
    data=""
    def pushlex(self):
        print("Analyse Lexical")
    def pushsyn(self):
        print("Analyse Syntaxique")
    def openfile(self):
        dialog= QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            meth.file_name= dialog.selectedFiles()
            self.path = meth.file_name[0]

            if meth.file_name[0].endswith('.txt'):
                with open(meth.file_name[0],'r') as f:
                    meth.data= f.read()
                    self.TInput.setText(meth.data)
                    f.close()
            else:
                pass
        self.TOutput.append(self.path)
        
    def newfile(self):
        meth.file_name = QtWidgets.QFileDialog.getSaveFileName()
        file = open(meth.file_name[0],'w')
        text = ""
        file.write(text)
        file.close()
        self.TOutput.append("File Created")
    def save(self):
        file = open(meth.file_name[0],'w')
        text = self.TInput.toPlainText()
        file.write(text)
        file.close()
        self.TOutput.append("File Saved")
        print("File Saved")
    def ctrl_c(self):
        cp = QApplication.clipboard()
        cp.clear(mode=cp.Clipboard)
        cursor = self.TInput.textCursor()
        print(cursor.selectedText())
        cp.setText(cursor.selectedText(),mode = cp.Clipboard)
    def cut(self):
        cp = QApplication.clipboard()
        cp.clear(mode=cp.Clipboard)
        cursor = self.TInput.textCursor()
        print(cursor.selectedText())
        cp.setText(cursor.selectedText(),mode = cp.Clipboard)
        cursor.removeSelectedText()
    def paste(self):
        cp = QApplication.clipboard().text()
        self.TInput.insertPlainText(cp)
    def neww(window):
        meth.window.append(window) 
        window.show()
