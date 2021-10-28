import RichConsole as RC
from typing import Text
import json
import Variables as Var

with open ("DessinCarte","r",encoding = "utf-8") as MyFile:
    MapData = MyFile.readlines()

Symbol = Var.PlayerData["Symbol"]
FG = Var.PlayerData["Foreground"]
BG = Var.PlayerData["Background"]
# MapElement = Var.MapElements['Symbol']
# print(MapElement)

#load map from textfile

def drawmap():
    for i in MapData:
        for j in i:
            element = j
            if element == "m":
                print("∆",end="")
            elif element == "j":
                print("ͳ", end="")
            elif element == "e":
                print("Í", end = "")
            elif element == "p":
                print("░",end = "")
            elif element == "X":
                print("x",end = "")
            elif element == "":
                print("\n")



if __name__ == "__main__":
    drawmap()


# def drawplayer():
#     RC.ColorPrintAt(Symbol,y=Var.PlayerData["Y"],x=Var.PlayerData["X"])


3/26
3/49
21/14
26/27