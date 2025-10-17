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
    
    stat1 = responseFirstPokemon['stats']
    name1 = responseFirstPokemon['name']
    atk1 = stat1[1]['base_stat']
    hp1 = stat1[0]['base_stat']
    def1 = stat1[2]['base_stat']

    stat2 = responseSecondPokemon['stats']
    name2 = responseSecondPokemon['name']
    atk2 = stat2[1]['base_stat']
    hp2 = stat2[0]['base_stat']
    def2 = stat2[2]['base_stat']

    print(f"\nStatistiques de {name1} : ATK = {atk1}, DEF = {def1}, HP = {hp1}")
    print(f"Statistiques de {name2} : ATK = {atk2}, DEF = {def2}, HP = {hp2}\n")

    for i in range (1, 6):

        damage1 = max(atk1 - def2, 1)
        hp2 -= damage1
        print(f"{name1} attaque {name2} et inflige {damage1} dégâts.")
        if hp2 <= 0:
            print(f"{name2} est K.O.")
            print(f"🏆 {name1} remporte le combat !")
            break
        else:
            print(f"Il reste {hp2} HP à {name2}.")

        damage2 = max(atk2 - def1, 1)
        hp1 -= damage2
        print(f"{name2} attaque {name1} et inflige {damage2} dégâts.")
        if hp1 <= 0:
            print(f"{name1} est K.O.")
            print(f"🏆 {name2} remporte le combat !")
            break
        else:
            print(f"Il reste {hp1} HP à {name1}.\n")

    if hp1 > 0 and hp2 > 0:
        print("\n⏱️ Le combat est terminé après 5 tours.")
        if hp1 > hp2:
            print(f"{name1} a plus de HP restants et gagne !")
        elif hp2 > hp1:
            print(f"{name2} a plus de HP restants et gagne !")
        else:
            print("Match nul !")