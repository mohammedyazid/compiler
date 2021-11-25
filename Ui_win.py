# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compiler.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.025, y2:1, stop:0.383085 rgba(36, 31, 49, 255), stop:0.791045 rgba(61, 56, 70, 255));\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lex_button = QtWidgets.QPushButton(self.centralwidget)
        self.lex_button.setGeometry(QtCore.QRect(650, 390, 141, 70))
        self.lex_button.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"color: rgb(0, 0, 0);")
        self.lex_button.setObjectName("lex_button")
        self.synt_button = QtWidgets.QPushButton(self.centralwidget)
        self.synt_button.setGeometry(QtCore.QRect(650, 470, 141, 70))
        self.synt_button.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"color: rgb(0, 0, 0);")
        self.synt_button.setObjectName("synt_button")
        Ui_MainWindow.TInput = QtWidgets.QTextEdit(self.centralwidget)
        Ui_MainWindow.TInput.setGeometry(QtCore.QRect(10, 30, 771, 341))
        Ui_MainWindow.TInput.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color:black;\n"
"font: 75 12pt \"Ubuntu\";\n"
"\n"
"")
        Ui_MainWindow.TInput.setObjectName("TInput")
        Ui_MainWindow.TOutput = QtWidgets.QTextEdit(self.centralwidget)
        Ui_MainWindow.TOutput.setGeometry(QtCore.QRect(10, 390, 631, 151))
        Ui_MainWindow.TOutput.setStyleSheet("background-color: rgb(192, 191, 188);\n"
"color:black;\n"
"font: 75 12pt \"Ubuntu\";\n"
"")
        Ui_MainWindow.TOutput.setObjectName("TOutput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.bar_newfile = QtWidgets.QAction(MainWindow)
        self.bar_newfile.setObjectName("bar_newfile")
        self.bar_new_window = QtWidgets.QAction(MainWindow)
        self.bar_new_window.setObjectName("bar_new_window")
        self.bar_openfile = QtWidgets.QAction(MainWindow)
        self.bar_openfile.setObjectName("bar_openfile")
        self.bar_savefile = QtWidgets.QAction(MainWindow)
        self.bar_savefile.setObjectName("bar_savefile")
        self.bar_copy = QtWidgets.QAction(MainWindow)
        self.bar_copy.setObjectName("bar_copy")
        self.bar_paste = QtWidgets.QAction(MainWindow)
        self.bar_paste.setObjectName("bar_paste")
        self.bar_cut = QtWidgets.QAction(MainWindow)
        self.bar_cut.setObjectName("bar_cut")
        self.menuFile.addAction(self.bar_newfile)
        self.menuFile.addAction(self.bar_new_window)
        self.menuFile.addAction(self.bar_openfile)
        self.menuFile.addAction(self.bar_savefile)
        self.menuEdit.addAction(self.bar_copy)
        self.menuEdit.addAction(self.bar_paste)
        self.menuEdit.addAction(self.bar_cut)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lex_button.setText(_translate("MainWindow", "Analyse Lexical"))
        self.synt_button.setText(_translate("MainWindow", "Analyse Syntaxique"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.bar_newfile.setText(_translate("MainWindow", "New File"))
        self.bar_new_window.setText(_translate("MainWindow", "New Window"))
        self.bar_openfile.setText(_translate("MainWindow", "Open File"))
        self.bar_savefile.setText(_translate("MainWindow", "Save File"))
        self.bar_copy.setText(_translate("MainWindow", "Copy"))
        self.bar_paste.setText(_translate("MainWindow", "Paste"))
        self.bar_cut.setText(_translate("MainWindow", "Cut"))
