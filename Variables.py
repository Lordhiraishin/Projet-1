# coding: utf-8

from typing import Text
import RichConsole as RC
import json





# general game data





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

Key1 = False
Key2 = False
Key3 = False

GameIsRunning = True


with open ("Data/MapElement.json","r",encoding="utf-8" ) as MyElementFile:
    MapData = json.load(MyElementFile)

    
#load map from textfile


    