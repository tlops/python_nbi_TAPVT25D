# Lägg till ny kontakt
# 1. Ta emot input från användaren
# 2. Spara namn i en lista
# 3. När programmet avslutas så sparar vi listan i en fil


def read_file(name):
    print("Läser kontakter från fil")
    try:
        with open(name) as file:
            return list(map(lambda row: row.strip(), file))
    except:
        print("Ingen fil hittades - startar med en tom lista")
        return []

def save_file(name, contacts):
    print("Sparar kontakter till fil")
    try:
        with open(name, "w") as file:
            for contact in contacts:
                file.write(f"{contact}\n")
    except OSError:
        print("Kunde inte spara filen")
    else:
        print("Fil sparad!")

def display_menu():
    print("\n--- Kontaktlista ---")
    print("1. Visa kontakter")
    print("2. Lägg till kontakt")
    print("3. Ta bort kontakt")
    print("4. Avsluta")

def main():
    file_name = "contacts.txt"
    contacts = read_file(file_name)

    while True:
        display_menu()
        try:
            choose = int(input("Välj ett alternativ (1-4): "))
        except ValueError:
            print("Du kan enbart välja siffra 1-4")
            continue # Hoppa tillbaka till menyn
        if choose == 1:
            print("Kontakter:\n")
            for contact in contacts:
                print(f"- {contact}")
        elif choose == 2:
            name = input("Ange namn:")
            contacts.append(name)
            print(f"{name} har lagts till")
        elif choose == 3:
            try:
                index = int(input("Vilken kontakt vill du ta bort(nummer)?: "))
                removed_contact = contacts.pop(index)
                print(f"{removed_contact} har tagits bort")
            except ValueError:
                print("Ogiltlig nummer")
            except IndexError:
                print("Kontakten finns inte")
        elif choose == 4:
            save_file(file_name, contacts)
            break # Avsluta program
        else:
            print("Välj siffra 1-4")

if __name__ == "__main__": # Kör main() enbart om filen körs direkt inte om den importeras
    main()