# Write your solution here
editor = ""

while editor.lower() != "visual studio code":
    editor = input("Editor: ")

    if editor.lower() == "visual studio code":
        print(f"an excellent choice!")
        break
    elif editor.lower() == "notepad" or editor.lower() == "word":
        print(f"awful")
    else:
        print(f"not good")
