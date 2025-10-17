

- La [PokéAPI](https://pokeapi.co/) est une API RESTful gratuite qui fournit des info sur les Pokémon, leurs types, leurs évolutions, etc. Les endpoints que vous utiliserez le plus souvent sont :
    - `https://pokeapi.co/api/v2/pokemon/{id}` : Récupère les info sur un Pokémon par son ID ou son nom
    - `https://pokeapi.co/api/v2/type/{type}` : Récupère les infos sur un type de Pokémon


- Écrivez une fonction qui demande au user :
    - Le nom/id d'un Pokémon et affiche ses statistiques : *points de vie*, *attaque*, *défense*, etc. (Ne retourner pas tout simplement le grand `json`)
    - Le nom de deux Pokémon et compare leurs statistiques. Lequel est le plus fort (en points de vie et en attaque) ?
    - Le type des Pokémon (`fire`, `dragon`, etc.) et calcule le nombre des Pokémon de ce type `fire`, la moyenne des points de vie (HP)


- Répondre aux **Q1, 2, 3 communes** ?
- **Q1 commune** : Proposer une fonction qui permet gérer les erreurs courantes lors des requêtes vers l’API ? Celle-ci permettra des pauses (`time.sleep`), des mécanismes de `retry` (tentatives de nouvelles exécution), … ⇒ des calls plus robustes :
    - Par exemple : si le statut `429` (**Too Many Requests**) est retourné, `500/503` (Internal Server Error / Service Unavailable : erreur de serveur), éventuellement : `400` (**Bad Request**) , `401` (**Unauthorized** : token absent ou invalide) , `403` (**Forbidden**) , 404, identifiant non valide,… ?
- **Q2 commune** : Améliorer cette dernière fonction pour qu’elle puisse gérer des millions de requêtes de manière efficace et **simulez** à l’aide d’un script une charge très élevée de call vers plusieurs rootes : ["https://api.example.com/data1", "https://api.example.com/data2", "https://api.example.com/data3"] ? Indice : concurrence et parallélisme en Python, `asyncio`
- **Q3 commune** : Avancé - Améliorer encore cette dernière fonction en y spécifiant un `cache` avec un délai d’expiration d’1 heure ET **simulez/montrer** son bon fonctionnement ? Cela permet de :
    - Réduire les appels répétitifs à l'API (surtout si on doit retourner les mêmes data via l’AP) et donc d'alléger la charge sur le serveur.
    - Améliorer la rapidité de la réponse en se basant sur le cache et donc Améliorer les perf. de l’app. en prod.
- Simulez un combat entre deux Pokémon en utilisant leurs statistiques de base. Le Pokémon qui inflige le plus de dégâts totaux en cinq tours remporte le combat