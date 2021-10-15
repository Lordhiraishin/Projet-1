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
list =[
    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ]
CodedUserName = "" 
CorrectAnswer = False
# lAlphabet = list(Alphabet)
# print(f"La clé est{encodeKey}")
# print(lZenPython)
# print(lAlphabet)

# print(encodeKey)
# print(test[encodeKey])
newAlphabet = ""

UserName = input("Quel est votre nom ?")
# print(ZenPython[0])
letter = ZenPython[1]
indexLetter = test.index(letter)
# print(indexLetter)
print(ZenPython)


for i in range(0,26):
    newLetter = Alphabet[i + encodeKey]
    newAlphabet += newLetter
    # print(Alphabet[i + encodeKey], end ="")
    
print()
codedKey = newAlphabet.index(letter)
# print(codedKey)
# print(Alphabet[encodeKey])

for Letter in range(len(ZenPython)):
    Letter = ZenPython[Letter]
    # print(Letter)
    if Letter == " ":
        print(" ",end="")
    else:
        LetterIndex = Alphabet.index(Letter)
        encodedLetter = newAlphabet[LetterIndex]
        print(encodedLetter,end="")

print()


for Secret in range(len(UserName)):
    iLetter = UserName[Secret]
    iLetterIndex = Alphabet.index(iLetter)
    iLetter = newAlphabet[iLetterIndex]
    CodedUserName = CodedUserName+ iLetter

# print(CodedUserName)


while CorrectAnswer == False:
    if CodedUserName == input():
        print("félicitation, tu as gagné la deuxième clé")
        CorrectAnswer == True
        break
    else:
        print("non, essaye encore")
        




# Reconnaitre player name, -> afficher zen python modifier -> demander input lettre -> modif grace table ascii en effectuant un roulement
# de toute les lettres avec la variable apporté par le joueur -> quand le joueur est pret, rentrer son nom codé -> verif 

