# try:
#     number = int(input("Skriv in ett tal: "))
#     result = 10 / number
#     print(f"Resultat: {result}")
# except ValueError:
#     print("Enbart heltal tillåts")
# except ZeroDivisionError:
#     print("Du kan inte dela med noll")


# try:
#     number = int(input("Skriv in ett tal: "))
#     result = 10 / number
#     print(f"Resultat: {result}")
# except (ValueError, ZeroDivisionError):
#     print("Ett fel inträffande")
# else: # Hit går den om det inte blev ett fel
#     print("Utträkningen är klar")
# finally: # Denna körs oavsett om det gick bra eller blev fel
#     print("Nu avslutas programmet")

try:
    with open("data.txt") as file:
        file_content = file.read()
        print("Filen innehåller:\n")
        print(file_content)
except FileNotFoundError:
    print("Filen hittades inte")


def squarerot(number):
    if number < 0:
        raise ValueError("Inga negativa tal tillåts")

    return number ** 0.5


try:
    sum = squarerot(-9)
    print(f"Summan blev: {sum}")
except ValueError as error:
    print(error)