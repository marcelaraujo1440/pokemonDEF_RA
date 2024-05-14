import random
import time
pokemonsIniciais = ["Bulbasaur", "Squirtle", "Charmander"]
pokemons_caverna = ['Onix', 'Zubat', 'Diglet', 'Geodude', 'Grimer', 'Gastly', 'Hypno', 'Voltorb', 'Cubone']
pokemons_mato = ['Pidgey', 'Caterpie', 'Bellsprout', 'Abra', 'Weedle', 'Ekans', 'Pikachu', 'Spearow']
rep_floresta = []
rep_caverna = []
pokedex = []
tentativas = 3

def introducao():
    print("Professor Carvalho aparece")
    nomeJogador = input("Professor Carvalho: Olá treinador, bem-vindo ao mundo Pokémon. Eu sou o Professor Carvalho, como posso te chamar?\nDigite aqui seu nome: ")
 
    print(f"Professor Carvalho: É um prazer te conhecer, {nomeJogador}. Esta é a cidade de Pallet, na região de Kanto!\n")
    time.sleep(0.5)
    pokemon_inicial()
def pokemon_inicial():
    inicial=int(input("----Escolha um pokemon inicial----\n1-Charmander\n2-Squirtle\n3-Bulbassaur\n>>> "))
    if inicial == 1:
        pokedex.append('Charmander')
    elif inicial ==2:
        pokedex.append('Squirtle')
    elif inicial ==3:
        pokedex.append('Bulbassaur')
    elif inicial != 1 or inicial != 2 or inicial != 3:
        print("Digite uma opção válida...")
    print(f"Um {pokedex[0]}! Otima escolha!")
    return inicial


def escolha_pokemon():
    while True:
        escolha = int(input(f'\nO que deseja fazer?\n(1) Ir para a Floresta\n(2) Ir para a Caverna\n(3) Pokedex\n(4) Sair \n>>> '))
        
        if escolha == 1:
            bioma(pokemons_mato, rep_floresta)
        elif escolha == 2:
            bioma(pokemons_caverna, rep_caverna)
        elif escolha == 3 :
            abrir_pokedex()
        elif escolha == 4:
            print("Até logo")
            break
        else:
            print("Digite uma opção válida...")

def bioma(lista_pokemon, rep_lista):
    pok = random.choice(lista_pokemon)
    if pok in rep_lista:
        print(f'\nVocê encontrou um {pok}, mas você já possui este Pokémon!')
        return
    print(f"Você encontrou 3 pokebolas")
    time.sleep(1)
    print(f'\n*{pok} apareceu*\n')

    capt_pokemon(pok, lista_pokemon, rep_lista)

def capt_pokemon(pokemon, lista_pokemon, rep_lista):
    tentativas_local = tentativas
    while True:
        captura = input(f'Você deseja capturar este Pokémon? (s/n)\n>>>').lower()
        if captura == 'n':
            print(f'\nOk, você escolheu não capturar {pokemon}.')
            break

        if captura == 's':
            for _ in range(tentativas_local):
                num1 = random.randint(0, 1)
                num2 = random.randint(0, 1)
                if num1 == num2:
                    print("Você capturou esse Pokémon!")
                    pokedex.append(pokemon)
                    rep_lista.append(pokemon)
                    return captura
                elif num1 != num2:
                    
                    tentar_novamente(pokemon, lista_pokemon, rep_lista)
                    return captura
                
                
def tentar_novamente(pokemon, Lista_pokemon,rep_lista):
    tentativas_local = tentativas
    while tentativas_local > 0:
        novamente = input("\nvocê nao conseguiu capturar esse pokemon, deseja tentar novamente? (s/n)\n>>>")
                 
        if novamente == 's':
            num1 = random.randint(0,3)
            num2 = random.randint(0,3)   

            if num1 == num2:
                    print("Você capturou esse pokémon!")
                    pokedex.append(pokemon)
                    rep_lista.append(pokemon)
                    return novamente
            else:
                print("O pokémon fugiu!")
                tentativas_local -= 1
        
               
        if novamente == 'n':
                return novamente
        else:
                print("Tente com uma opção válida!")   
        print("Você não conseguiu capturar o Pokémon, e acabaram suas pokebolas!")
        return novamente
               
def abrir_pokedex():
    if len(pokedex) < 1:
        print("Você ainda não capturou nenhum Pokémon!")
    else:
        time.sleep(0.5)
        print(f"Aqui são todos os Pokémon que você já capturou: {pokedex}") 

introducao()
escolha_pokemon()
