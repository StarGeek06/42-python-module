print("Bienvenue sur ma plateforme de jeu.")
print("Ce jeu est intitulé <Plus ou Moins>, oui oui je sais vous ne cernez pas encore le jeu,")
print("Je vais vous expliquez!\n")

print("Regles de Jeu:\n")

print("Jeu Solitaire:")
print("Le principe de ce jeu est de deviner le nombre entré par le programmeur.\nLorsque le nombre que vous entrez est ,")
print("superieur au nombre il vous le signale par <Too Low>, Lorsqu'il est plus grand il vous le signale par <Too High>.Lorsque ")
print("vous ne le trouvez pas au bout de 5 essais..., Bah vous perdez!\n")

print("Jeu en Binôme:")
print("Le but du jeu en fait est que l'un des joueurs entre un nombre caché bien sur,  et a l'autre de le ")
print("trouver.")

print("Les regles étant fixées! \n Pour jouer Solitaire tapez S \n Pour jouer en binôme, tapez B.\n")
choice = input("Allez, choisissez: ")
if choice == 'S' or choice == 's':
    print("Ah! Option Solitaire....")
    print("J'aimerai bien voir comment vous allex reussir a trouver le vrai nombre\nparmi 5000 nombres..")
    print("Bref, Bonne Chance.")
    import random
    num_real = random.randint(1, 500)

    fail_counts = 10
    print("Devinez un nombre entre 1 et 5000.\nVous avez 10 chances.")

    while (fail_counts > 0)  :
        choose = int(input("Entrez votre choix : "))
        if choose == num_real:
            print("Congratulations! Je vous ai sous-estimé.")
            break
        elif choose < num_real:
            print("Trop petit!")
        else:
            print("Trop Grand!")
        fail_counts -= 1
        print("Il vous reste", fail_counts, "chances.")
    if (fail_counts == 0) :
        print("Comme je l'avais dit, vous avez perdu!. C'était juste",num_real)


elif choice == 'B' or choice == 'b':
    import random
    from getpass import getpass
    print("Okay,")
    Joueurs = []
    fail = 10
    joueur_1 = input("Entrez le nom du joueur 1: ")
    joueur_2 = input("Entrez le nom du joueur 2: ")
    Joueurs.append(joueur_1)
    Joueurs.append(joueur_2)
    print("Bon on va tirer au sort!")
    guess_2 = getpass("{} entre un nombre que tu veux que {} devine: ".format(joueur_2, joueur_1))
    while (fail > 0)  :
        guess_1 = input("{} entre le nombre que tu penses avoir vu: ".format(joueur_1))
        if guess_1 == guess_2:
            print("Congratulations! Je vous ai sous-estimé.")
            break
        elif guess_1 < guess_2:
            print("Trop petit!")
        else:
            print("Trop Grand!")
        fail -= 1
        print("Il vous reste", fail, "chances.")
    if (fail == 0) :
        print("Comme je l'avais dit, vous avz perdu!. C'était juste {}".format(guess_2))
        
else:
    print("Cette lettre n'est pas une option")
    print("Réessayez: ")
    choice = input("Continue: ")
     
