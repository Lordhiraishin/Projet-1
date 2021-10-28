# coding utf-8

# Imports
import json
import random
import time
import Variables

# Variables

GoodAnswer = True
nb = 1
nbSinge = 1
Fizz = "Fizz !"
Buzz = "Buzz !"
Fizzbuzz = "FizzBuzz !"



# Functions
def FizzBuzz():
    """
    Launch the fizzbuzz quest
    """

    print("En explorant la jungle, tu remarques une bande de singes braillards évoluant dans les arbres. En écoutant avec un  peu plus d’attention, tu te rends comptes que les singes semblent articuler des nombres et que deux sons  reviennent régulièrement : Fizz et Buzz… ")
    print("À un moment, les cris s’arrêtent et tu te retrouves subitement entouré par les singes.")
    print("L’un d’eux, probablement le chef vu sa démarche assurée, descend de l’arbre et s’approche de toi. Il te toise un  instant puis, du doigt, te désigne un endroit en hauteur. En levant la tête, tu aperçois une grosse clé en or, pendue  à une solide liane, tu commences à chercher un moyen de grimper dans les arbres, mais cela déclenche une vive  réaction de la part des singes. Il semble qu’ils ne soient pas disposés à te donner la clé comme ça !")
    print("Tu te ravises alors, et le chef se rapproche de toi et commence à te parler…")
    print("« Toi jouer ! Si gagner alors clé à toi ! »")
    print("Jouer ? Mais à quoi ? ")
    print("Semblant lire dans tes pensées, le chef dit alors « Nous montrer. » Puis il dit « 1 ». Un autre singe dans les arbres  dit alors « 2 », puis un troisième « Fizz » et ainsi de suite : « 4 », « Buzz », « Fizz », « 7 », « 8 », « Fizz », « Buzz »,  « 11 », « 12 »")
    print(" À ce moment, tous les autres singes se mettent à rire et celui qui vient d’annoncer 12 pousse un  cri de déception et se retourne sur sa branche en boudant, puis le jeu recommence avec les singes restants : « 1 »,  « 2 », « Fizz »…")
    print("Au bout de quelques tours tu comprends le principe du jeu et tu tentes ta chance pour obtenir la clé.")
    print()


    with open ("FizzBuzzPlayers.json", encoding= "UTF-8") as SingeFile:
            FizzbuzzPlayers = json.load(SingeFile)

# load players name and chance from json file


    listPlayer = []

    for players in range(len(FizzbuzzPlayers)):
        listPlayer.append(FizzbuzzPlayers[players]["Name"])
        # print(listPlayer)
 #fill an empty list with the player names from the json


    FirstPlayer = random.randint(0,len(listPlayer)-1)
    print(f"Le premier joueur est {listPlayer[FirstPlayer]}")

    #Randomize the first player from one within the list and after first player is the player playing this turn

    PremierChiffre = 1

    print(f"{listPlayer[FirstPlayer]} dit : {PremierChiffre}")

    ChanceSinge = random.randint(FizzbuzzPlayers[5]["ChanceMin"],FizzbuzzPlayers[5]["ChanceMax"])
    ChanceChefSinge = random.randint(FizzbuzzPlayers[10]["ChanceMin"],FizzbuzzPlayers[10]["ChanceMax"])
    ChancePlayer = random.randint(FizzbuzzPlayers[0]["ChanceMin"],FizzbuzzPlayers[0]["ChanceMax"])

# Get the chance of each player randomly within the minimum chance given and the maximum chance given

    GameTurn = True
    while GameTurn == True:

        #Game is starting

        if FirstPlayer >=  len(listPlayer)-1:
            FirstPlayer = 0
        else:
            FirstPlayer += 1

        




        chance = random.randint(0,100)

        #choose a random number, if > to the player chance, he loose

        if len(listPlayer) > 1:

            #The game is running till there is only one player left

            if listPlayer[FirstPlayer] == FizzbuzzPlayers[10]["Name"]:
                if chance > ChanceChefSinge:
                    print("Le chef singe à perdu !")
                    listPlayer.pop(FirstPlayer)
                    #delete the player from the list when he loose
                else:
                    PremierChiffre +=1
                    if PremierChiffre%3 == 0 and PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizzbuzz}")
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
                    #delete the player from the list when he loose
                else:
                    PremierChiffre +=1
                    if PremierChiffre%3 == 0 and PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizzbuzz}")
                    elif PremierChiffre%3 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizz}")
                    elif PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Buzz}")
                    else:
                        print(f"{listPlayer[FirstPlayer]} dit : {PremierChiffre}")
            else: 
                if ChanceSinge < chance:
                    print(f"{listPlayer[FirstPlayer]} a perdu ! ")
                    listPlayer.pop(FirstPlayer)
                    #delete the player from the list when he loose
                else:
                    PremierChiffre +=1
                    if PremierChiffre%3 == 0 and PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizzbuzz}")
                    elif PremierChiffre%3 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Fizz}")
                    elif PremierChiffre%5 == 0:
                        print(f"{listPlayer[FirstPlayer]} dit : {Buzz}")
                    else:
                        print(f"{listPlayer[FirstPlayer]} dit : {PremierChiffre}")

                
            

        else:
            print(f"Le vainqueur est : {listPlayer[FirstPlayer]}")
            Variables.Key3
            GameTurn = False
            #reveal the winner and stop the game when there is only one player left
            
                    
        time.sleep(0.5)    
        #put some time beetwen each player answer, allow the game to be more understandable



if __name__ == "__main__":
    FizzBuzz()