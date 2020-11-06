# Contributor :
# I Gede Teguh Satya Dharma (1708561019)
# Muhammad Firyanul Rizky (1708561006)
# I Gusti Ngurah Agung Widiaksa Putra (1708561066)

#importing nltk


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 70, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 100, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 231, 131))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 20, 231, 131))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 150, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 150, 81, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IR Project"))
        self.pushButton.setText(_translate("MainWindow", "Tokenisasi"))
        self.pushButton_2.setText(_translate("MainWindow", "Stopwords"))
        self.pushButton_3.setText(_translate("MainWindow", "Stemming"))
        self.label.setText(_translate("MainWindow", "Input Source"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        #adding action to push button
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton_2.clicked.connect(self.makeStopword)
        self.pushButton_3.clicked.connect(self.makeStemming)


    def clicked(self):
        # membuat result menjadi kosong
        self.lineEdit_2.clear()
        contentSource = self.lineEdit.toPlainText()
        # contentSource.translate(str.maketrans('','',string.punctuation)).lower()
        resToken = word_tokenize(contentSource)
        res = self.convertIntoString(resToken)
        self.lineEdit_2.insertPlainText(res)


    def convertIntoString(self, resToken):
        str = ""
        for r in resToken:
            str = str+r+(' | ')
        return str.lower()

    def makeStopword(self):
        #membuat result menjadi kosong
        self.lineEdit_2.clear()

        contentSource = self.lineEdit.toPlainText()
        resToken = word_tokenize(contentSource)
        myStopwords = set(stopwords.words('english'))

        deletedEl = ''
        for r in resToken :
            if r not in myStopwords:
                deletedEl = deletedEl + r + (' | ')
                deletedEl = deletedEl.lower()
        self.lineEdit_2.insertPlainText(deletedEl)

    def makeStemming(self):
        ps = PorterStemmer()
        # membuat result menjadi kosong
        self.lineEdit_2.clear()
        contentSource = self.lineEdit.toPlainText()
        resToken = word_tokenize(contentSource)
        stemRes = ''
        for r in resToken:
            stemRes = stemRes+ ps.stem(r)+ (' | ')
            stemRes.lower()
        self.lineEdit_2.insertPlainText(stemRes)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
