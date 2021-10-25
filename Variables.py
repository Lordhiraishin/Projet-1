# coding: utf-8

from typing import Text
import RichConsole as RC




# general game data

GameIsRunning = True
PossibleActions = {
    "H" : { "DeltaY" : -1, "DeltaX" : 0}, 
    "B" : { "DeltaY" : 1, "DeltaX" : 0}, 
    "G" : { "DeltaY" : 0, "DeltaX" : -1}, 
    "D" : { "DeltaY" : 0, "DeltaX" : 1}, 
    "Q" : { "DeltaY" : 0, "DeltaX" : 0}
}
PlayerData = {
    "Symbol": "֍",
    "Foreground": "WHITE",
    "Background": "BLACK",
    "X": 48,
    "Y": 27,
    "LastDirection": "",
    "Username" : ""
}


TextLine = 0



# map elements
MapElements = {
    "m" : {
        "Symbol" : "∆",
        "Foreground": "RED",
        "Background": "RED",
        "Name": "Montagne",
        "CanWalk": False
    },
    "e" : {
        "Symbol" : "Í",
        "Foreground" : "BLUE",
        "Background" : "BLUE",
        "Name" : "Eau",
        "CanWalk": False

    },
    "j" : {
        "Symbol": "ͳ",
        "Foreground": "GREEN",
        "Background": "GREEN",
        "Name": "Jungle",
        "CanWalk": True
    },
    "p": {
        "Symbol": "░",
        "Foreground": "YELLOW",
        "Background": "YELLOW",
        "Name": "Plage",
        "CanWalk": True
    },
    "X" : {
        "Symbol": "X",
        "Foreground": "PURPLE",
        "Background": "WHITE",
        "Name": "Quête",
        "CanWalk": True
    }
}

# m = MapElements[0]
# e = MapElements[1]
# j = MapElements[2]
# p = MapElements[3]
# x = MapElements[4]

# map data (2D list)

# x1 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]
# x2 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]
# x3 = [m,m,m,m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,x,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m,m,m,m,x,m]
# x4 = [m,m,m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m]
# x5 = [m,m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m]
# x6 = [m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m,m,m]
# x7 = [m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,m,m,m,m]
# x8 = [m,m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,e,e,e,e,e,j,j,j,j,j,j,j,m,m,m,m,j,e,e,e,e,e]
# x9 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,m,m,p,p,e,e,e,e]
# x10 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,m,m,p,p,p,p,e,e,e,e]
# x11 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,m,m,p,p,p,p,p,p,p,e]
# x12 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p]
# x13 = [m,m,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,e]
# x14 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,e,e,e]
# x15 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,e,e]
# x16 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p,p]
# x17 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p,p]
# x18 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,e,e]
# x19 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p]
# x20 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p]
# x21 = [e,e,j,j,j,j,j,j,j,j,j,j,j,x,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,e,e]
# x22 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,p]
# x23 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,p,e]
# x24 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,e]
# x25 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p]
# x26 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,x,m,m,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p]
# x27 = [e,e,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,m,m,m,m,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,e,e]
# x28 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]
# x29 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]
# x30 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

# MapData = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30]

with open ("DessinCarte","r",encoding = "utf-8") as MyFile:
    MapData = MyFile.readlines()

#load map from textfile

def drawmap():
    for i in MapData:
        for j in i:
            RC.ColorPrintAt(j)
    