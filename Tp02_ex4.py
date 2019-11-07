
"""
    Programme simulant un jeu de BlackJack avec des lancés de dés. L'objectif du jeu est d'arriver au plus proche de
    21 sans dépasser 21. Pour se faire l'utilisateur peut lancer un nombre de dés de son choix. Le programme simule un
    lancer de dés (en générant aléatoirement des valeurs entre 1 et 6) et obtiens une somme. L'utilisateur peut décider
    de continuer de lancer des dés supplémentaires ou de s'arrêter (entrer 0 lorsque l'on demande le nombre de dés).
    L'ordinateur joue également en parallèle avec sa propre somme et son score est affiché également. Le jeu se termine lorsque le
    joueur ET l'ordinateur ont terminé de jouer.

    Indications:
        - Si le joueur entre 0 comme nombre de dés à lancer, cela signifie qu'il arrête de lancer plus de dés et sa partie se termine
        - Voici le détail sur la stratégie de jeu de l'ordinateur:
            - Si la somme de l'ordinateur est inférieure à 6, il demande 3 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 6 et inférieure à 12, il demande 2 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 12 et inférieure à 18, il demande 1 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 18, il s'arrête de jouer

"""
import random
# Déclaration et Initialisation des variables
de_uti: int = None
de_ordi: int = None
somme_de_uti: int = 0
somme_de_ordi: int = 0
BLACK_JACK: int = 21
boucle_uti: int = 0
boucle_ordi: int = 0

# Séquence d'opérations

while de_uti != 0 or de_ordi != 0:
    de_uti = int(input("Combien de dés voulez-vous utiliser?: "))
    if somme_de_ordi < 6:
        de_ordi = 3
    elif somme_de_ordi >= 6 and somme_de_ordi < 12:
        de_ordi = 2
    elif somme_de_ordi >= 12 and somme_de_ordi < 18:
        de_ordi = 1
    else:
        de_ordi = 0

    while boucle_uti < de_uti:
        somme_de_uti += random.randint(1, 6)
        boucle_uti += 1


    print("Vous avez un score de {}".format(somme_de_uti))

    while boucle_ordi < de_ordi:
        somme_de_ordi += random.randint(1, 6)
        boucle_ordi += 1

    print("""L'ordinateur à choisi {} dés.
    Son score est de {}""".format(de_ordi, somme_de_ordi))
    boucle_uti = 0
    boucle_ordi = 0

if somme_de_ordi == somme_de_uti:
    print("Vous êtes à égalité!")
if somme_de_uti > 21 or somme_de_uti < somme_de_ordi:
    print("Vous avez perdu {} à {} contre l'ordi !".format(somme_de_uti, somme_de_ordi))
if somme_de_ordi < somme_de_uti < 21 or somme_de_uti <= 21 and somme_de_ordi > 21:
    print("Vous avez gagné {} à {} contre l'ordi!".format(somme_de_uti, somme_de_ordi))