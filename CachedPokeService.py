from cachetools import TTLCache
import PokeService

type_cache = TTLCache(maxsize=100, ttl=3600)
pokemon_data_cache = TTLCache(maxsize=1000, ttl=3600)
pokemon_name_cache = TTLCache(maxsize=1000, ttl=3600)

def getPokemonTypeService(type_name):
    type_name = type_name.lower()
    if type_name in type_cache:
        print("[CACHE] Type récupéré depuis le cache.")
        return type_cache[type_name]

    print("[API CALL] Type récupéré depuis l'API.")
    data = PokeService.getPokemonTypeService(type_name)
    type_cache[type_name] = data
    return data

def getListOfPokemonData(link_list):
    pokemons = []

    for link in link_list:
        if link in pokemon_data_cache:
            print(f"[CACHE] Pokémon depuis cache : {link}")
            pokemons.append(pokemon_data_cache[link])
        else:
            data = PokeService.fetchData(link)
            pokemon_data_cache[link] = data
            pokemons.append(data)

    return pokemons

def getPokemonData(pokemon_identifier):
    cache_key = str(pokemon_identifier).lower()
    
    if cache_key in pokemon_name_cache:
        print(f"[CACHE] Pokémon '{pokemon_identifier}' récupéré depuis le cache.")
        return pokemon_name_cache[cache_key]
    
    print(f"[API CALL] Pokémon '{pokemon_identifier}' récupéré depuis l'API.")
    data = PokeService.getPokemonData(pokemon_identifier)
    pokemon_name_cache[cache_key] = data
    return data