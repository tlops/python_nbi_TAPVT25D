#!/usr/bin/python3

index = 10

pokemons = ["Pikachu", "Charmander", "Bulbasaur"] # en lista, datatyp array

print(pokemons) # Skriv ut lista
print("Längd:", len(pokemons)) # Längd på lista

pokemons.append("Squirtle") # Lägger till ett värde i en lista
print(pokemons)
print(pokemons[1]) # Skriver ut värdet på position 1 i listan (man startar på 0)

pokemons.remove("Squirtle") # Tar bort värdet "Squirtle"
print(pokemons)

for i in range(len(pokemons)): # Loopar igenom listan
    print("Pokemon:", pokemons[i])

for pokemon in pokemons:
    print(pokemon)

while index > 0:
    print("Index: ", index)
    index = index - 1
    print("Inuti while-loop")

print("While-loop klar")

for i in range(5): # Kollar varje gång om i < 5
    print("I: ", i)
    print("Inuti for-loop")

print("For-loop klar")

for i in range(100, 0, -10): # Kollar varje gång i > 0
    print(i)
