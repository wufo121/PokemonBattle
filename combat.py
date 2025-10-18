import CachedPokeService

def combat():
    askFirstPokemon = True
    askSecondPokemon = True
    while(askFirstPokemon):
        firstPokemon = input("Renseignez le nom du premier pokemon : ")    
        try:
            responseFirstPokemon = CachedPokeService.getPokemonData(firstPokemon)
            askFirstPokemon = False
        except:
            print("Le pokemon renseigné n'existe pas, veuillez réessayer.")
    while(askSecondPokemon):
        secondPokemon = input("Renseignez le nom du second pokemon : ")    
        try:
            responseSecondPokemon = CachedPokeService.getPokemonData(secondPokemon)
            askSecondPokemon = False
        except:
            print("Le pokemon renseigné n'existe pas, veuillez réessayer.")

    print(f"Le combat entre {responseFirstPokemon['name']} et {responseSecondPokemon['name']} peut commencer !")
    
    atk1 = responseFirstPokemon['stats'][1]['base_stat']
    hp1 = responseFirstPokemon['stats'][0]['base_stat']
    def1 = responseFirstPokemon['stats'][2]['base_stat']
    atk2 = responseSecondPokemon['stats'][1]['base_stat']
    hp2 = responseSecondPokemon['stats'][0]['base_stat']
    def2 = responseSecondPokemon['stats'][2]['base_stat']

    for i in range(1, 6):
        damage1 = max(atk1 - def2, 1)
        hp2 -= damage1
        print(f"{responseFirstPokemon['name']} attaque {responseSecondPokemon['name']} et inflige {damage1} dégâts.")
        if hp2 <= 0:
            print(f"{responseSecondPokemon['name']} est K.O. ❌")
            print(f"🏆 {responseFirstPokemon['name']} remporte le combat !")
            break
        else:
            print(f"Il reste {hp2} HP à {responseSecondPokemon['name']}.")

        damage2 = max(atk2 - def1, 1)
        hp1 -= damage2
        print(f"{responseSecondPokemon['name']} attaque {responseFirstPokemon['name']} et inflige {damage2} dégâts.")
        if hp1 <= 0:
            print(f"{responseFirstPokemon['name']} est K.O. ❌")
            print(f"🏆 {responseSecondPokemon['name']} remporte le combat !")
            break
        else:
            print(f"Il reste {hp1} HP à {responseFirstPokemon['name']}.\n")

    # Si aucun KO après 5 tours
    if hp1 > 0 and hp2 > 0:
        print("\n⏱️ Le combat est terminé après 5 tours.")
        if hp1 > hp2:
            print(f"🏆 {responseFirstPokemon['name']} a plus de HP restants et gagne !")
        elif hp2 > hp1:
            print(f"🏆 {responseSecondPokemon['name']} a plus de HP restants et gagne !")
        else:
            print("🤝 Match nul !")
    
    print("\n--- Appuyez sur Entrée pour revenir au menu ---")
    input()