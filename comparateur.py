import CachedPokeService
import time

def comparateur():
    askFirstPokemon = True
    askSecondPokemon = True
    while(askFirstPokemon):
        pokemon1 = input("Renseignez le nom ou l'id du premier pokemon dont vous souhaitez comparer les statistiques : ")    
        try:
            response1 = CachedPokeService.getPokemonData(pokemon1)
            askFirstPokemon = False
        except:
            print("Entrée invalide")
    while(askSecondPokemon):
        pokemon2 = input("Renseignez le nom ou l'id du deuxième pokemon dont vous souhaitez comparer les statistiques : ")
        try:
            response2 = CachedPokeService.getPokemonData(pokemon2)
            askSecondPokemon = False
        except:
            print("Entrée invalide")
    
    stats1 = response1["stats"]
    stats2 = response2["stats"]
    index = 0
    print()
    for stat in stats1:
        time.sleep(0.5)
        stat_name = stat['stat']['name'].upper()
        base_stat1 = stat['base_stat']
        base_stat2 = stats2[index]['base_stat']
        if base_stat1 > base_stat2:
            print(f"{stat_name} : {response1['name']}({base_stat1}) est meilleur que {response2['name']}({base_stat2})")
        elif base_stat1 < base_stat2:
            print(f"{stat_name} : {response2['name']}({base_stat2}) est meilleur que {response1['name']}({base_stat1})")
        else:
            print(f"{stat_name} : {response1['name']} est aussi bon que {response2['name']} : {base_stat1}")
        index += 1
    print()
    
    print("\n--- Appuyez sur Entrée pour revenir au menu ---")
    input()