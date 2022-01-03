from posixpath import join
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtCore import QDir
from compiler import Ui_MainWindow
import re
import lexer
import Parser
import re,nltk
motscles = "class|String|int|char|float|Scanner|nextInt|nextFloat|nextLine|System|out|println|if|else|public|static|void|new|^in$"
operateurs = "^(=)$|^(\+){1,2}$|(-)|(<)|(>)"
chiffres = "^(\d+)$"
symboles = "[\[!\|{};,\.']|\(\){|\(|\)|{}|\[\]|\{|\}|\""
identif = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
mc=[]
op=[]
symb=[]
chif=[]
iden=[]
class meth(object): 
    window=[]
    file_name=[]
    data=""
    j=0
    def pushlex(self):
        Ui_MainWindow.OUTPUT.setText("")
        Unites = nltk.wordpunct_tokenize(Ui_MainWindow.INPUT.toPlainText());
        mc.clear()
        op.clear()
        symb.clear()
        chif.clear()
        iden.clear()
        for i in Unites:
            if(re.findall(motscles,i)):
                mc.append(i)
            elif(re.findall(operateurs,i)):
                op.append(i)
            elif(re.findall(symboles,i)):
                symb.append(i)
            elif(re.findall(chiffres,i)):
                chif.append(i)
            elif(re.findall(identif,i)):
                iden.append(i)
        if meth.j==1:
            meth.j=0
        else:
            Ui_MainWindow.OUTPUT.append("-----------Identificateurs---------")
            Ui_MainWindow.OUTPUT.append(str(iden))
            Ui_MainWindow.OUTPUT.append("-----------Mots Cles---------------")
            Ui_MainWindow.OUTPUT.append(str(mc))
            Ui_MainWindow.OUTPUT.append("-----------Operateurs--------------")
            Ui_MainWindow.OUTPUT.append(str(op))
            Ui_MainWindow.OUTPUT.append("-----------Constants----------------")
            Ui_MainWindow.OUTPUT.append(str(chif))
            Ui_MainWindow.OUTPUT.append("-----------Symboles----------------")
            Ui_MainWindow.OUTPUT.append(str(symb))

    def pushsyn(self):
        
        content = Ui_MainWindow.INPUT.toPlainText()
        file = open('Test.lang','w')
        file.write(content)
        file.close()
        #calling the lexer class and initialise it with the source code
        lex = lexer.lexer(content)

        #calling tokenize method
        tokens = lex.tokenize()
        
        #Parser
        parse = Parser.Parser(tokens)
        objs = parse.parse()
	    
	    
        

    def openfile(self):
        dialog= QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            meth.file_name= dialog.selectedFiles()
            self.path = meth.file_name[0]

            if meth.file_name[0].endswith('.java'):
                with open(meth.file_name[0],'r') as f:
                    meth.data= f.read()
                    Ui_MainWindow.INPUT.setText(meth.data)
                    f.close()
            else:
                pass
        Ui_MainWindow.OUTPUT.append(self.path)
        
    def newfile(self):
        meth.file_name = QtWidgets.QFileDialog.getSaveFileName()
        file = open(meth.file_name[0],'w')
        text = ""
        file.write(text)
        file.close()
        Ui_MainWindow.OUTPUT.append("File Created")
    def save(self):
        file = open(meth.file_name[0],'w')
        text = Ui_MainWindow.INPUT.toPlainText()
        file.write(text)
        file.close()
        Ui_MainWindow.OUTPUT.append("File Saved")
        print("File Saved")
    def ctrl_c(self):
        cp = QApplication.clipboard()
        cp.clear(mode=cp.Clipboard)
        cursor = Ui_MainWindow.INPUT.textCursor()
        print(cursor.selectedText())
        cp.setText(cursor.selectedText(),mode = cp.Clipboard)
    def cut(self):
        cp = QApplication.clipboard()
        cp.clear(mode=cp.Clipboard)
        cursor = Ui_MainWindow.INPUT.textCursor()
        print(cursor.selectedText())
        cp.setText(cursor.selectedText(),mode = cp.Clipboard)
        cursor.removeSelectedText()
    def paste(self):
        cp = QApplication.clipboard().text()
        Ui_MainWindow.INPUT.insertPlainText(cp)
    def neww(window):
        meth.window.append(window) 
        window.show()

