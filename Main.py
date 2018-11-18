

#Project by Lukaszbroski
#Hopefully this project will help with some decision making.
#Feel free to use this project and modify it however you like.
#However I would appreciate if you include my name in the credits somewhere.

#the program structure will hopefully be as follows:

#the program batch processes all .txts in a folder
#the program will read the spoiler logs, and create an object for exactly what checks are required, and how many steps
#it takes to get there or something like that if I deem it important
#the program will then compile spreadsheet data for the inputted spoiler logs.


import glob
import os
import re
import pandas as pd


cwd = os.getcwd()
def parse_files():

    for filename in os.listdir(cwd + "/input", "*.txt"):
        with open(filename, 'r+') as current_file:
            lines = current_file.readlines()
            for current_line in range(0, len(lines)):
                line = lines[current_line]
                current_sphere = 1
                if line == "Locations:":
                    print("%d" + line %current_line)

                if line == "Playthrough:":
                    print(line)
                else:
                    if line == current_sphere + ": {":
                        print(current_sphere + ": {")
                        current_sphere += 1
                    if line == "Always Required Locations:":
                        print("end of 'playthrough'")


