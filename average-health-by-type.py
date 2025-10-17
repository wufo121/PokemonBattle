import PokeService


def get_type_pokemon():
    pokemon = input("Renseignez le nom du type dont vous souhaitez affichez les statistique")
    PokeService.getPokemonTypeService(pokemon)

    if response.status_code != 200:
        print('Erreur')
        return None
    
    data = response.json()
    pokemons = data['pokemon']
    count = len(pokemons)

    total_hp = 0
    for mon in pokemons:
        stats = get_pokemon_stats(mon['pokemon']['name'])
        if stats:
            total_hp += stats.get('hp', 0)

avg_hp = total_hp / count if count > 0 else 0

print(f"Type '{pokemon_type}': {count} Pokémon(s), moyenne HP = {avg_hp:.2f}")