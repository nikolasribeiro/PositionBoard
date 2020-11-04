import sys
import os
import time
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUI.gui_participant import Ui_Window_Participans
import threading
import Data.ping_pong_db as db
import Data.pool_db as pool_db
import Data.uno_db as uno_db
import json

status16 = {}
status8  = {}
status4  = {}
final    = {}
ROUTES   = ["config/ping_pong/", "config/pool/", "config/uno/"]

class MainGUI(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("raw.ui", self)

        #Call modal to add participans
        self.add_part.triggered.connect(self.show_participans)
        self.refresh_button.clicked.connect(self.get_participans)

        #Selecting the game to display
        self.game_selector.activated[str].connect(self.select_game)

        #Buttons of save and load data to board
        self.save_board.clicked.connect(self.save_status)
        self.load_board.clicked.connect(self.load_status)

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
        self.win_1.clicked.connect( lambda: self.next_stage(1))
        self.win_2.clicked.connect( lambda: self.next_stage(2))
        self.win_3.clicked.connect( lambda: self.next_stage(3))
        self.win_4.clicked.connect( lambda: self.next_stage(4))
        self.win_5.clicked.connect( lambda: self.next_stage(5))
        self.win_6.clicked.connect( lambda: self.next_stage(6))
        self.win_7.clicked.connect( lambda: self.next_stage(7))
        self.win_8.clicked.connect( lambda: self.next_stage(8))
        self.win_9.clicked.connect( lambda: self.next_stage(9))
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
        self.next_semifinalsBTN.clicked.connect(    lambda: self.semi_finals(1))
        self.next_semifinalsBTN_2.clicked.connect(  lambda: self.semi_finals(2))
        self.next_semifinalsBTN_3.clicked.connect(  lambda: self.semi_finals(3))
        self.next_semifinalsBTN_4.clicked.connect(  lambda: self.semi_finals(4))
        
        #Select WINNER!
        self.btn_final.clicked.connect(lambda  : self.final(1))
        self.btn_final2.clicked.connect(lambda : self.final(2))

    def select_game(self, game):
        if game == "Ping Pong":
            self.reset_board()
            self.name_of_game.setText(game)
            self.get_participans(db)
        
        if game == "Uno":
            self.reset_board()
            self.name_of_game.setText(game)
            self.get_participans(uno_db)
        
        if game == "Pool":
            self.reset_board()
            self.name_of_game.setText(game)
            self.get_participans(pool_db)

    def get_participans(self, database):
        people = database.get_participant()
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
        global status16

        # ==== LEFT SIDE ====
        if identifier in [1,2,3,4,5,6,7,8]:

            if identifier == 1:
                self.next_stage1.setText(self.part_1.text())
                self.part_2.setStyleSheet("background-color: #FE2E2E")
                self.part_1.setStyleSheet("background-color: #28B463")
                self.win_2.setEnabled(False)
                self.win_1.setEnabled(False)
            
            elif identifier == 2:
                self.next_stage1.setText(self.part_2.text())

                self.part_1.setStyleSheet("background-color: #FE2E2E")
                self.part_2.setStyleSheet("background-color: #28B463")
                self.win_1.setEnabled(False)
                self.win_2.setEnabled(False)

            elif identifier == 3:
                self.next_stage1_2.setText(self.part_3.text())
                
                self.part_4.setStyleSheet("background-color: #FE2E2E")
                self.part_3.setStyleSheet("background-color: #28B463")
                self.win_4.setEnabled(False)
                self.win_3.setEnabled(False)

            elif identifier == 4:
                self.next_stage1_2.setText(self.part_4.text())
                
                self.part_3.setStyleSheet("background-color: #FE2E2E")
                self.part_4.setStyleSheet("background-color: #28B463")
                self.win_3.setEnabled(False)
                self.win_4.setEnabled(False)

            elif identifier == 5:
                self.next_stage1_3.setText(self.part_5.text())
                
                self.part_6.setStyleSheet("background-color: #FE2E2E")
                self.part_5.setStyleSheet("background-color: #28B463")
                self.win_6.setEnabled(False)
                self.win_5.setEnabled(False)

            elif identifier == 6:
                self.next_stage1_3.setText(self.part_6.text())
                
                self.part_5.setStyleSheet("background-color: #FE2E2E")
                self.part_6.setStyleSheet("background-color: #28B463")
                self.win_5.setEnabled(False)
                self.win_6.setEnabled(False)
            
            elif identifier == 7:
                self.next_stage1_4.setText(self.part_7.text())
                
                self.part_8.setStyleSheet("background-color: #FE2E2E")
                self.part_7.setStyleSheet("background-color: #28B463")
                self.win_8.setEnabled(False)
                self.win_7.setEnabled(False)

            elif identifier == 8:
                self.next_stage1_4.setText(self.part_8.text())
                
                self.part_7.setStyleSheet("background-color: #FE2E2E")
                self.part_8.setStyleSheet("background-color: #28B463")
                self.win_7.setEnabled(False)
                self.win_8.setEnabled(False)

        # ==== RIGHT SIDE ====
        if identifier in [9,10,11,12,13,14,15,16]:
            if identifier == 9:
                self.next_stage1_5.setText(self.part_9.text())
                
                self.part_10.setStyleSheet("background-color: #FE2E2E")
                self.part_9.setStyleSheet("background-color: #28B463")
                self.win_10.setEnabled(False)
                self.win_9.setEnabled(False)

            elif identifier == 10:
                self.next_stage1_5.setText(self.part_10.text())
                
                self.part_9.setStyleSheet("background-color: #FE2E2E")
                self.part_10.setStyleSheet("background-color: #28B463")
                self.win_9.setEnabled(False)
                self.win_10.setEnabled(False)

            elif identifier == 11:
                self.next_stage1_6.setText(self.part_11.text())
                
                self.part_12.setStyleSheet("background-color: #FE2E2E")
                self.part_11.setStyleSheet("background-color: #28B463")
                self.win_12.setEnabled(False)
                self.win_11.setEnabled(False)

            elif identifier == 12:
                self.next_stage1_6.setText(self.part_12.text())
                
                self.part_11.setStyleSheet("background-color: #FE2E2E")
                self.part_12.setStyleSheet("background-color: #28B463")
                self.win_11.setEnabled(False)
                self.win_12.setEnabled(False)

            elif identifier == 13:
                self.next_stage1_7.setText(self.part_13.text())
                
                self.part_14.setStyleSheet("background-color: #FE2E2E")
                self.part_13.setStyleSheet("background-color: #28B463")
                self.win_14.setEnabled(False)
                self.win_13.setEnabled(False)

            elif identifier == 14:
                self.next_stage1_7.setText(self.part_14.text())
               
                self.part_13.setStyleSheet("background-color: #FE2E2E")
                self.part_14.setStyleSheet("background-color: #28B463")
                self.win_13.setEnabled(False)
                self.win_14.setEnabled(False)

            elif identifier == 15:
                self.next_stage1_8.setText(self.part_15.text())

                
                self.part_16.setStyleSheet("background-color: #FE2E2E")
                self.part_15.setStyleSheet("background-color: #28B463")
                self.win_16.setEnabled(False)
                self.win_15.setEnabled(False)

            elif identifier == 16:
                self.next_stage1_8.setText(self.part_16.text())

                
                self.part_15.setStyleSheet("background-color: #FE2E2E")
                self.part_16.setStyleSheet("background-color: #28B463")
                self.win_15.setEnabled(False)
                self.win_16.setEnabled(False)

        if self.next_stage1.text() != "" and self.next_stage1_2.text() != "" and self.next_stage1_3.text() != "" and self.next_stage1_4.text() != "" and self.next_stage1_5.text() != "" and self.next_stage1_6.text() != "" and self.next_stage1_7.text() != "" and self.next_stage1_8.text() != "":
            self.next_stageBTN_1.setEnabled(True)
            self.next_stageBTN_2.setEnabled(True)
            self.next_stageBTN_3.setEnabled(True)
            self.next_stageBTN_4.setEnabled(True)
            self.next_stageBTN_5.setEnabled(True)
            self.next_stageBTN_6.setEnabled(True)
            self.next_stageBTN_7.setEnabled(True)
            self.next_stageBTN_8.setEnabled(True)

    def quarter_final(self, code):
        global status8

        # ==== LEFT SIDE ====
        if code in [1,2,3,4]:
            if code == 1:
                self.next_semiFinals.setText(self.next_stage1.text())
                self.next_stage1_2.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_2.setEnabled(False)
                self.next_stageBTN_1.setEnabled(False)

            elif code == 2:
                self.next_semiFinals.setText(self.next_stage1_2.text())

                self.next_stage1.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1_2.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_1.setEnabled(False)
                self.next_stageBTN_2.setEnabled(False)

            elif code == 3:
                self.next_semiFinals_2.setText(self.next_stage1_3.text())


                self.next_stage1_4.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1_3.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_4.setEnabled(False)
                self.next_stageBTN_3.setEnabled(False)

            elif code == 4:
                self.next_semiFinals_2.setText(self.next_stage1_4.text())


                self.next_stage1_3.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1_4.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_3.setEnabled(False)
                self.next_stageBTN_4.setEnabled(False)
        
        # ==== RIGHT SIDE ====
        if code in [5,6,7,8]:
            if code == 5:
                self.next_semiFinals_3.setText(self.next_stage1_5.text())
                self.next_stage1_6.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1_5.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_6.setEnabled(False)
                self.next_stageBTN_5.setEnabled(False)

            elif code == 6:
                self.next_semiFinals_3.setText(self.next_stage1_6.text())
                self.next_stage1_5.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1_6.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_5.setEnabled(False)
                self.next_stageBTN_6.setEnabled(False)

            elif code == 7:
                self.next_semiFinals_4.setText(self.next_stage1_7.text())
                self.next_stage1_8.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1_7.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_8.setEnabled(False)
                self.next_stageBTN_7.setEnabled(False)
                
            
            elif code == 8:
                self.next_semiFinals_4.setText(self.next_stage1_8.text())
                self.next_stage1_7.setStyleSheet("background-color: #FE2E2E")
                self.next_stage1_8.setStyleSheet("background-color: #28B463")
                self.next_stageBTN_7.setEnabled(False)
                self.next_stageBTN_8.setEnabled(False)


        if self.next_semiFinals.text() != "" and self.next_semiFinals_2.text() != "" and self.next_semiFinals_3.text() != "" and self.next_semiFinals_4.text() != "":
            self.next_semifinalsBTN.setEnabled(True)
            self.next_semifinalsBTN_2.setEnabled(True)
            self.next_semifinalsBTN_3.setEnabled(True)
            self.next_semifinalsBTN_4.setEnabled(True)

    def semi_finals(self, code):
        # ==== LEFT SIDE ====
        if code in [1,2]:
            if code == 1:
                self.final_part.setText(self.next_semiFinals.text())
                self.next_semiFinals_2.setStyleSheet("background-color: #FE2E2E")
                self.next_semiFinals.setStyleSheet("background-color: #28B463")
                self.next_semifinalsBTN_2.setEnabled(False)
                self.next_semifinalsBTN.setEnabled(False)

            if code == 2:
                self.final_part.setText(self.next_semiFinals_2.text())
                self.next_semiFinals.setStyleSheet("background-color: #FE2E2E")
                self.next_semiFinals_2.setStyleSheet("background-color: #28B463")
                self.next_semifinalsBTN.setEnabled(False)
                self.next_semifinalsBTN_2.setEnabled(False)
        
        if code in [3,4]:
            if code == 3:
                self.final_part2.setText(self.next_semiFinals_3.text())
                self.next_semiFinals_4.setStyleSheet("background-color: #FE2E2E")
                self.next_semiFinals_3.setStyleSheet("background-color: #28B463")
                self.next_semifinalsBTN_4.setEnabled(False)
                self.next_semifinalsBTN_3.setEnabled(False)
            
            if code == 4:
                self.final_part2.setText(self.next_semiFinals_4.text())
                self.next_semiFinals_3.setStyleSheet("background-color: #FE2E2E")
                self.next_semiFinals_4.setStyleSheet("background-color: #28B463")
                self.next_semifinalsBTN_3.setEnabled(False)
                self.next_semifinalsBTN_4.setEnabled(False)

        if self.final_part.text() != "" and self.final_part2.text() != "":
            self.btn_final.setEnabled(True)
            self.btn_final2.setEnabled(True)

    def final(self, code):

        if code == 1:
            self.show_winner(self.final_part.text())
            self.final_part2.setStyleSheet("background-color: #FE2E2E")
            self.final_part.setStyleSheet("background-color: #28B463")
            self.btn_final2.setEnabled(False)
        
        elif code == 2:
            self.show_winner(self.final_part2.text())
            self.final_part.setStyleSheet("background-color: #FE2E2E")
            self.final_part2.setStyleSheet("background-color: #28B463")
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

    def reset_board(self):

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

        #Disabled all the unnesesary buttons
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

        #Reset the styles of the LineText
        self.part_1.setStyleSheet("")
        self.part_2.setStyleSheet("")
        self.part_3.setStyleSheet("")
        self.part_4.setStyleSheet("")
        self.part_5.setStyleSheet("")
        self.part_6.setStyleSheet("")
        self.part_7.setStyleSheet("")
        self.part_8.setStyleSheet("")
        self.part_9.setStyleSheet("")
        self.part_10.setStyleSheet("")
        self.part_11.setStyleSheet("")
        self.part_12.setStyleSheet("")
        self.part_13.setStyleSheet("")
        self.part_14.setStyleSheet("")
        self.part_15.setStyleSheet("")
        self.part_16.setStyleSheet("")

        self.next_stage1.setStyleSheet("")
        self.next_stage1_2.setStyleSheet("")
        self.next_stage1_3.setStyleSheet("")
        self.next_stage1_4.setStyleSheet("")
        self.next_stage1_5.setStyleSheet("")
        self.next_stage1_6.setStyleSheet("")
        self.next_stage1_7.setStyleSheet("")
        self.next_stage1_8.setStyleSheet("")

        self.next_semiFinals.setStyleSheet("")
        self.next_semiFinals_2.setStyleSheet("")
        self.next_semiFinals_3.setStyleSheet("")
        self.next_semiFinals_4.setStyleSheet("")

        self.final_part.setStyleSheet("")
        self.final_part2.setStyleSheet("")

        #Reset the Line Text to blank
        self.next_stage1.setText("")
        self.next_stage1_2.setText("")
        self.next_stage1_3.setText("")
        self.next_stage1_4.setText("")
        self.next_stage1_5.setText("")
        self.next_stage1_6.setText("")
        self.next_stage1_7.setText("")
        self.next_stage1_8.setText("")

        self.next_semiFinals.setText("")
        self.next_semiFinals_2.setText("")
        self.next_semiFinals_3.setText("")
        self.next_semiFinals_4.setText("")

        self.final_part.setText("")
        self.final_part2.setText("")

    def save_status(self):
        global status16, status8, status4, final, ROUTES

        #saving this data in the status global variable

        #16th Participants
        status16[self.part_1.text()]    = {'name': self.part_1.text(),  'color': self.part_1.styleSheet(),  'btn_state': self.win_1.isEnabled()}
        status16[self.part_2.text()]    = {'name': self.part_2.text(),  'color': self.part_2.styleSheet(),  'btn_state': self.win_2.isEnabled()}
        status16[self.part_3.text()]    = {'name': self.part_3.text(),  'color': self.part_3.styleSheet(),  'btn_state': self.win_3.isEnabled()}
        status16[self.part_4.text()]    = {'name': self.part_4.text(),  'color': self.part_4.styleSheet(),  'btn_state': self.win_4.isEnabled()}
        status16[self.part_5.text()]    = {'name': self.part_5.text(),  'color': self.part_5.styleSheet(),  'btn_state': self.win_5.isEnabled()}
        status16[self.part_6.text()]    = {'name': self.part_6.text(),  'color': self.part_6.styleSheet(),  'btn_state': self.win_6.isEnabled()}
        status16[self.part_7.text()]    = {'name': self.part_7.text(),  'color': self.part_7.styleSheet(),  'btn_state': self.win_7.isEnabled()}
        status16[self.part_8.text()]    = {'name': self.part_8.text(),  'color': self.part_8.styleSheet(),  'btn_state': self.win_8.isEnabled()}
        status16[self.part_9.text()]    = {'name': self.part_9.text(),  'color': self.part_9.styleSheet(),  'btn_state': self.win_9.isEnabled()}
        status16[self.part_10.text()]   = {'name': self.part_10.text(), 'color': self.part_10.styleSheet(), 'btn_state': self.win_10.isEnabled()}
        status16[self.part_11.text()]   = {'name': self.part_11.text(), 'color': self.part_11.styleSheet(), 'btn_state': self.win_11.isEnabled()}
        status16[self.part_12.text()]   = {'name': self.part_12.text(), 'color': self.part_12.styleSheet(), 'btn_state': self.win_12.isEnabled()}
        status16[self.part_13.text()]   = {'name': self.part_13.text(), 'color': self.part_13.styleSheet(), 'btn_state': self.win_13.isEnabled()}
        status16[self.part_14.text()]   = {'name': self.part_14.text(), 'color': self.part_14.styleSheet(), 'btn_state': self.win_14.isEnabled()}
        status16[self.part_15.text()]   = {'name': self.part_15.text(), 'color': self.part_15.styleSheet(), 'btn_state': self.win_15.isEnabled()}
        status16[self.part_16.text()]   = {'name': self.part_16.text(), 'color': self.part_16.styleSheet(), 'btn_state': self.win_16.isEnabled()}
        
        status8[self.next_stage1.text()]    = {'name': self.next_stage1.text(),     'color':self.next_stage1.styleSheet(),   'btn_state':self.next_stageBTN_1.isEnabled()}
        status8[self.next_stage1_2.text()]  = {'name': self.next_stage1_2.text(),   'color':self.next_stage1_2.styleSheet(), 'btn_state':self.next_stageBTN_2.isEnabled()}
        status8[self.next_stage1_3.text()]  = {'name': self.next_stage1_3.text(),   'color':self.next_stage1_3.styleSheet(), 'btn_state':self.next_stageBTN_3.isEnabled()}
        status8[self.next_stage1_4.text()]  = {'name': self.next_stage1_4.text(),   'color':self.next_stage1_4.styleSheet(), 'btn_state':self.next_stageBTN_4.isEnabled()}
        status8[self.next_stage1_5.text()]  = {'name': self.next_stage1_5.text(),   'color':self.next_stage1_5.styleSheet(), 'btn_state':self.next_stageBTN_5.isEnabled()}
        status8[self.next_stage1_6.text()]  = {'name': self.next_stage1_6.text(),   'color':self.next_stage1_6.styleSheet(), 'btn_state':self.next_stageBTN_6.isEnabled()}
        status8[self.next_stage1_7.text()]  = {'name': self.next_stage1_7.text(),   'color':self.next_stage1_7.styleSheet(), 'btn_state':self.next_stageBTN_7.isEnabled()}
        status8[self.next_stage1_8.text()]  = {'name': self.next_stage1_8.text(),   'color':self.next_stage1_8.styleSheet(), 'btn_state':self.next_stageBTN_8.isEnabled()}

        status4[self.next_semiFinals.text()]    = {'name': self.next_semiFinals.text(),   'color': self.next_semiFinals.styleSheet(),    'btn_state':self.next_semifinalsBTN.isEnabled()}
        status4[self.next_semiFinals_2.text()]  = {'name': self.next_semiFinals_2.text(), 'color':self.next_semiFinals_2.styleSheet(),   'btn_state':self.next_semifinalsBTN_2.isEnabled()}
        status4[self.next_semiFinals_3.text()]  = {'name': self.next_semiFinals_3.text(), 'color':self.next_semiFinals_3.styleSheet(),   'btn_state':self.next_semifinalsBTN_3.isEnabled()}
        status4[self.next_semiFinals_4.text()]  = {'name': self.next_semiFinals_4.text(), 'color':self.next_semiFinals_4.styleSheet(),   'btn_state':self.next_semifinalsBTN_4.isEnabled()}

        final[self.final_part.text()] = {'name': self.final_part.text(), 'color':self.final_part.styleSheet(),   'btn_state':self.btn_final.isEnabled()}
        final[self.final_part2.text()] = {'name': self.final_part2.text(), 'color':self.final_part2.styleSheet(),   'btn_state':self.btn_final2.isEnabled()}

        if self.name_of_game.text() == "Ping Pong":

            with open(f"{ROUTES[0]}config16.json", 'w') as save:
                json.dump(status16, save)
            
            with open(f"{ROUTES[0]}config8.json", 'w') as save8:
                print(save8)
                json.dump(status8, save8)
            
            with open(f"{ROUTES[0]}config4.json", "w") as save4:
                json.dump(status4, save4)
            
            with open(f"{ROUTES[0]}config2.json", "w") as save2:
                json.dump(final, save2)

        elif self.name_of_game.text() == "Uno":
            with open(f"{ROUTES[2]}config16.json", 'w') as save:
                json.dump(status16, save)
            
            with open(f"{ROUTES[2]}config8.json", 'w') as save8:
                print(save8)
                json.dump(status8, save8)
            
            with open(f"{ROUTES[2]}config4.json", "w") as save4:
                json.dump(status4, save4)
            
            with open(f"{ROUTES[2]}config2.json", "w") as save2:
                json.dump(final, save2)
        
        elif self.name_of_game.text() == "Pool":
            with open(f"{ROUTES[1]}config16.json", 'w') as save:
                json.dump(status16, save)
            
            with open(f"{ROUTES[1]}config8.json", 'w') as save8:
                print(save8)
                json.dump(status8, save8)
            
            with open(f"{ROUTES[1]}config4.json", "w") as save4:
                json.dump(status4, save4)
            
            with open(f"{ROUTES[1]}config2.json", "w") as save2:
                json.dump(final, save2)

        msg = QMessageBox()
        msg.setWindowTitle("Data Saved")
        msg.setText("Data Saved Successfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def load_status(self):
        global ROUTES

        if self.name_of_game.text() == "Ping Pong":
            self.__load_data(ROUTES[0])

        elif self.name_of_game.text() == "Uno":
            self.__load_data(ROUTES[2])

        elif self.name_of_game.text() == "Pool":
            self.__load_data(ROUTES[1])


    
    def __load_data(self, selector):
        print("Esto es selector cuando llama a la funcion anonima: ", selector)

        with open(f"{selector}config16.json") as load:
            loading_data = json.load(load)
            
            tmp16 = []

            for key in loading_data.keys():
                if key != '':
                    tmp16.append(key)
                else:
                    print("La key esta vacia")
            
            self.part_1.setText(loading_data[tmp16[0]]['name'])
            self.part_2.setText(loading_data[tmp16[1]]['name'])
            self.part_3.setText(loading_data[tmp16[2]]['name'])
            self.part_4.setText(loading_data[tmp16[3]]['name'])
            self.part_5.setText(loading_data[tmp16[4]]['name'])
            self.part_6.setText(loading_data[tmp16[5]]['name'])
            self.part_7.setText(loading_data[tmp16[6]]['name'])
            self.part_8.setText(loading_data[tmp16[7]]['name'])
            self.part_9.setText(loading_data[tmp16[8]]['name'])
            self.part_10.setText(loading_data[tmp16[9]]['name'])
            self.part_11.setText(loading_data[tmp16[10]]['name'])
            self.part_12.setText(loading_data[tmp16[11]]['name'])
            self.part_13.setText(loading_data[tmp16[12]]['name'])
            self.part_14.setText(loading_data[tmp16[13]]['name'])
            self.part_15.setText(loading_data[tmp16[14]]['name'])
            self.part_16.setText(loading_data[tmp16[15]]['name'])

            self.part_1.setStyleSheet(loading_data[tmp16[0]]['color'])
            self.part_2.setStyleSheet(loading_data[tmp16[1]]['color'])
            self.part_3.setStyleSheet(loading_data[tmp16[2]]['color'])
            self.part_4.setStyleSheet(loading_data[tmp16[3]]['color'])
            self.part_5.setStyleSheet(loading_data[tmp16[4]]['color'])
            self.part_6.setStyleSheet(loading_data[tmp16[5]]['color'])
            self.part_7.setStyleSheet(loading_data[tmp16[6]]['color'])
            self.part_8.setStyleSheet(loading_data[tmp16[7]]['color'])
            self.part_9.setStyleSheet(loading_data[tmp16[8]]['color'])
            self.part_10.setStyleSheet(loading_data[tmp16[9]]['color'])
            self.part_11.setStyleSheet(loading_data[tmp16[10]]['color'])
            self.part_12.setStyleSheet(loading_data[tmp16[11]]['color'])
            self.part_13.setStyleSheet(loading_data[tmp16[12]]['color'])
            self.part_14.setStyleSheet(loading_data[tmp16[13]]['color'])
            self.part_15.setStyleSheet(loading_data[tmp16[14]]['color'])
            self.part_16.setStyleSheet(loading_data[tmp16[15]]['color'])
            

            #Disabled buttons that already played
            self.win_1.setEnabled(loading_data[tmp16[0]]['btn_state'])
            self.win_2.setEnabled(loading_data[tmp16[1]]['btn_state'])
            self.win_3.setEnabled(loading_data[tmp16[2]]['btn_state'])
            self.win_4.setEnabled(loading_data[tmp16[3]]['btn_state'])
            self.win_5.setEnabled(loading_data[tmp16[4]]['btn_state'])
            self.win_6.setEnabled(loading_data[tmp16[5]]['btn_state'])
            self.win_7.setEnabled(loading_data[tmp16[6]]['btn_state'])
            self.win_8.setEnabled(loading_data[tmp16[7]]['btn_state'])
            self.win_9.setEnabled(loading_data[tmp16[8]]['btn_state'])
            self.win_10.setEnabled(loading_data[tmp16[9]]['btn_state'])
            self.win_11.setEnabled(loading_data[tmp16[10]]['btn_state'])
            self.win_12.setEnabled(loading_data[tmp16[11]]['btn_state'])
            self.win_13.setEnabled(loading_data[tmp16[12]]['btn_state'])
            self.win_14.setEnabled(loading_data[tmp16[13]]['btn_state'])
            self.win_15.setEnabled(loading_data[tmp16[14]]['btn_state'])
            self.win_16.setEnabled(loading_data[tmp16[15]]['btn_state'])
        
        with open(f"{selector}config8.json") as load8:
            loading_8 = json.load(load8)
            tmp8 = []

            for key in loading_8.keys():
                if key != '':
                    tmp8.append(key)
                else:
                    print("La key esta vacia")
            
            self.next_stage1.setText(loading_8[tmp8[0]]['name'])
            self.next_stage1_2.setText(loading_8[tmp8[1]]['name'])
            self.next_stage1_3.setText(loading_8[tmp8[2]]['name'])
            self.next_stage1_4.setText(loading_8[tmp8[3]]['name'])
            self.next_stage1_5.setText(loading_8[tmp8[4]]['name'])
            self.next_stage1_6.setText(loading_8[tmp8[5]]['name'])
            self.next_stage1_7.setText(loading_8[tmp8[6]]['name'])
            self.next_stage1_8.setText(loading_8[tmp8[7]]['name'])

            self.next_stage1.setStyleSheet(loading_8[tmp8[0]]['color'])
            self.next_stage1_2.setStyleSheet(loading_8[tmp8[1]]['color'])
            self.next_stage1_3.setStyleSheet(loading_8[tmp8[2]]['color'])
            self.next_stage1_4.setStyleSheet(loading_8[tmp8[3]]['color'])
            self.next_stage1_5.setStyleSheet(loading_8[tmp8[4]]['color'])
            self.next_stage1_6.setStyleSheet(loading_8[tmp8[5]]['color'])
            self.next_stage1_7.setStyleSheet(loading_8[tmp8[6]]['color'])
            self.next_stage1_8.setStyleSheet(loading_8[tmp8[7]]['color'])

            self.next_stageBTN_1.setEnabled(loading_8[tmp8[0]]['btn_state'])
            self.next_stageBTN_2.setEnabled(loading_8[tmp8[1]]['btn_state'])
            self.next_stageBTN_3.setEnabled(loading_8[tmp8[2]]['btn_state'])
            self.next_stageBTN_4.setEnabled(loading_8[tmp8[3]]['btn_state'])
            self.next_stageBTN_5.setEnabled(loading_8[tmp8[4]]['btn_state'])
            self.next_stageBTN_6.setEnabled(loading_8[tmp8[5]]['btn_state'])
            self.next_stageBTN_7.setEnabled(loading_8[tmp8[6]]['btn_state'])
            self.next_stageBTN_8.setEnabled(loading_8[tmp8[7]]['btn_state'])
        
        with open(f"{selector}config4.json") as load4:
            loading_4 = json.load(load4)
            tmp4 = []

            for key in loading_4.keys():
                if key != '':
                    tmp4.append(key)
                else:
                    print("La key esta vacia")
            
            self.next_semiFinals.setText(loading_4[tmp4[0]]['name'])
            self.next_semiFinals_2.setText(loading_4[tmp4[1]]['name'])
            self.next_semiFinals_3.setText(loading_4[tmp4[2]]['name'])
            self.next_semiFinals_4.setText(loading_4[tmp4[3]]['name'])

            self.next_semiFinals.setStyleSheet(loading_4[tmp4[0]]['color'])
            self.next_semiFinals_2.setStyleSheet(loading_4[tmp4[1]]['color'])
            self.next_semiFinals_3.setStyleSheet(loading_4[tmp4[2]]['color'])
            self.next_semiFinals_4.setStyleSheet(loading_4[tmp4[3]]['color'])

            self.next_semifinalsBTN.setEnabled(loading_4[tmp4[0]]['btn_state'])
            self.next_semifinalsBTN_2.setEnabled(loading_4[tmp4[1]]['btn_state'])
            self.next_semifinalsBTN_3.setEnabled(loading_4[tmp4[2]]['btn_state'])
            self.next_semifinalsBTN_4.setEnabled(loading_4[tmp4[3]]['btn_state'])
        
        with open(f"{selector}config2.json") as load2:
            loading_2 = json.load(load2)
            tmp = []

            for key in loading_2.keys():
                if key != '':
                    tmp.append(key)
                else:
                    print("La key esta vacia")
            
            self.final_part.setText(loading_2[tmp[0]]['name'])
            self.final_part2.setText(loading_2[tmp[1]]['name'])
            
            self.btn_final.setEnabled(loading_2[tmp[0]]['btn_state'])
            self.btn_final2.setEnabled(loading_2[tmp[1]]['btn_state'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainGUI()
    gui.show()
    sys.exit(app.exec_())
