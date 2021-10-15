import random
import json



def LoadFromJson():
    with open ("FizzBuzzPlayers.json", "r", encoding= "UTF-8") as Myfile:
        FizzbuzzPlayers = json.load(Myfile)

        chancePlayer = FizzbuzzPlayers[1][random.randint(["ChanceMin"],["ChanceMax"])]
        chanceSinge = FizzbuzzPlayers[2][random.randint(["ChanceMin"],["ChanceMax"])]
        chanceChefSinge = FizzbuzzPlayers[3][random.randint(["ChanceMin"],["ChanceMax"])]
        print(chancePlayer, chanceChefSinge, chanceSinge)




if __name__ == "__main__":
    LoadFromJson()