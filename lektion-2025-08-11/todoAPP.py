#!/usr/bin/python3


todos = []
answer = ""

while answer != "klar":
    answer = input("""Vad är din todo? 
    Skriv 'visa' för att visa alla todos. 
    Skriv 'klar' för att avsluta.
    Skriv 'ta bort' siffran på den todo som jag vill ta bort.
    Skriv 'redigera' for att byta någon av de todos som har lagt till redan.\n""")

    if answer != "klar" and answer != "visa" and answer != "ta bort" and answer != "redigera":
        todos.append(answer)
        print("Todo tillagd")
    elif answer == "visa":
        print("-----Todos-----")
        for i in range(len(todos)):
            print(f"{i + 1}. {todos[i]}")

    elif answer == "ta bort":
        if not todos:
            print("There is nothing in todo list")
        else:
            to_delete = input("Enter the serial number of the item you want to delete: ")
            delete_index = int(to_delete) - 1
            print("You have selected to delete this item: \n", todos[delete_index])
            del todos[delete_index]

    elif answer == "redigera":
        if not todos:
            print("There is nothing in todo list")
        else: 
            to_edit = int(input("Enter the serial number of the item you want to edit: "))
            if to_edit <= len(todos):
                new_todo = input("Enter the new todo: ")
                old_todo_index = to_edit - 1
                old_todo = todos[old_todo_index]
                todos[old_todo_index] = new_todo
                print(f"'{old_todo}' has been updated to '{new_todo}'.")
            else:
                print("invalid Number")


