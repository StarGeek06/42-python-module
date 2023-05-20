import matplotlib.pyplot as plt
from colorama import Fore
from termcolor import colored


print(f"{Fore.YELLOW}{'Bienvenue, sur ma plateforme'}{Fore.RESET}\n")
print("  -Pour voir le menu, tapez 1")
print("  -Pour quitter, tapez 2.\n")
s = 0
while s != 1 and s != 2:
    try:
        s = int(input("  Choix: "))
    except ValueError:
        print(f"{Fore.RED}{'Ceci nest pas un entier!'}{Fore.RESET}")
        s = input("Réessayez s'il vous plaît: ")


Match = []
Name = []
Surname = []
Note = []
Notes = []
Cred = []

while s == 1:
    print("Voulez-vous continuer?")
    print("   Entrez o, pour oui et")
    print("   Entrez n, pour non.\n\n")
    h = input("    Continue: ")
    if h == 'o' or h == 'O':
        print(f"{Fore.MAGENTA}{'<<-----Menu----->>'}{Fore.BLACK}")
        print(" 1- Enregistrez les informations des etudiants.")
        print(" 2- Voir les statistiques.")
        print(" 3- Cherchez les informations d'un etudiant.")
        print(" 4- Modifier un nom.")
        print(" 5- Ajouter un nom. ")
        print(" 6- Enregistrez les informations dans un fichier.")
        print(" 7- Afficher l'histogramme")

        choice = int(input("   Votre Choix:  "))

        if choice == 1:

            Eff = int(input("Effectif de la classe: "))

            for i in range(0, Eff):
                print(f"{Fore.CYAN}{'**********<< Etudiant {} >>**********'}{Fore.LIGHTMAGENTA_EX}".format(i + 1))
                nom = input(colored(" Nom: ",attrs=["underline"]))
                Name.append(nom)
                prenom = input(colored(" Prenom: ",attrs=["underline"]))
                Surname.append(prenom)
                print("Combien de matieres voulez vous enregistrez pour {}?".format(prenom))
                mat = int(input(""))
                print("Et combien de notes par matiere ?")
                note = int(input(""))
                print("Ainsi, procedons a l'enregistrement...")
                moy = 0

                for j in range(0, mat):
                    print(f"{Fore.CYAN}{'**** Matiere {} ****'}{Fore.BLUE}".format(j + 1))
                    moymat = 0
                    for k in range(0, note):
                        notes = int(input(colored("Note {}:".format(k+1),attrs=["underline"])))
                        Note.append(notes)
                        while ((notes < 0) or (notes > 20)):
                            print(f"{Fore.RED}{'Veuillez entrez une valeur comprise entre 0 et 20 PLEASE!!!'}{Fore.BLACK}")
                            notes = int(input("Note {}:".format(k + 1)))
                            Note.append(notes)

                        moymat += notes
                    total = moymat / note
                    Notes.append(Note)
                    moy += total
                moyenne = moy / mat

                print((colored("Moyenne: {}\n".format(moyenne),attrs=["underline"])))
                Match.append(moyenne)

        if choice == 2:
            for x, y, z in zip(Name, Surname, Match):
                print(f"{Fore.GREEN}{'{} {} : {}'.format(x, y, z)}{Fore.LIGHTGREEN_EX}")


        if choice == 3:
            search_word = input("Quel est le nom que vous recherchez: ")
            for z in Name:
                if search_word == z:
                    a = Name.index(search_word)
                    print(search_word, Surname[a], Match[a])

        if choice == 4:
            print("Vous voulez modifiez un nom(N), un prenom(P) ou les deux(D)?")
            choose = input("Entrez votre reponse: ")
            if choose == "N" or choose == "n":
                nme = input("Entrez le nom que vous voulez modifiez: ")
                for g in Name:
                    if nme not in Name:
                        print("Ce nom n'est pas dans la liste.")
                        nme = input("Réessayez: ")
                    if nme == g:
                        nme_chge = input("Entrez le nouveau nom: ")
                for h in range(len(Name)):
                    if Name[h] == nme:
                        Name[h] = nme_chge

                print("La tentative de modification a été un succès!")
                print("Voulez-vous voir le resultat?")
                see_value = input("Oui ou Non (O ou N): ")
                if see_value == 'o' or see_value == 'O' or see_value == 'Oui' or see_value == 'OUI':
                    b = Name.index(nme_chge)
                    print(nme_chge, Surname[b], Match[b])
                else:
                    print("Okay, Boff!")


            elif choose == "P" or choose == "p":
                snme = input("Entrez le prenom que vous voulez modifiez: ")
                snme_chge = input("Entrez le nouveau prenom: ")
                for x in Surname:
                    if snme is not Surname:
                        print("Ce prénom n'est pas dans la liste.")
                        snme = input("Réessayez: ")
                for h in range(len(Surname)):
                    if Surname[h] == snme:
                        Surname[h] = snme_chge
                print("La tentative de modification a été un succès!")
                print("Voulez-vous voir le resultat?")
                see_pvalue = input("Oui ou Non (O ou N): ")
                if see_pvalue == 'o' or see_pvalue == 'O' or see_pvalue == 'Oui' or see_pvalue == 'OUI':
                    c = Surname.index(snme_chge)
                    print(Name[c], snme_chge, Match[c])
                else:
                    print("Okay, Boff!")


            elif choose == "D" or choose == "d":
                name = input("Entrez le nom que vous voulez modifiez: ")
                name_chge = input("Entrez le nouveau nom: ")
                surname = input("Entrez le prenom que vous voulez modifiez: ")
                surname_chge = input("Entrez le nouveau prenom: ")
                for w in Name:
                    if name is not Name:
                        print("Ce nom n'est pas dans la liste.")
                        name = input("Réessayez: ")
                for q in Surname:
                    if surname is not Surname:
                        print("Ce nom n'est pas dans la liste.")
                        surname = input("Réessayez: ")
                for f in range(len(Name)):
                    if Name[f] == name:
                        Name[f] = name_chge
                for g in range(len(Surname)):
                    if Surname[g] == surname:
                        Surname[g] = surname_chge
                print("La tentative de modification a été un succès!")
                print("Voulez-vous voir le resultat?")
                see_dvalue = input("Oui ou Non (O ou N): ")
                if see_dvalue == 'o' or see_dvalue == 'O' or see_dvalue == 'Oui' or see_dvalue == 'OUI':
                    p = Name.index(name_chge)
                    t = Surname.index(surname_chge)
                    for v in Name:
                        if v == name_chge:
                            print(v, Surname[p], Match[p])
                    for y in Surname:
                        if y == surname_chge:
                            print(Name[t], y, Match[t])
                else:
                    print("Okay, Boff!")
            else:
                print("Okay...")


        if choice == 5:
            quest = int(input("Combien d'eleves voulez-vous ajoutez? "))
            for i in range(quest):
                new_name = input("Entrez le nouveau nom: ")
                new_surname = input("Entrez le nouveau prenom: ")
                Name.append(new_name)
                Surname.append(new_surname)
                print("Combien de matieres voulez vous enregistrez pour {}?".format(new_surname))
                matieres = int(input(""))
                print("Et combien de notes par matiere ?")
                pad = int(input(""))
                print("Ainsi, procedons a l'enregistrement...")
                moy = 0

                for x in range(0, matieres):
                    print("**** Matiere {} ****".format(x + 1))
                    moymat = 0
                    for r in range(0, pad):
                        notes = int(input("Note {}:".format(r + 1)))
                        while ((notes < 0) or (notes > 20)):
                            print("Veuillez entrez une valeur comprise entre 0 et 20 s'il vous plait !!!")
                            notes = int(input("Note {}:".format(r + 1)))
                        moymat += notes
                    total = moymat / pad
                    moy += total
                new_average = moy / matieres
                print("Moyenne: {}\n".format(new_average))
                Match.append(new_average)

        if choice == 6:
            print("Voulez-vous enregistrez le fichier en pdf ou en txt?")
            print(" -Entrez P pour pdf,")
            print(" -Entrez T pout txt.")
            Stock = input("Choisissez l'extension: ")
            if Stock == "P" or Stock == "p":

                from reportlab.lib.pagesizes import letter
                from reportlab.lib import colors
                from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

                pdf_filename = "Bulletin.pdf"

                document = SimpleDocTemplate(pdf_filename, pagesize=letter)
                donnees_bulletins = [["Nom", "Prénom"] + ["Note {}".format(z + 1) for z in range(len(Notes[0]))]]

                for nom, prenom, ligne_notes in zip(Name, Surname, Notes):
                    donnees_bulletins.append([nom, prenom] + ligne_notes)

                table = Table(donnees_bulletins)

                table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))

                elements = [table]
                document.build(elements)
                print(f"Le fichier PDF '{pdf_filename}' a été créé avec succès.")









        if choice == 7:
            couleurs = []
            for k in Match:
                if k <= 7:
                    couleurs.append('red')
                elif k < 13:
                    couleurs.append('orange')
                elif k < 16:
                    couleurs.append('purple')
                elif k < 18:
                    couleurs.append('yellow')
                elif k <= 20:
                    couleurs.append('green')
            plt.bar(Surname, Match, color=couleurs, edgecolor='black', label="ValidationMat")
            plt.xlabel("Prenoms")
            plt.ylabel("Moyenne")
            plt.legend()
            plt.grid(color="black")
            plt.show()
        



    elif h == 'N' or h == 'n':
        break
    else:
        print("Cette lettre ne convient a aucune requête.")
        h = input("Réessayez: ")

if s == 2:
    print("Bien, A vos ordres!")

if s != 1 or s != 2:
    print("Ce chiffre ne correspond à aucune option dans le menu.")



