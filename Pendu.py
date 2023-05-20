import random
from colorama import Fore
trying = 5
Mots_facile = ["chat", "chien", "maison", "soleil", "arbre", "fleur", "jour", "nuit", "mer", "montagne",
    "vélo", "voiture", "avion", "train", "bus", "école", "livre", "stylo", "café", "gâteau",
    "pomme", "orange", "banane", "tomate", "fromage", "pain", "jardin", "parc", "piscine", "musique",
    "danse", "football", "basketball", "tennis", "guitare", "piano", "dessin", "peinture", "photo", "film",
    "théâtre", "parler", "écouter", "lire", "écrire", "manger", "boire", "courir", "sauter", "nager",
    "voler", "dormir", "rire", "pleurer", "travailler", "jouer", "voyager", "apprendre", "aimer", "partager",
    "donner", "recevoir", "venir", "aller", "entrer", "sortir", "regarder", "voir", "écouter", "entendre",
    "sourire", "chanter", "cuisiner", "acheter", "vendre", "aider", "comprendre", "parler", "penser", "souvenir",
    "oublier", "essayer", "aimer", "détester", "besoin", "bonjour", "merci", "excusez-moi", "au revoir", "oui",
    "non", "peut-être", "maintenant", "demain", "hier", "heure", "jour", "semaine", "mois", "année"]

Mots_moy = ["intéressant", "différent", "sérieux", "important", "particulier", "curieux", "responsable", "suffisant", "prudent",
    "confortable", "original", "significatif", "précieux", "moderne", "efficace", "agréable", "remarquable", "élégant",
    "inoubliable", "harmonieux", "satisfaisant", "chaleureux", "sensible", "magnifique", "médiocre", "trivial", "banal",
    "complex", "considérable", "exigeant", "subtil", "redoutable", "essentiel", "perceptible", "fiable", "respectable",
    "abordable", "accessible", "adéquat", "authentique", "consistant", "durable", "accessible", "pratique", "agile",
    "cohérent", "compatible", "économique", "flexible", "rentable", "stable", "valable", "viable", "évident",
    "fondamental", "persuasif", "profond", "rationnel", "réfléchi", "résistant", "réussi", "savoureux", "séduisant",
    "spirituel", "étonnant", "excellent", "extraordinaire", "fantastique", "formidable", "impressionnant", "merveilleux",
    "exceptionnel", "brillant", "créatif", "innovant", "stimulant", "captivant", "inspirant", "pétillant", "excitant",
    "exquis", "majestueux", "majestueux", "prodigieux", "glorieux", "gracieux", "imposant", "magnanime", "mémorable",
    "mystérieux", "plaisant", "réjouissant", "éblouissant", "splendide", "délicieux", "intelligent", "perspicace",
    "philosophique", "révélateur", "sublime", "superbe", "tranchant", "unique", "vif"]

Mots_diff = ["épigénétique", "pléthore", "ubiquité", "quintessence", "oxymore", "équinoxe", "inexorable", "dithyrambe", "abyssal",
    "satrape", "égrégore", "fustiger", "népotisme", "prévarication", "vacuité", "éristique", "lacrymal", "ploutocratie",
    "soporifique", "hégémonie", "inique", "diatribe", "cynisme", "sycophante", "nébuleux", "symbiose", "sagacité",
    "paroxysme", "caligraphe", "palimpseste", "circumnavigation", "époustouflant", "contempteur", "hémistiche", "péremptoire",
    "déférence", "lacune", "indolence", "mendacité", "apocryphe", "lucifuge", "pléonasm", "exacerbation", "panacée",
    "cryptomnésie", "contumace", "réification", "farfelu", "bucolique", "soliloque", "apodictique", "hiératique",
    "péremptoire", "égrillard", "extrapolation", "pyrrhonien", "néologisme", "stridulation", "herméneutique", "ambivalent",
    "épistolaire", "volubile", "acrimonie", "ébullition", "palabrer", "scabreux", "zénith", "subversif", "iconoclaste",
    "paradigme", "fébrile", "mélancolie", "moribond", "équivoque", "exécrable", "jubilatoire", "indigène", "chimérique",
    "omnipotent", "immarcescible", "immanent", "diaphane", "perspicace", "persiflage", "altruisme", "obséquieux",
    "sinécure", "élucubration", "exorbitant", "inconséquent", "lascif", "machiavélique", "contemptible", "innuendo",
    "quolibet", "vitupérer", "abracadabrant", "pétrichor", "vacuité", "fallacieux", "éristique", "exsangue"]

