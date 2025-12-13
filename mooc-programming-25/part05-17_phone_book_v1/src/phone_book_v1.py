# Write your solution here
book = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        book[name] = number
        print("ok!")
    elif command == 1:
        name = input("name: ")
        print(book.get(name, "no number"))
