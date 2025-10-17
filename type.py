import PokeService


def get_type_pokemon():
    askType = True
    while(askType):
        typeInput = input("Renseignez le nom du type dont vous souhaitez affichez les statistique : ")
        try:
            response = PokeService.getPokemonTypeService(typeInput)
            askType = False
        except:
            print("Entrée incorecte, veillez entrer un type en anglais")

    linkList = []
    for pokemonLink in response:
        linkList.append(pokemonLink['pokemon']['url'])
    count = len(linkList)

    pokemons = PokeService.getListOfPokemonData(linkList)

    total_hp = 0
    for pokemon in pokemons:
        hp = pokemon['stats'][0]['base_stat']
        if hp:
            total_hp += hp

    avg_hp = total_hp / count if count > 0 else 0

    print(f"Type '{typeInput}': {count} Pokémon(s), moyenne HP = {avg_hp:.2f}")