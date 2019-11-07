"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration des variables
montant_1: float
montant_2: float
choix_article: int
SANDWICH_AU_POULET: float
CHIPS_PAPRIKA: float
BARRE_CHOCOLATEE: float
BONBONS: float
ICE_TEA: float
LIMONADE: float
donnee_uti: str
###Initialisation des variables
SANDWICH_AU_POULET = 4.90
CHIPS_PAPRIKA = 2.50
BARRE_CHOCOLATEE = 2.00
BONBONS = 3.30
ICE_TEA = 2.20
LIMONADE = 1.90
montant_1 = 0
montant_2 = 0
donnee_uti = None

### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet ",SANDWICH_AU_POULET,".-")
print("2. Chips Paprika",CHIPS_PAPRIKA,".-")
print("3. Barre chocolatée",BARRE_CHOCOLATEE,".-")
print("4. Bonbons",BONBONS,".-")
print("5. Ice Tea",ICE_TEA,".-")
print("6. Limonade",LIMONADE,".-")

montant_1 = float(input("Veuillez insérer votre monnaie: "))
donnee_uti = str(input("Veuillez choisir un artcile: "))

choix_article = int(donnee_uti.split(" ")[0])

print(choix_article)
while not 0 < choix_article < 7:
    choix_article = int(input("Cette article n'existe pas! Veuillez entrer un numéro de produit valable:  "))



if choix_article == 1:
    while montant_1 < SANDWICH_AU_POULET:
        print("Montant insuffisant, il manque " + str(SANDWICH_AU_POULET - montant_1) + ".")
        montant_2 = float(input("Veuillez insérer la monnaie manquante: "))
        montant_1 += montant_2
    else:
        print("Transaction acceptée")
        print("Retour de la monnaie:", montant_1 - SANDWICH_AU_POULET)
        print("Sandwich au poulet, bon appétit!")
if choix_article == 2:
    while montant_1 < CHIPS_PAPRIKA:
        print("Montant insuffisant, il manque " + str(CHIPS_PAPRIKA - montant_1) + ".")
        montant_2 = float(input("Veuillez insérer la monnaie manquante: "))
        montant_1 += montant_2
    else:
        print("Transaction acceptée")
        print("Retour de la monnaie:", montant_1 - CHIPS_PAPRIKA)
        print("Sandwich au poulet, bon appétit!")
if choix_article == 3:
    while montant_1 < BARRE_CHOCOLATEE:
        print("Montant insuffisant, il manque " + str(BARRE_CHOCOLATEE - montant_1) + ".")
        montant_2 = float(input("Veuillez insérer la monnaie manquante: "))
        montant_1 += montant_2
    else:
        print("Transaction acceptée")
        print("Retour de la monnaie:", montant_1 - BARRE_CHOCOLATEE)
        print("Sandwich au poulet, bon appétit!")
if choix_article == 4:
    while montant_1 < BONBONS:
        print("Montant insuffisant, il manque " + str(BONBONS - montant_1) + ".")
        montant_2 = float(input("Veuillez insérer la monnaie manquante: "))
        montant_1 += montant_2
    else:
        print("Transaction acceptée")
        print("Retour de la monnaie:", montant_1 - BONBONS)
        print("Sandwich au poulet, bon appétit!")
if choix_article == 5:
    while montant_1 < ICE_TEA:
        print("Montant insuffisant, il manque " + str(ICE_TEA - montant_1) + ".")
        montant_2 = float(input("Veuillez insérer la monnaie manquante: "))
        montant_1 += montant_2
    else:
        print("Transaction acceptée")
        print("Retour de la monnaie:", montant_1 - ICE_TEA)
        print("Sandwich au poulet, bon appétit!")
if choix_article == 6:
    while montant_1 < LIMONADE:
        print("Montant insuffisant, il manque " + str(LIMONADE - montant_1) + ".")
        montant_2 = float(input("Veuillez insérer la monnaie manquante: "))
        montant_1 += montant_2
    else:
        print("Transaction acceptée")
        print("Retour de la monnaie:", montant_1 - LIMONADE)
        print("Sandwich au poulet, bon appétit!")