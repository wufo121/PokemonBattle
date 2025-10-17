from PokeService import getPokemonData


def showStats(stats):
    print("║ \n║ STATISTIQUES DU POKÉMON")
    
    for stat in stats:
        stat_name = stat['stat']['name'].upper()
        base_stat = stat['base_stat']
        
        print(f"║ {stat_name:<21} {base_stat:<3}")
    
    print("╚════════════════════════════════════╝")
def ask_who_pokemon_user_want_see():
    while(True):
        pokemon = input("Renseignez le nom du pokemon ou l'id du pokemon dont vous souhaitez affichez les statistique : ")    
        try:
            response = getPokemonData(pokemon)
            print("╔════════════════════════════════════╗")
            print(f"║ ID\t\t\t{response["id"]}")
            print(f"║ NAME\t\t\t{response["name"]}")
            print(f"║ HEIGHT\t\t{response["height"]*10} cm")
            print(f"║ WEIGHT\t\t{response["weight"]/10} kg")
            showStats(response['stats'])
            return
        except:
            print("Entrée invalide")
