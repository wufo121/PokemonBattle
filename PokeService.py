from requests import get, status_codes
import time

BASE_API_URL = 'https://pokeapi.co/api/v2/'
RETRY_CODES = [429, 500, 503]



def handleError(code):
    if code in RETRY_CODES:
        return None 
    else:
        raise Exception(f"{code} {status_codes._codes[code][0]}")

def fetchData(route, retries=3, delay=2):

    for attempt in range(1, retries + 1):
        response = get(route)
        code = response.status_code

        if 200 <= code < 300:
            return response.json()  

        try:
            result = handleError(code)
            if result is None:
                print(f"⚠️ {code} - retry {attempt}/{retries}...")
                time.sleep(delay * attempt)
        except Exception as e:
            if attempt == retries:
                raise
            else:
                print(f"⚠️ Attempt {attempt}/{retries} failed: {e}")
                time.sleep(delay * attempt)

    raise Exception("❌ Failed after multiple attempts")

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


try:
    print(fetchData("pokemon", 5))
except Exception as e:
    print(e)