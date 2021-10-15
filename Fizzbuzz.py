# coding utf-8

# Imports
import json
import random

# Variables

GoodAnswer = True
nb = 1
# chanceSinge = 30
# chanceChefSinge = 70
# chancePlayer = 80
nbSinge = 1
Fizz = "Fizz !"
Buzz = "Buzz !"
FizzBuzz = "FizzBuzz !"

# GameStart = True



# Functions


with open ("FizzBuzzPlayers.json", encoding= "UTF-8") as SingeFile:
        FizzbuzzPlayers = json.load(SingeFile)

    
while GoodAnswer == True:
    
    listPlayer = []

    for players in range(len(FizzbuzzPlayers)):
        listPlayer.append(FizzbuzzPlayers[players]["Name"])
        # print(listPlayer)
        

    FirstPlayer = random.randint(0,len(listPlayer)-1)
    print(f"Le premier joueur est {listPlayer[FirstPlayer]}")

    PremierChiffre = 1

    print(f"{listPlayer[FirstPlayer]} dit : {PremierChiffre}")

    GameTurn = True
    while GameTurn == True:

        if FirstPlayer >= len(listPlayer)-1:
            FirstPlayer = 0
        else:
            FirstPlayer += 1

        PremierChiffre +=1


        # ChanceSinge = random.randint(FizzbuzzPlayers[10][players]["ChanceMin"],FizzbuzzPlayers[players]["ChanceMax"])
        # ChanceChefSinge = random.randint(FizzbuzzPlayers[9][players]["ChanceMin"],FizzbuzzPlayers[players]["ChanceMax"])
        # ChancePlayer = random.randint(FizzbuzzPlayers[0][players]["ChanceMin"],FizzbuzzPlayers[players]["ChanceMax"])
        # print(ChanceChefSinge)
        # print(ChancePlayer)
        # print(ChanceSinge)

        ChanceSinge = 30
        ChanceChefSinge = 70
        ChancePlayer = 80
        chance = random.randint(0,100)

        if len(listPlayer) > 1:

            if listPlayer[FirstPlayer] == FizzbuzzPlayers[10]["Name"]:
                if chance > ChanceChefSinge:
                    print("Le chef singe à perdu !")
                    listPlayer.pop(FirstPlayer)
                else:
                    if PremierChiffre%3 == 0 and PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {FizzBuzz}")
                    elif PremierChiffre%3 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizz}")
                    elif PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Buzz}")
                    else:
                        print(f"{listPlayer[FirstPlayer]} dit : {PremierChiffre}")
            elif listPlayer[FirstPlayer] == FizzbuzzPlayers[0]["Name"]:
                if ChancePlayer < chance:
                    print(f"{listPlayer[FirstPlayer]} a perdu ! ")
                    print(f"Vous avez perdu le FizzBuzz")
                    listPlayer.pop(FirstPlayer)
                else:
                    if PremierChiffre%3 == 0 and PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {FizzBuzz}")
                    elif PremierChiffre%3 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizz}")
                    elif PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Buzz}")
                    else:
                        print(f"{listPlayer[FirstPlayer]} dit : {PremierChiffre}")
            elif listPlayer[FirstPlayer] == FizzbuzzPlayers[5]["Name"]:
                if ChanceSinge < chance:
                    print(f"{listPlayer[FirstPlayer]} a perdu ! ")
                    listPlayer.pop(FirstPlayer)
                else:
                    if PremierChiffre%3 == 0 and PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {FizzBuzz}")
                    elif PremierChiffre%3 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizz}")
                    elif PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Buzz}")
                    else:
                        print(f"{listPlayer[FirstPlayer]} dit : {PremierChiffre}")

                print(listPlayer)

        else:
            print(f"Le vainqueur est : {listPlayer[FirstPlayer]}")
            break
