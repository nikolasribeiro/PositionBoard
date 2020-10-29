import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from gui_main import MainGUI


class DisplayModal(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("participant_raw.ui", self)
        
        #Saves the name into a database
        self.btn_add.clicked.connect(self.add_participan)

    def add_participan(self):

        return (
    
            self.participant1.text(),
            self.participant_2.text(),
            self.participant_3.text(),
            self.participant_4.text(),
            self.participant_5.text(),
            self.participant_6.text(),
            self.participant_7.text(),
            self.participant_8.text(),
            self.participant_9.text(),
            self.participant_10.text(),
            self.participant_11.text(),
            self.participant_22.text(),
            self.participant_23.text(),
            self.participant_24.text(),
            self.participant_25.text(),
            self.participant_26.text()

        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DisplayModal()
    gui.show()
    sys.exit(app.exec_())
