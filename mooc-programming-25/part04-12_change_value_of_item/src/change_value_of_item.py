# Write your solution here
list1 = [1, 2, 3, 4, 5]
index = 0

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    else:
        val = int(input("New Value: "))
        list1[index] = val
        print(list1)
