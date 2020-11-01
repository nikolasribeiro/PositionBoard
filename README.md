# PositionBoard
<img src="img/Imagen.png" alt="Install developer terminal" />
This software is for the tournament of Ping Pong in Holberton School (you can use it in another tournament where 16 participans are in)

## Files
   **Content of this repo**    
| **File** | **Decription**|
|----------|---------------|
| Data | Folder that contains the code of a simple database |
| GUI | Folder that contains the source python code for GUI functionality. This code is getting from pyuic5 |
| img | Folder that contain a sample image of the software |
| gui_main.py | Main code of the software |
| participant_raw.ui | Interfaz without pyuic5 |
| raw.ui | Main GUI |

## Requirements
You need to install those programs in you Virtual Machine, main OS or in virtualenv for the software runs.

* Python3
* PyQt5
* Pyinstaller - Only if you want to create an executable file

## How to run it
First, if you are on linux. You need to open a new terminal and go to the folder repository and then execute this command
```
python3 gui_main.py
```

if you install all the packages, you will see the main gui.

***First Steps***
For adding new participants to you torunament, you go to the menu and select "Participans" and next: Add Participans
Then, a new window is opened and inside that window, you insert the 16th names of the participans and click on "Load Participans"

When you have all the names included for the tournament, close the new window and inside the MAIN GUI you have a button with the legend: "Set Participans!"
if you click on that button, you bring to the main gui all the participans names and you can start the tournament!


### Author
*Nicolas Ribeiro* - [Github](https://github.com/nikolasribeiro) || [Linkedin](https://www.linkedin.com/in/nicolas-sebastian-ribeiro/) || [Email](nikolas.sebastian.ribeiro@gmail.com)
