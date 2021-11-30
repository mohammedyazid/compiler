from posixpath import join
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtCore import QDir
from Ui_win import Ui_MainWindow
import re,os
class meth():
    window=[]
    file_name=[]
    data=""
    def pushlex(self):
        print("Analyse Lexical")
        Ui_MainWindow.TInput.setText("")
    def pushsyn(self):
        print("Analyse Syntaxique")
        mail=Ui_MainWindow.TInput.toPlainText()
        line=0
        for line in open("ver.txt"):
            pattern = re.compile(line)
            for match in re.finditer(pattern, mail):
                Ui_MainWindow.TOutput.setText("Forme Valid")
            if re.search(pattern,mail) is None:
                Ui_MainWindow.TOutput.setText("Invalid Forme")
        # path = 'ver.txt'
        # with open(os.path.join(os.path.dirname(__file__), path), 'r') as input_file:
        #     data = input_file.read()
        # input_file.close()
        # txt = "The rain in Spain"
        # result = re.findall(data, txt)
        # print(data)
        #Ui_MainWindow.TOutput.append('|'.join(result))
        

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
                    Ui_MainWindow.TInput.setText(meth.data)
                    f.close()
            else:
                pass
        Ui_MainWindow.TOutput.append(self.path)
        
    def newfile(self):
        meth.file_name = QtWidgets.QFileDialog.getSaveFileName()
        file = open(meth.file_name[0],'w')
        text = ""
        file.write(text)
        file.close()
        Ui_MainWindow.TOutput.append("File Created")
    def save(self):
        file = open(meth.file_name[0],'w')
        text = Ui_MainWindow.TInput.toPlainText()
        file.write(text)
        file.close()
        Ui_MainWindow.TOutput.append("File Saved")
        print("File Saved")
    def ctrl_c(self):
        cp = QApplication.clipboard()
        cp.clear(mode=cp.Clipboard)
        cursor = Ui_MainWindow.TInput.textCursor()
        print(cursor.selectedText())
        cp.setText(cursor.selectedText(),mode = cp.Clipboard)
    def cut(self):
        cp = QApplication.clipboard()
        cp.clear(mode=cp.Clipboard)
        cursor = Ui_MainWindow.TInput.textCursor()
        print(cursor.selectedText())
        cp.setText(cursor.selectedText(),mode = cp.Clipboard)
        cursor.removeSelectedText()
    def paste(self):
        cp = QApplication.clipboard().text()
        Ui_MainWindow.TInput.insertPlainText(cp)
    def neww(window):
        meth.window.append(window) 
        window.show()
