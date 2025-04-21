# Write your solution here
def search(my_phonebook):
    name = input("name:")
    if name in my_phonebook:
        print(my_phonebook[name])
    if name not in my_phonebook:
        print("no number")

def add(my_phonebook):
    name = input("name:")
    number = input("number:")
    my_phonebook[name] = number
    print("ok!")

def phonebook():
    my_phonebook = {}
    while True:
        command = int(input("command(1 search, 2 add, 3 quit): "))
        if command == 3:
            print("quitting...")
            break
        if command == 2:
            add(my_phonebook)
        if command == 1:
            search(my_phonebook)

phonebook()
