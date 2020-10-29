import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from gui_participant import Ui_Window_Participans
import threading
import core
from core_participans import *


class MainGUI(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("raw.ui", self)

        #Call modal to add participans
        self.add_part.triggered.connect(self.show_participans)
        self.refresh_button.clicked.connect(self.get_participans)

    def get_participans(self):
        people = DisplayModal().add_participan()
        

        print("Esto es participans: ", people)

    def set_participans_on_board(self):
        self.part_1.setText(core.participans["part1"])

    def show_participans(self):
        self.modal = QMainWindow()
        self.ui = Ui_Window_Participans()
        self.ui.setupUi(self.modal)
        self.modal.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainGUI()
    gui.show()
    sys.exit(app.exec_())