Mangas_name = [ "Naruto Uzumaki", "Goku", "Monkey D. Luffy", "Ichigo Kurosaki", "Light Yagami", "Eren Yeager",
    "Saitama", "Spike Spiegel", "Edward Elric", "Levi Ackerman", "Vegeta", "Lelouch Lamperouge",
    "Natsu Dragneel", "L Lawliet", "Kakashi Hatake", "Gon Freecss", "Guts", "Yusuke Urameshi",
    "Ryuk", "Mikasa Ackerman", "Killua Zoldyck", "Alucard", "Roronoa Zoro", "Kenshin Himura",
    "Sasuke Uchiha", "Inuyasha", "Gintoki Sakata", "Sanji Vinsmoke", "Yusuke Urameshi", "Roy Mustang",
    "Luffy", "Kaneki Ken", "Sesshomaru", "Gohan", "Sasori", "Gaara", "Broly", "Sora", "Kira Yoshikage",
    "Alphonse Elric", "Kurapika", "Rukia Kuchiki", "Katsuki Bakugo", "Shoto Todoroki", "Hinata Hyuga",
    "Rin Okumura", "Yugi Muto", "Nami", "Trafalgar D. Water Law", "Ryoma Echizen", "Koro-sensei",
    "Jotaro Kujo", "Sasori", "Mikasa Ackerman", "Jiraiya", "Saito Hajime", "Sosuke Aizen",
    "Shinji Ikari", "Kirito", "Asuna Yuuki", "Saber", "Rias Gremory", "Issei Hyodo", "Ryuko Matoi",
    "Satsuki Kiryuin", "Maka Albarn", "Black Star", "Nagisa Shiota", "Gon Freecss", "Kurama",
    "Hiei", "Kuwabara", "Genos", "Rei Ayanami", "Erza Scarlet", "Lucy Heartfilia", "Gray Fullbuster",
    "Natsu Dragneel", "Wendy Marvell", "Jellal Fernandes", "Mirajane Strauss", "Gaara", "Kankuro",
    "Temari", "Rock Lee", "Neji Hyuga", "Tsunade", "Jiraiya", "Kiba Inuzuka", "Shikamaru Nara",
    "Kisuke Urahara", "Yoruichi Shihoin", "Byakuya Kuchiki", "Kotaro Tatsumi", "Matoi Ryuko", "Satsuki Kiryuin",
    "Revy", "Balalaika", "Robert E.O. Speedwagon", "Joseph Joestar", "Eren Yeager", "Mikasa Ackerman",
    "Armin Arlert", "Levi Ackerman", "Eren"]



word_real_facile = random.choice(Mots_facile)
word_real_moyen = random.choice(Mots_moy)
word_real_diff = random.choice(Mots_diff)
word_real_anm = random.choice(Mangas_name)


print("Ah! Vous revoila, vous voulez jouez a mon jeu.\n")
print("Bien vous avez trois options:\n")
print("*Pour le niveau facile, tapez f;\n*Pour le niveau moyen tapez m;\n*Pour le niveau difficile tapez d;\nPour les noms d'animés, tapez a.")
choice = input("Bon j'ai pas que ca a faire, choisissez: ")

letters_find_f = []
long_words_f = "-" * len(word_real_facile)



