import CachedPokeService


def get_type_pokemon():
    askType = True
    while(askType):
        typeInput = input("Renseignez le nom du type dont vous souhaitez affichez les statistique : ")

        if typeInput.lower() == 'menu':
            return
        try:
            response = CachedPokeService.getPokemonTypeService(typeInput)
            askType = False
        except:
            print("Entrée incorrecte, veuillez entrer un type en anglais.")

    linkList = [pokemonLink['pokemon']['url'] for pokemonLink in response]
    count = len(linkList)

    pokemons = CachedPokeService.getListOfPokemonData(linkList)

    total_hp = 0
    for pokemon in pokemons:
        hp = pokemon['stats'][0]['base_stat']
        if hp:
            total_hp += hp

    avg_hp = total_hp / count if count > 0 else 0

    print(f"Type '{typeInput}': {count} Pokémon(s), moyenne HP = {avg_hp:.2f}")
    print("\n--- Cache chargé ! Essayez le même type pour voir la différence ---\n")