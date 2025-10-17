from pokedex import ask_who_pokemon_user_want_see
from type import get_type_pokemon
from comparateur import comparateur
from combat import combat


def intro():
    print("Bonjour, vous êtes la pour voir des Pokemon se foutre sur la gueule pendant que tu cries des attaques qui peuvent raser des maisons ou des villes, tout ça alors que tu as à peine 10 ans et 1000 pokedollars en poche (on se demande tous comment une mère célibataire au chomâge peut se le permettre d'ailleurs.?.. Enfin bref.).")

def userChoice():
    print("""
     MENU PRINCIPAL POKÉMON
    
    Que souhaitez-vous faire ?
    
    1.  Afficher les statistiques d'un Pokémon
    2.   Comparer les statistiques de deux Pokémon
    3.  Calculer la moyenne des points de vie d'un type
    4.   Simuler un combat Pokémon entre 2 Pokémon
    5.  Quitter
    """)
    
    while True:
        choice = input("👉 Votre choix (1-5) : ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
        else:
            print("❌ Veuillez choisir un nombre entre 1 et 5")

def executeChoice(choice):
    if choice == 1:
        ask_who_pokemon_user_want_see()
    if choice == 2:
        comparateur()
    if choice == 3:
        print("moyenne de point de vie par type")
        get_type_pokemon()
    if choice == 4:
        print("combat")
        combat()
    if choice == 5:
        print("Merci ! Au Revoir !")
        # a remplacer



def main():
    intro()
    choice = userChoice()
    executeChoice(choice)


if __name__ == "__main__":
    main()