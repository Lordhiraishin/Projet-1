# coding : utf-8

#Imports
from os import replace
import random

#Variables
PlayerName = ""
ZenPython = "beautiful is better than ugly explicit is better than implicit simple is better than complex"
lZenPython = list(ZenPython)
Alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encodeKey = random.randint(0,25)
test = "abcdefghijklmnopqrstuvwxyz"
tryNumber = 0






#functions
def CodeCesar():

    print("Au nord de la plage, tu trouves un petit temple taillé dans la paroi rocheuse. Au-dessus de l’arche d’entrée, est  écrit un message dans une langue apparemment inconnue mais utilisant l’alphabet habituel. ")
    print("Sur les colonnes de l’arche, sont d’ailleurs gravées en relief toutes les lettres de l’alphabet. Curieux, tu appuies au  hasard sur l’une des lettres et tu t’aperçois que les lettres formant le message changent. Malgré cela, le message  en lui-même reste incompréhensible. En effectuant plusieurs tests, tu te rends compte qu’a une lettre définie  correspond une composition spécifique du message. Ne voyant pas trop quoi faire d’autre pour le moment, tu  décides d’entrer dans le temple")
    print("À l’intérieur, tout le sol est recouvert de sable. Au milieu de la petite pièce, se trouve un autel avec une niche  fermée par une grille apparemment sans serrure. À l’intérieur de la niche tu vois une grosse clé en argent  (inatteignable tant que la grille est en place). À côté de la niche, un écriteau en bois indique : « Récite le crédo du  Python, puis trace ton nom secret ». ")
    print("")

    UserName = input("Quel est votre nom ?")

    letter = ZenPython[1]
    indexLetter = test.index(letter)

    #Get the position of the first letter of the zen of python in the alphabet

    newAlphabet = ""
    CodedUserName = "" 
    CorrectAnswer = False

    print(ZenPython)


    for i in range(0,26):
        newLetter = Alphabet[i + encodeKey]
        newAlphabet += newLetter

        #for each letter in the alphabet, get is replacement in the new alphabet encoded with a random key
    
        
    print()
    codedKey = newAlphabet.index(letter)


    for Letter in range(len(ZenPython)):
        Letter = ZenPython[Letter]
        
        if Letter == " ":
            print(" ",end="")
        else:
            LetterIndex = Alphabet.index(Letter)
            encodedLetter = newAlphabet[LetterIndex]
            print(encodedLetter,end="")

            #Encode each letter of the zen into its encoded self, but do not modify the space

    print()


    for Secret in range(len(UserName)):
        iLetter = UserName[Secret]
        iLetterIndex = Alphabet.index(iLetter)
        iLetter = newAlphabet[iLetterIndex]
        CodedUserName = CodedUserName+ iLetter

        #Take the player username and encode it letter by letter to get the correct answer the player has to enter to win




    while CorrectAnswer == False:
        if CodedUserName == input("Quel est ton nom codé?"):
            print("félicitation, tu as gagné la deuxième clé")
            CorrectAnswer == True
            break
        else:
            print("non, essaye encore")
            tryNumber = tryNumber +1

            #The player guess his encoded name, if he's right end the game, else another guess
        


if __name__ == "__main__":
    CodeCesar()

# Reconnaitre player name, -> afficher zen python modifier -> demander input lettre -> modif grace table ascii en effectuant un roulement
# de toute les lettres avec la variable apporté par le joueur -> quand le joueur est pret, rentrer son nom codé -> verif 

