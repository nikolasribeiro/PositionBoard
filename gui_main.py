import sys
import os
import time
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUI.gui_participant import Ui_Window_Participans
import threading
import Data.data_code as db

class MainGUI(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("raw.ui", self)

        #Call modal to add participans
        self.add_part.triggered.connect(self.show_participans)
        self.refresh_button.clicked.connect(self.get_participans)

        #Disable all the buttons to avoid future problems
        self.win_1.setEnabled(False)
        self.win_2.setEnabled(False)
        self.win_3.setEnabled(False)
        self.win_4.setEnabled(False)
        self.win_5.setEnabled(False)
        self.win_6.setEnabled(False)
        self.win_7.setEnabled(False)
        self.win_8.setEnabled(False)
        self.win_9.setEnabled(False)
        self.win_10.setEnabled(False)
        self.win_11.setEnabled(False)
        self.win_12.setEnabled(False)
        self.win_13.setEnabled(False)
        self.win_14.setEnabled(False)
        self.win_15.setEnabled(False)
        self.win_16.setEnabled(False)

        self.next_stageBTN_1.setEnabled(False)
        self.next_stageBTN_2.setEnabled(False)
        self.next_stageBTN_3.setEnabled(False)
        self.next_stageBTN_4.setEnabled(False)
        self.next_stageBTN_5.setEnabled(False)
        self.next_stageBTN_6.setEnabled(False)
        self.next_stageBTN_7.setEnabled(False)
        self.next_stageBTN_8.setEnabled(False)

        self.next_semifinalsBTN.setEnabled(False)
        self.next_semifinalsBTN_2.setEnabled(False)
        self.next_semifinalsBTN_3.setEnabled(False)
        self.next_semifinalsBTN_4.setEnabled(False)

        self.btn_final.setEnabled(False)
        self.btn_final2.setEnabled(False)


        #select the next stage
        self.win_1.clicked.connect(lambda: self.next_stage(1))
        self.win_2.clicked.connect(lambda: self.next_stage(2))
        self.win_3.clicked.connect(lambda: self.next_stage(3))
        self.win_4.clicked.connect(lambda: self.next_stage(4))
        self.win_5.clicked.connect(lambda: self.next_stage(5))
        self.win_6.clicked.connect(lambda: self.next_stage(6))
        self.win_7.clicked.connect(lambda: self.next_stage(7))
        self.win_8.clicked.connect(lambda: self.next_stage(8))
        self.win_9.clicked.connect(lambda: self.next_stage(9))
        self.win_10.clicked.connect(lambda: self.next_stage(10))
        self.win_11.clicked.connect(lambda: self.next_stage(11))
        self.win_12.clicked.connect(lambda: self.next_stage(12))
        self.win_13.clicked.connect(lambda: self.next_stage(13))
        self.win_14.clicked.connect(lambda: self.next_stage(14))
        self.win_15.clicked.connect(lambda: self.next_stage(15))
        self.win_16.clicked.connect(lambda: self.next_stage(16))

        #Select the Quarter Finals
        self.next_stageBTN_1.clicked.connect(lambda: self.quarter_final(1))
        self.next_stageBTN_2.clicked.connect(lambda: self.quarter_final(2))
        self.next_stageBTN_3.clicked.connect(lambda: self.quarter_final(3))
        self.next_stageBTN_4.clicked.connect(lambda: self.quarter_final(4))
        self.next_stageBTN_5.clicked.connect(lambda: self.quarter_final(5))
        self.next_stageBTN_6.clicked.connect(lambda: self.quarter_final(6))
        self.next_stageBTN_7.clicked.connect(lambda: self.quarter_final(7))
        self.next_stageBTN_8.clicked.connect(lambda: self.quarter_final(8))

        #Select Semi Finals
        self.next_semifinalsBTN.clicked.connect(lambda  : self.semi_finals(1))
        self.next_semifinalsBTN_2.clicked.connect(lambda: self.semi_finals(2))
        self.next_semifinalsBTN_3.clicked.connect(lambda: self.semi_finals(3))
        self.next_semifinalsBTN_4.clicked.connect(lambda: self.semi_finals(4))
        
        #Select WINNER!
        self.btn_final.clicked.connect(lambda  : self.final(1))
        self.btn_final2.clicked.connect(lambda : self.final(2))

    def get_participans(self):
        people = db.get_participant()
        names = []
        for name in people:
            names.append(name[1])
        
        self.part_1.setText(names[0])
        self.part_2.setText(names[1])
        self.part_3.setText(names[2])
        self.part_4.setText(names[3])
        self.part_5.setText(names[4])
        self.part_6.setText(names[5])
        self.part_7.setText(names[6])
        self.part_8.setText(names[7])
        self.part_9.setText(names[8])
        self.part_10.setText(names[9])
        self.part_11.setText(names[10])
        self.part_12.setText(names[11])
        self.part_13.setText(names[12])
        self.part_14.setText(names[13])
        self.part_15.setText(names[14])
        self.part_16.setText(names[15])

        #Disable the get button
        self.refresh_button.setEnabled(False)

        #Enable all the buttons
        self.win_1.setEnabled(True)
        self.win_2.setEnabled(True)
        self.win_3.setEnabled(True)
        self.win_4.setEnabled(True)
        self.win_5.setEnabled(True)
        self.win_6.setEnabled(True)
        self.win_7.setEnabled(True)
        self.win_8.setEnabled(True)
        self.win_9.setEnabled(True)
        self.win_10.setEnabled(True)
        self.win_11.setEnabled(True)
        self.win_12.setEnabled(True)
        self.win_13.setEnabled(True)
        self.win_14.setEnabled(True)
        self.win_15.setEnabled(True)
        self.win_16.setEnabled(True)

    def next_stage(self, identifier):


        # ==== LEFT SIDE ====
        if identifier in [1,2,3,4,5,6,7,8]:

            if identifier == 1:
                self.next_stage1.setText(self.part_1.text())
                self.part_2.setStyleSheet("background-color: #FE2E2E")
                self.win_2.setEnabled(False)
                self.win_1.setEnabled(False)
            
            elif identifier == 2:
                self.next_stage1.setText(self.part_2.text())
                self.part_1.setStyleSheet("background-color: #FE2E2E")
                self.win_1.setEnabled(False)
                self.win_2.setEnabled(False)

            elif identifier == 3:
                self.next_stage1_2.setText(self.part_3.text())
                self.part_4.setStyleSheet("background-color: #FE2E2E")
                self.win_4.setEnabled(False)
                self.win_3.setEnabled(False)

            elif identifier == 4:
                self.next_stage1_2.setText(self.part_4.text())
                self.part_3.setStyleSheet("background-color: #FE2E2E")
                self.win_3.setEnabled(False)
                self.win_4.setEnabled(False)

            elif identifier == 5:
                self.next_stage1_3.setText(self.part_5.text())
                self.part_6.setStyleSheet("background-color: #FE2E2E")
                self.win_6.setEnabled(False)
                self.win_5.setEnabled(False)

            elif identifier == 6:
                self.next_stage1_3.setText(self.part_6.text())
                self.part_5.setStyleSheet("background-color: #FE2E2E")
                self.win_5.setEnabled(False)
                self.win_6.setEnabled(False)
            
            elif identifier == 7:
                self.next_stage1_4.setText(self.part_7.text())
                self.part_8.setStyleSheet("background-color: #FE2E2E")
                self.win_8.setEnabled(False)
                self.win_7.setEnabled(False)

            elif identifier == 8:
                self.next_stage1_4.setText(self.part_8.text())
                self.part_7.setStyleSheet("background-color: #FE2E2E")
                self.win_7.setEnabled(False)
                self.win_8.setEnabled(False)

        # ==== RIGHT SIDE ====
        if identifier in [9,10,11,12,13,14,15,16]:
            if identifier == 9:
                self.next_stage1_5.setText(self.part_9.text())
                self.part_10.setStyleSheet("background-color: #FE2E2E")
                self.win_10.setEnabled(False)
                self.win_9.setEnabled(False)

            elif identifier == 10:
                self.next_stage1_5.setText(self.part_10.text())
                self.part_9.setStyleSheet("background-color: #FE2E2E")
                self.win_9.setEnabled(False)
                self.win_10.setEnabled(False)

            elif identifier == 11:
                self.next_stage1_6.setText(self.part_11.text())
                self.part_12.setStyleSheet("background-color: #FE2E2E")
                self.win_12.setEnabled(False)
                self.win_11.setEnabled(False)

            elif identifier == 12:
                self.next_stage1_6.setText(self.part_12.text())
                self.part_11.setStyleSheet("background-color: #FE2E2E")
                self.win_11.setEnabled(False)
                self.win_12.setEnabled(False)

            elif identifier == 13:
                self.next_stage1_7.setText(self.part_13.text())
                self.part_14.setStyleSheet("background-color: #FE2E2E")
                self.win_14.setEnabled(False)
                self.win_13.setEnabled(False)

            elif identifier == 14:
                self.next_stage1_7.setText(self.part_14.text())
                self.part_13.setStyleSheet("background-color: #FE2E2E")
                self.win_13.setEnabled(False)
                self.win_14.setEnabled(False)

            elif identifier == 15:
                self.next_stage1_8.setText(self.part_15.text())
                self.part_16.setStyleSheet("background-color: #FE2E2E")
                self.win_16.setEnabled(False)
                self.win_15.setEnabled(False)

            elif identifier == 16:
                self.next_stage1_8.setText(self.part_16.text())
                self.part_15.setStyleSheet("background-color: #FE2E2E")
                self.win_15.setEnabled(False)
                self.win_16.setEnabled(False)

        if self.next_stage1.text() != "" and self.next_stage1_2.text() != "":
            self.next_stageBTN_1.setEnabled(True)
            self.next_stageBTN_2.setEnabled(True)

        if self.next_stage1_3.text() != "" and self.next_stage1_4.text() != "":
            self.next_stageBTN_3.setEnabled(True)
            self.next_stageBTN_4.setEnabled(True)

        if self.next_stage1_5.text() != "" and self.next_stage1_6.text() != "":
            self.next_stageBTN_5.setEnabled(True)
            self.next_stageBTN_6.setEnabled(True)

        if self.next_stage1_7.text() != "" and self.next_stage1_8.text() != "":
            self.next_stageBTN_7.setEnabled(True)
            self.next_stageBTN_8.setEnabled(True)

    def quarter_final(self, code):

        # ==== LEFT SIDE ====
        if code in [1,2,3,4]:
            if code == 1:
                self.next_semiFinals.setText(self.next_stage1.text())
                self.next_stage1_2.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_2.setEnabled(False)
                self.next_stageBTN_1.setEnabled(False)

            elif code == 2:
                self.next_semiFinals.setText(self.next_stage1_2.text())
                self.next_stage1.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_1.setEnabled(False)
                self.next_stageBTN_2.setEnabled(False)

            elif code == 3:
                self.next_semiFinals_2.setText(self.next_stage1_3.text())
                self.next_stage1_4.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_4.setEnabled(False)
                self.next_stageBTN_3.setEnabled(False)

            elif code == 4:
                self.next_semiFinals_2.setText(self.next_stage1_4.text())
                self.next_stage1_3.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_3.setEnabled(False)
                self.next_stageBTN_4.setEnabled(False)
        
        # ==== RIGHT SIDE ====
        if code in [5,6,7,8]:
            if code == 5:
                self.next_semiFinals_3.setText(self.next_stage1_5.text())
                self.next_stage1_6.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_6.setEnabled(False)
                self.next_stageBTN_5.setEnabled(False)

            elif code == 6:
                self.next_semiFinals_3.setText(self.next_stage1_6.text())
                self.next_stage1_5.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_5.setEnabled(False)
                self.next_stageBTN_6.setEnabled(False)

            elif code == 7:
                self.next_semiFinals_4.setText(self.next_stage1_7.text())
                self.next_stage1_6.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_6.setEnabled(False)
                self.next_stageBTN_7.setEnabled(False)
            
            elif code == 8:
                self.next_semiFinals_4.setText(self.next_stage1_8.text())
                self.next_stage1_7.setStyleSheet("background-color: #FE2E2E")
                self.next_stageBTN_7.setEnabled(False)
                self.next_stageBTN_6.setEnabled(False)


        if self.next_semiFinals.text() != "" and self.next_semiFinals_2.text() != "":
            self.next_semifinalsBTN.setEnabled(True)
            self.next_semifinalsBTN_2.setEnabled(True)
        
        if self.next_semiFinals_3.text() != "" and self.next_semiFinals_4.text() != "":
            self.next_semifinalsBTN_3.setEnabled(True)
            self.next_semifinalsBTN_4.setEnabled(True)



    def semi_finals(self, code):
        # ==== LEFT SIDE ====
        if code in [1,2]:
            if code == 1:
                self.final_part.setText(self.next_semiFinals.text())
                self.next_semiFinals_2.setStyleSheet("background-color: #FE2E2E")
                self.next_semifinalsBTN_2.setEnabled(False)
                self.next_semifinalsBTN.setEnabled(False)

            if code == 2:
                self.final_part.setText(self.next_semiFinals_2.text())
                self.next_semiFinals.setStyleSheet("background-color: #FE2E2E")
                self.next_semifinalsBTN.setEnabled(False)
                self.next_semifinalsBTN_2.setEnabled(False)
        
        if code in [3,4]:
            if code == 3:
                self.final_part2.setText(self.next_semiFinals_3.text())
                self.next_semiFinals_4.setStyleSheet("background-color: #FE2E2E")
                self.next_semifinalsBTN_4.setEnabled(False)
                self.next_semifinalsBTN_3.setEnabled(False)
            
            if code == 4:
                self.final_part2.setText(self.next_semiFinals_4.text())
                self.next_semiFinals_3.setStyleSheet("background-color: #FE2E2E")
                self.next_semifinalsBTN_3.setEnabled(False)
                self.next_semifinalsBTN_4.setEnabled(False)

        if self.final_part.text() != "" and self.final_part2.text() != "":
            self.btn_final.setEnabled(True)
            self.btn_final2.setEnabled(True)

    def final(self, code):

        if code == 1:
            self.show_winner(self.final_part.text())
            self.final_part2.setStyleSheet("background-color: #FE2E2E")
            self.btn_final2.setEnabled(False)
        
        elif code == 2:
            self.show_winner(self.final_part2.text())
            self.final_part.setStyleSheet("background-color: #FE2E2E")
            self.btn_final.setEnabled(False)

    def show_winner(self, name_of_winner):
        msg = QMessageBox()
        msg.setWindowTitle("WE HAVE A WINNER!!")
        msg.setText(f"And the winner is: {name_of_winner} !!!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

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
