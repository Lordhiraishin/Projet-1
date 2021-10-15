# coding: utf-8

# imports
import json
# import Variables as Var
# import RichConsole as RC

# variables

# functions
def LoadFromFile(map1):
    """
        Load map from text file
        Map with specified number from MapFolder
        MapNumber -> int : number of the map to load
    """
    #  try:
    #     # load map data from text file
    #     with open(f"{Var.MapFolder}Map {MapNumber}", "r", encoding="utf-8") as MyFile:
    #         MapData = MyFile.readlines()



    def DrawMap():
        """
            Draw map on screen from MapData 2D list
        """

        RC.ClearConsole()

        # each line in 2D list
        for Y, Line in enumerate(Var.MapData):
            # for each column in current line
            for X, Character in enumerate(Line):
                # get map element data from dictionnary
                # matching current character in 2D list
                MapElement = Var.MapElements[Character]
                # print map element at coordinates
                RC.ColorPrintAt(
                    MapElement["Symbol"],
                    MapElement["Foreground"],
                    MapElement["Background"],
                    Y+1,
                    X+1)