if choice == 'f' or choice == "F":
    while trying > 0:
        print(f"{Fore.CYAN}{'Mot: {}'.format(long_words_f)}{Fore.BLACK}")
        letter_choose_f = input("Entrez une lettre que vous pensez être dans le mot:")
        if letter_choose_f in word_real_facile:
            print("La lettre est dans le mot !")
            letters_find_f.append(letter_choose_f)

            long_words_f = ""
            for i in range(len(word_real_facile)):
                if word_real_facile[i] in letters_find_f:
                    long_words_f += word_real_facile[i]
                else:
                    long_words_f += "-"

            if "-" not in long_words_f:
                print(f"{Fore.GREEN}{'Vous avez gagné! Le mot était', word_real_facile}{Fore.BLACK}")
                break
        else:
            print("Cette lettre n'est pas dans le mot.")
            trying -= 1
            print("Il vous reste", trying, "essai(s)")
            if trying == 0:
                print(f"{Fore.RED}{'Bah, vous avez perdu unh...., le mot était:', word_real_facile}{Fore.RED}")




letters_find_m = []
long_words_m = "-" * len(word_real_moyen)

if choice == 'm' or choice == 'M':
    while trying > 0:
        print("Mot:",long_words_m)
        letter_choose = input("Entrez une lettre que vous pensez être dans le mot:")
        if letter_choose in word_real_moyen:
            print("La lettre est dans le mot !")
            letters_find_m.append(letter_choose)

            long_words_m = ""
            for j in range(len(word_real_moyen)):
                if word_real_moyen[j] in letters_find_m:
                    long_words_m += word_real_moyen[j]
                else:
                    long_words_m += "-"

            if "-" not in long_words_m:
                print("Vous avez gagné! Le mot était", word_real_moyen)
                break
        else:
            print("Cette lettre n'est pas dans le mot.")
            trying -= 1
            print("Il vous reste", trying, "essai(s)")
            if trying == 0:
                print("Bah, vous avez perdu unh...., le mot était:", word_real_moyen)




letters_find_d = []
long_words_d = "-" * len(word_real_diff)

if choice == 'd' or choice == 'D':
    while trying > 0:
        print("Mot:",long_words_d)
        letter_choose = input("Entrez une lettre que vous pensez être dans le mot:")
        if letter_choose in word_real_diff:
            print("La lettre est dans le mot !")
            letters_find_d.append(letter_choose)

            long_words_d = ""
            for i in range(len(word_real_diff)):
                if word_real_diff[i] in letters_find_d:
                    long_words_d += word_real_diff[i]
                else:
                    long_words_d += "-"

            if "-" not in long_words_d:
                print("Vous avez gagné! Le mot était", word_real_diff)
                break
        else:
            print("Cette lettre n'est pas dans le mot.")
            trying -= 1
            print("Il vous reste", trying, "essai(s)")
            if trying == 0:
                print("Bah, vous avez perdu unh...., le mot était:", word_real_diff)






letters_find_a = []
long_words_a = "-" * len(word_real_anm)

if choice == 'A' or choice == 'a':
    print("Bien vous devez devinez le mot exact parmi le noms des personnages d'animés.\nMais attention, il y a des pieges.")
    while trying > 0:
        print("Nom:",long_words_a)
        letter_choose = input("Entrez une lettre que vous pensez être dans le nom: ")
        if letter_choose in word_real_anm:
            print("La lettre est dans le mot !")
            letters_find_a.append(letter_choose)

            long_words_a = ""
            for k in range(len(word_real_anm)):
                if word_real_anm[k] in letters_find_a:
                    long_words_a += word_real_anm[k]
                else:
                    long_words_a += "-"

            if "-" not in long_words_a:
                print("Vous avez gagné! Le mot était", word_real_anm)
                break
        else:
            print("Cette lettre n'est pas dans le mot.")
            trying -= 1
            print("Il vous reste", trying, "essai(s)")
            if trying == 0:
                print("Bah, vous avez perdu unh...., Quel honte pour le gang des Otaku!.Le vrai nom était:", word_real_anm)










