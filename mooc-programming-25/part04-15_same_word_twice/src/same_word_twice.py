# Write your solution here
i = 0
word_list = []

while True:
    word = input("Word: ")
    if word in word_list:
        print(f"You typed in {i} different words")
        break
    word_list.append(word)
    i += 1
