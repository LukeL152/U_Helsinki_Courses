# Write your solution here
layers = int(input("Layers: "))

size = 2 * layers - 1
center = layers - 1

for row in range(size):
    for col in range(size):
        distance = max(abs(row - center), abs(col - center))
        letter = chr(ord("A") + distance)
        print(letter, end="")
    print()
