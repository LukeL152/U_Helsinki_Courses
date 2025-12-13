# Write your solution here
num_items = int(input("How many items: "))
list1 = []
i = 1

while i <= num_items:
    add = int(input(f"Item {i}:"))
    list1.append(add)
    i += 1

print(list1)
