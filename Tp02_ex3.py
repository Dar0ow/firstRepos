"""
    Programme permettant de savoir si un trajet ou une série de trajet sont réalisable par rapport
    au réservoir d'essence d'une voiture. Pour ce faire il faut spécifier une distance en kilometres
    et un nombre de passagers à bord(sans compte le conducteur).
    Indications:
        - Le véhicule a les caractéristiques suivantes :
            - Une consommation fixe de 5.0 litre pour 100km
            - Pour chaque personne ajoutée (le conducteur ne compte pas), l'essence utilisée augmente de 30%
              en rapport à la consommation normale
                - Exemple : pour 1 personne en plus du conducteur, la consommation vaut 1.3 fois la consommation normale
                            pour 2 personnes en plus du conducteur, la consommation vaut 1.6 fois la consommation normale
        - Lors de la saisie de la distance, si l'utilisateur met 0, le programme rempli le réservoir d'essence
          du véhicule
        - Lorsque qu'un voyage est réalisable, un message affiche le nombre de litres restants
        - Le programme se termine uniquement si une panne d'essence se produit. Si cela arrive,
          Un message affiche que la panne arrivera lors de ce trajet. Un second message affichera
          la distance parcourue avec tous les trajets.
"""
# Déclaration et initialisation des variables
ESSENCE_INITIAL : float = 32.5
CONSOMATION_NORMALE : int = 5
consomation_trajet: float = 0
nb_passagers : int = 0
essence : float = 0
distance : float = 0
distance_globale : float = 0
# Séquence d'opération
essence = ESSENCE_INITIAL

while essence > 0:
    while distance == 0:
        distance = float(input("Veuillez inserer la distance à parcourir, si vous saisissez 0 le reservoir est remplie :"))
        if distance == 0:
            essence = 32.5
    nb_passagers = int(input("Veuillez insérer le nombres de passagers dans le véhicule: "))

    if nb_passagers != 0:
        consomation_trajet = consomation_trajet + CONSOMATION_NORMALE / 100 * (30 * nb_passagers)
    essence = essence - distance * (consomation_trajet / 100)

    distance_globale = distance_globale + distance
    if essence > 0:
        print("Le voyage est réalisable. Il vous reste {:.2f} litres d'essence dans votre réservoir.".format(essence))
    distance = 0

print("La panne vas arriver lors de ce trajet!")
print("Vous avez parcouru {:.2f} kilomètres au total".format(distance_globale))