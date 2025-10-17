from PokeService import getPokemonData

def combat():
    askFirstPokemon = True
    askSecondPokemon = True
    while(askFirstPokemon):
        firstPokemon = input("Renseignez le nom du premier pokemon : ")    
        try:
            responseFirstPokemon = getPokemonData(firstPokemon)
            askFirstPokemon = False
        except:
            print("Le pokemon renseigné n'existe pas, veuillez réessayer.")
    while(askSecondPokemon):
        secondPokemon = input("Renseignez le nom du second pokemon : ")    
        try:
            responseSecondPokemon = getPokemonData(secondPokemon)
            askSecondPokemon = False
        except:
            print("Le pokemon renseigné n'existe pas, veuillez réessayer.")

    print(f"Le combat entre {responseFirstPokemon['name']} et {responseSecondPokemon['name']} peut commencer !")
    
    atk1 = responseFirstPokemon['stats'][1]['base_stat']
    hp1 = responseFirstPokemon['stats'][0]['base_stat']
    atk2 = responseSecondPokemon['stats'][1]['base_stat']
    hp2 = responseSecondPokemon['stats'][0]['base_stat']

    for i in range (1, 6):
        damage1 = max(atk1 - def2, 1)
        hp2 -= damage1
        print(f"{responseFirstPokemon} attaque {responseSecondPokemon} et inflige {damage1} dégâts.")
        if hp2 <= 0:
            print(f"{responseSecondPokemon} est K.O. ❌")
            print(f"🏆 {responseFirstPokemon} remporte le combat !")
            break
        else:
            print(f"Il reste {hp2} HP à {responseSecondPokemon}.")

        # 🥊 Attaque du second Pokémon
        damage2 = max(atk2 - def1, 1)
        hp1 -= damage2
        print(f"{responseSecondPokemon} attaque {responseFirstPokemon} et inflige {damage2} dégâts.")
        if hp1 <= 0:
            print(f"{responseFirstPokemon} est K.O. ❌")
            print(f"🏆 {responseSecondPokemon} remporte le combat !")
            break
        else:
            print(f"Il reste {hp1} HP à {responseFirstPokemon}.\n")

    # Si aucun KO après 5 tours
    if hp1 > 0 and hp2 > 0:
        print("\n⏱️ Le combat est terminé après 5 tours.")
        if hp1 > hp2:
            print(f"🏆 {responseFirstPokemon} a plus de HP restants et gagne !")
        elif hp2 > hp1:
            print(f"🏆 {responseSecondPokemon} a plus de HP restants et gagne !")
        else:
            print("🤝 Match nul !")