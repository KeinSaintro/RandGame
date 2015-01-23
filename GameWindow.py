# coding=utf-8
import sys
from random import randint
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from GameForm import Ui_MainWindow

class Game(QtGui.QMainWindow):

    def __init__(self):
        super(Game, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.maxStrick = 0
        self.nowStrick = 0
        self.WinText = ['Molodec','Norm','Not Bad','Ne Autist','Pobeda iz 10']
        self.LoseText = ['Bad','Autist','Davai Eshe Raz','Pochti Poluchilos','Loh']
        self.show()
        self.connect(self.ui.pushButton, SIGNAL("clicked()"),lambda who = 1: self.defGame(who))
        self.connect(self.ui.pushButton_3, SIGNAL("clicked()"),lambda who = 2: self.defGame(who))
        self.connect(self.ui.pushButton_5, SIGNAL("clicked()"),lambda who = 3: self.defGame(who))
        self.connect(self.ui.pushButton_2, SIGNAL("clicked()"),lambda who = 4: self.defGame(who))
        self.connect(self.ui.pushButton_4, SIGNAL("clicked()"),lambda who = 5: self.defGame(who))
        self.connect(self.ui.pushButton_6, SIGNAL("clicked()"),lambda who = 6: self.defGame(who))

    def defGame(self, number):
        randomText = randint(0,4)
        randomNumber = randint(1,6)
        if number == randomNumber:
            self.ui.label_7.setText(self.WinText[randomText])
            self.nowStrick = self.nowStrick + 1
            self.ui.label_5.setText(str(self.nowStrick))
            print self.nowStrick
            if self.nowStrick > self.maxStrick:
                self.maxStrick = self.nowStrick
                self.ui.label_6.setText(str(self.maxStrick))
                print self.ui.label_6
        else:
            self.ui.label_7.setText(self.LoseText[randomText])
            self.nowStrick = 0
            self.ui.label_5.setText(str(self.nowStrick))
        return


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()