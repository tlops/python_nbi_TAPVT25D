#!/usr/bin/python3


# i. Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan med funktionen print.
list_films = ["Pirate of the Caribean", "The God Father", "Sound of Music", "Dead Poets Society"]
for film in list_films:
    print(film)
# ii. Lägg till "Fellowship of the ring" sist i listan.
list_films.append("Fellowship of the ring")
print(list_films)

# iii. Lägg till "The two towers" på första platsen i listan. (index noll)
list_films[0] = "The two towers" 
print(list_films)

## iv. Ta reda på vilken position (index) "Fellowship of the ring" har nu.
index = list_films.index("Fellowship of the ring")
print("The index of 'Fellowship of the ring' is: ", index)

# v. Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
del list_films[1]
index = list_films.index("Fellowship of the ring")
print("The new index of 'Fellowship of the ring' is: ", index)

# vi. Ta reda på hur lång listan är. (len)
length = len(list_films)
print("The lenght of the list is: ", length)

# vii. Vänd listan baklänges.
print("Here is the new list of Films: ", list_films)
list_films.reverse()
print("Here is the reversed list of Films: ", list_films)

# vii. Sortera listan stigande i bokstavsordning.
list_films.sort()
print("Here is the list of filmed in ascending order: ", list_films)
