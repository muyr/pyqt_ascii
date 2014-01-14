# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.11
# Email : muyanru345@163.com
###################################################################
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    import sip
    sip.setapi("QString",  2)
    sip.setapi("QVariant",  2)
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import sys,pickle

class MAsciiWindow(QWidget):
    def __init__(self, parent = None):
        super(MAsciiWindow, self).__init__(parent)
        self.setStyleSheet('font-family:Microsoft YaHei')
        # sometimes use 'U'
        # sometimes use 'rb'
        pickleFile = open('asciiDict.mu', 'U')
        # pickleFile = open('asciiDict.mu', 'rb')
        self.asciiDict = pickle.load(pickleFile)
        pickleFile.close()
        self.initUI()

    def initUI(self):
        inputLabel = QLabel('Input Word:')
        self.inputLineEdit = QLineEdit('')
        # self.inputLineEdit.setInputMask('N')
        genButton = QPushButton('Go')
        self.connect(genButton, SIGNAL('clicked()'), self.slotGenAscii)
        
        emptyCharLabel = QLabel('Empty Char:')
        self.emptyCharLineEdit = QLineEdit(' ')
        self.emptyCharLineEdit.setMaxLength(1)
        fillCharLabel = QLabel('Fill Char:')
        self.fillCharLineEdit = QLineEdit('#')
        self.fillCharLineEdit.setMaxLength(1)


        self.resultTextEdit = QTextEdit('')
        self.resultTextEdit.setFixedHeight(130)
        self.resultTextEdit.setWordWrapMode(QTextOption.NoWrap)

        copyButton = QPushButton('Copy')
        self.connect(copyButton, SIGNAL('clicked()'), self.slotCopy)
        

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(inputLabel)
        inputLayout.addWidget(self.inputLineEdit)
        inputLayout.addWidget(genButton)

        fillCharLayout = QHBoxLayout()
        fillCharLayout.addWidget(emptyCharLabel)
        fillCharLayout.addWidget(self.emptyCharLineEdit)
        fillCharLayout.addSpacing(10)
        fillCharLayout.addWidget(fillCharLabel)
        fillCharLayout.addWidget(self.fillCharLineEdit)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(fillCharLayout)
        mainLayout.addWidget(self.resultTextEdit)
        mainLayout.addWidget(copyButton)
        self.setLayout(mainLayout)

    def slotGenAscii(self):
        inputWord = self.inputLineEdit.text()
        emptyChar = self.emptyCharLineEdit.text()
        fillChar = self.fillCharLineEdit.text()
        outputWord = ''
        outputList = []
        for char in inputWord:
            if self.asciiDict.has_key(char.lower()):
                outputList.append(self.asciiDict.get(char.lower()))
        contentList = []
        for i in range(len(outputList[0])):
            tmpList = ''
            for j in range(len(outputList)):
                tmpList += outputList[j][i]
            contentList.append(tmpList)
        for i in contentList:
            for j in i:
                if j == '0':
                    outputWord += emptyChar
                elif j == '1':
                    outputWord += fillChar
            outputWord += '\n'
        doc = QTextDocument(outputWord)
        self.resultTextEdit.setDocument(doc)

    def slotCopy(self):
        clipboard = QApplication.clipboard()
        doc = self.resultTextEdit.document()
        clipboard.setText(doc.toPlainText())
    	


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MAsciiWindow()
    test.show()
    sys.exit(app.exec_())
