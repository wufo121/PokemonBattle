from requests import get, status_codes, Session, exceptions
from concurrent.futures import ThreadPoolExecutor, as_completed

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

def _fetch_pokemon_data_worker(session, url):
    """
    Worker pour le ThreadPool.
    Récupère les données d'une URL en utilisant une session partagée.
    """
    try:
        response = session.get(url)
        response.raise_for_status() # Lève une exception pour 4xx/5xx
        return response.json()
    except exceptions.RequestException as e:
        print(f"Erreur de requête pour {url}: {e}")
        return None # Important: retourne None en cas d'échec

# --- FONCTION getListOfPokemonData (MODIFIÉE) ---
def getListOfPokemonData(linkList):
    """
    Récupère une liste de données Pokémon en parallèle en utilisant des threads.
    """
    data = []
    
    # Nombre de requêtes simultanées. 
    MAX_WORKERS = 20
    
    with Session() as session:
        # Crée le pool de threads
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            
            # 1. On soumet toutes les tâches (futures) au pool
            # On utilise un dictionnaire pour lier le 'future' à l'URL
            future_to_url = {
                executor.submit(_fetch_pokemon_data_worker, session, link): link 
                for link in linkList
            }
            
            # 2. On récupère les résultats dès qu'ils arrivent
            for future in as_completed(future_to_url):
                result = future.result()
                if result is not None: # On n'ajoute que les requêtes réussies
                    data.append(result)
    return data