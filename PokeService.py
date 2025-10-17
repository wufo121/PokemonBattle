from requests import get, status_codes

# The API endpoint
BASE_API_URL = 'https://pokeapi.co/api/v2/'

def fetchData(route, retry = 0):
    # A GET request to the API
    try :
        for i in range(retry+1):
            response = get(route)
            # Si le code d'erreur commence par 200
            if int(response.status_code / 100) == 2:
                return response.json()
        # Si le code d'erreur commence par 300, 400 ou 500    
        if (response.status_code / 100) > 2 :
            raise Exception(f"{response.status_code} {status_codes._codes[response.status_code][0]}")
    except Exception as e:
        raise(e)

def getPokemonData(id):
    route = f'pokemon/{id}'
    data = fetchData(BASE_API_URL + route)
    return data

def getPokemonTypeService(type):
    route = f'type/{type}'
    data = fetchData(BASE_API_URL + route)
    return data['pokemon']

def getListOfPokemonData(linkList):
    data = []
    for link in linkList:
        data.append(fetchData(link))
    return data