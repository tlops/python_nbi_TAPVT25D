#!/usr/bin/python3

# Övning 1
""" 
Skriv en funktion som tar en sträng som parameter och returnerar längden på en sträng. Anropa funktion och console.log svaret. Tips! Du kan skriva .length på en variabel som är en sträng för att få längden.
"""
print("\n # Övning 1: String List: \n")
def string_length():
    input_string = input("Enter a string and get the length of the string: ")
    print("Here is the length of the string: ", input_string, " - ", len(input_string))

string_length()

# Övning 2
"""
Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. Först ska funktionen tala om ifall listan är tom, eller hur många element den har. Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
"""
print("\n # Övning 2: Pretty List: ")
ugly_list = ["a", "b", 3.14]
def pretty_print(input_list):
    if len(input_list) != 0:
        print("The length of the List is: ", len(input_list))
        for i in range(len(input_list)):
            print(f"{i + 1}. {input_list[i]}")
    else:
        print("The list is empty. ")

#pretty_print(["a", "b", 3.14])
pretty_print(ugly_list)


# Övning 3
"""
Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet. cut_edges([1, 2, 3, 4]) → [2, 3]`
"""
print("\n # Övning 3: Cut Edges: \n")
edge_list = [1, 2, 3, 4]
def cut_edges(cut_list):
     if len(cut_list) != 0:
         del cut_list[-1]
         del cut_list[0]
         print("here is the new list with the edges cut away: ", cut_list)
     else:
        print("The list is empty.")

cut_edges(edge_list)


# Övning 4
"""
Skriv en funktion som tar tre parametrar. De första två är två tal och den sista är en operator d.v.s antingen '+', '-', '/', '*'. Utför beräkningen och returnera summan och skriv ut. Det ska enbart gå att skicka med siffror (förutom operanden som är en sträng då) och varje operation ska vara sin egen funktion.
"""
print("\n # Övning 4: Calculator: \n")
import numbers

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by 0."
    return num1 / num2


def calculator(num1, num2, operator):
    if not isinstance(num1, numbers.Number) or not isinstance(num1, numbers.Number): 
        if operator == '+':
            return add(num1, num2)
        elif operator == '-':
            return subtract(num1, num2)
        elif operator == '*':
            return multiply(num1, num2)
        elif operator == '/':
            return divide(num1, num2)
        else:
            return "Error: Invalid operator. Please use one of: +, -, *, /"


