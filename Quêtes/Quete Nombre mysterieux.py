# coding utf-8

#Import
import random 

#Variables

Reussite = 0
NbEssai = 0
proposition = -1
NbTrouve = 0
Reset = False

# Start the story of the quest
print("Bonjour explorateur ! Pour ouvrir la porte de la montagne, atteindre le cœur de l’île et rejoindre tes compagnons,  tu devras tout d’abord prouver ta valeur individuelle en gagnant les 3 clés que tu obtiendras en relevant les défis appropriés. Ceci est le premier d’entre eux.")
print()
print("3 fois de suite, tu devras deviner le nombre que j’ai en tête, tu as 20 essais maximum pour les  trouver tous, es-tu prêt ? ")


# Start the loop for the number guesses
for NbTrouve in range(0,3):
    NbSecret1 = random.randint(1,100)
    proposition = -1
    if Reset == True:
        break
    while proposition != NbSecret1:
        proposition = int(input("Devine le nombre entre 0 et 100:"))
        print(NbEssai)
        NbEssai = NbEssai + 1
        if NbEssai > 20:
            print("Tu n'a pas réussi à trouver à temps. Recommence !")
            Reset = True
            break
        if proposition < NbSecret1:
            print(" Le nombre que j’ai en tête est plus grand")
        elif proposition > NbSecret1:
            print("Le nombre que j’ai en tête est plus petit !")
        else:
            if NbTrouve == 0:
                print("Bravo, tu as réussi à trouver le premier nombre !")
            elif NbTrouve == 1:
                print("Bravo, tu as réussi à trouver le second nombre !")
            elif NbTrouve == 2:
                print("Bravo, tu as réussi à trouver le dernier nombre !")





            # while proposition2 != NbSecret2:
            #     proposition2 = int(input("Devine le nombre entre 0 et 100:"))
            #     print(NbEssai)
            #     NbEssai = NbEssai + 1
            #     if proposition2 < NbSecret2:
            #         print("C'est plus!")
            #     elif proposition2 > NbSecret2:
            #         print("C'est moins !")
            #     else:
            #         print("Bravo, tu as réussi à trouver le second nombre !")
            #         if NbEssai > 20:
            #             print("Tu n'a pas réussi à trouver à temps. Recommence !")



            #         while proposition3 != NbSecret3:
            #             proposition3 = int(input("Devine le nombre entre 0 et 100:"))
            #             print(NbEssai)
            #             NbEssai = NbEssai + 1
            #             if proposition3 < NbSecret3:
            #                 print("C'est plus!")
            #             elif proposition3 > NbSecret3:
            #                 print("C'est moins !")
            #             else:
            #                 print("Bravo, tu as réussi à trouver le dernier nombre !")
            #             if NbEssai > 20:
            #                 print("Tu n'a pas réussi à trouver à temps. Recommence !")
            #                 if NbEssai > 20:
            #                     print("Tu n'a pas réussi à trouver à temps. Recommence !")



# if NbEssai > 20:
#     print("Tu n'a pas réussi à trouver à temps. Recommence !")

# if proposition == NbSecret1 and proposition2 == NbSecret2 and proposition3 == NbSecret3:
    print("Félicitations, il ne t'a fallu que ", end="" )
    print(NbEssai, end="")
    print(" Essais. La clé est tienne")