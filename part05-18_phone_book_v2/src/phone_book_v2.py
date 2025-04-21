# Write your solution here
def search(my_phonebook):
    name = input("name:")
    if name in my_phonebook:
        for number in my_phonebook[name]:
            print(number)
    if name not in my_phonebook:
        print("no number")

### When name in my_phonebook
###     add number to already existing number in a list
def add(my_phonebook):
    name = input("name:")
    number = input("number:")
    if name not in my_phonebook:
        my_phonebook[name] = []
    my_phonebook[name].append(number)
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
