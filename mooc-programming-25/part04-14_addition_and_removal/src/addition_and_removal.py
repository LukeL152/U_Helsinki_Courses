# Write your solution here
list1 = []
choice = ""
prev_num = 0
num = 1

while True:
    print(f"The list is now {list1}")
    choice = input("a(d)d, (r)emove or e(x)it:")
    if choice == "x":
        break
    elif choice == "d":
        list1.append(num)
        num += 1
        prev_num += 1
    elif choice == "r":
        list1.remove(prev_num)
        num -= 1
        prev_num -= 1


print(f"Bye!")
