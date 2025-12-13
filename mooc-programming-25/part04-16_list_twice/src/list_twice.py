# Write your solution here

list1 = []
list_sorted = []
while True:
    val = int(input("New item: "))
    if val == 0:
        print("Bye!")
        break
    else:
        list1.append(val)
        print(f"The list now: {list1}")

        list_sorted.append(val)
        list_sorted.sort()
    print(f"The list in order: {list_sorted}")
