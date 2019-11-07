"""
Considérons les opérations suivantes applicables à un nombre entier (positif) :
    — si ce nombre est divisible par 3, on lui ajoute 4 ;
    — s’il n’est pas divisible par 3 mais divisible par 4, on le divise par 2;
    — s’il n’est divisible ni par 3, ni par 4, on lui soustrait 1.
On répète ces opérations successivement jusqu’à arriver à 0.

Ecrivez un programme affichant le nombre d'opérations pour arriver à 0 pour
chaque chiffre entier compris entre deux valeurs demandées à l'utilisateur.

"""
# Déclaration et initialisation des variables
chiffre_demandé_1: int = None
chiffre_demandé_2: int = None
chiffre_compris: int = None

# Séquence d'opération

chiffre_demandé_1 = int(input("Veuillez saisir le plus petit chiffre: "))
chiffre_demandé_2 = int(input("Veuillez saisir le plus grand chiffre: "))

nb: int = chiffre_demandé_1


while nb <= chiffre_demandé_2:
    i = nb
    nb_operations: int = 0
    while i > 0:
        if i % 3 == 0:
            i = i + 4
        elif i % 4 == 0:
            i = i // 2
        else:
            i = i - 1
        nb_operations = nb_operations + 1
    else:
        print("{} -> {}".format(nb,nb_operations))
    nb = nb + 1