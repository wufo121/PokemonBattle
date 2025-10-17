from PokeService import getPokemonTypeService, getPokemonData
from pokedex import showStats

def get_type_pokemon():
    type_name = input("Renseignez le nom du type dont vous souhaitez affichez les statistique : \n ")
    valid_types = ["normal", "fire", "water", "electric", "grass", "ice", "fight", "poison", "ground",
                   "wind", "psychic", "bug", "ghost", "dragon", "dark", "steel", "fairy"]
    if type_name not in valid_types:
        print("Type invalide. Veuillez entrer un type valide.")
        return
    
    pokemons = getPokemonTypeService(type_name)
    total_hp = 0
    count = 0
    
    for entry in pokemons:
        try:
            pokemon_name = entry['pokemon']['name']
            data = getPokemonData(pokemon_name)
            
            hp = next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == 'hp')
            
            total_hp += hp
            count += 1
        except Exception as e:
            print(f"❌ Erreur lors du traitement de {pokemon_name}: {e}")

    if count > 0:
        average_hp = total_hp / count
        print(f"\n📊 Moyenne des HP des {count} pokémons de type {type_name} : {average_hp:.2f}")
    else:
        print("Aucun Pokémon n’a pu être chargé.")

