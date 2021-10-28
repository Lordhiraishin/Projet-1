# coding: utf-8

# imports
import json
from Map import drawmap
import Variables as Var
import RichConsole as RC
from Map1 import Drawmap
from NombreMysterieux import NombreMysterieux
import CodeCesar
import Fizzbuzz



# variables
Start = False
PlayerY = Var.PlayerData["Y"]
PlayerX = Var.PlayerData["X"]


# functions

def Draw(Erase = False):
    """
        Draw player on map
    """

    Symbol = Var.PlayerData["Symbol"]
    FG = Var.PlayerData["Foreground"]
    BG = Var.PlayerData["Background"]

    # MapElement = Var.MapElements[
    #     Var.MapData[Var.PlayerData["Y"] - 1]
    #     [Var.PlayerData["X"] - 1]]
    # # check if player is beeing erased
    # if Erase:
    #     Symbol = MapElement["Symbol"]
    #     FG = MapElement["Foreground"]
    #     BG = MapElement["Background"]

    # draw symbol at right place
    RC.ColorPrintAt(
        Symbol,
        FG,
        BG,
        PlayerY,
        PlayerX)




def Move(Direction):
    """
        Moves player in specified direction
        Direction -> str : direction to move
    """
    
    # print(f"Le joueur se déplace vers {Direction}")

    # save actual player position




while Start == False:
    Drawmap()
    Draw()
    RC.ColorPrintAt("","","",51,1)
    Direction = input("Dans quelle direction voulez vous allez ? (H)aut, (B)as, (G)auche, (D)roite,(Q)uitter le jeu").upper()

    # calculate new player position
    # PlayerY += Var.PossibleActions[Direction]["DeltaY"]
    # PlayerX += Var.PossibleActions[Direction]["DeltaX"]
    if PlayerY == 26 and PlayerX == 27:
            NombreMysterieux()
    else:
        if Direction == "H":
            PlayerY -= 1
        elif Direction == "B":
            PlayerY += 1
        elif Direction == "G":
            PlayerX -= 1
        elif Direction == "D":
            PlayerX += 1
        elif Direction == "Q":
            break
        Draw()

    

    # # check if movement is valid
    # MapElementAtPlayerPosition = Var.MapData[PlayerY - 1][PlayerX - 1]
    # MapElementData = Var.MapElements[MapElementAtPlayerPosition]
    # if MapElementData["CanWalk"]:
    #     Draw(True)
    #     Var.PlayerData["Y"] = PlayerY
    #     Var.PlayerData["X"] = PlayerX
    #     Draw()
    #     if MapElementAtPlayerPosition == "S":
    #         Var.GameIsRunning = False
    #         RC.ColorPrintAt(
    #             "\nBRAVO, tu as trouvé la sortie.",
    #             Y=Var.TextLine+2,
    #             X=1)
    # else:
    #     # obstacle
    #     print(f"Aïe, un {MapElementData['Name']} !")


