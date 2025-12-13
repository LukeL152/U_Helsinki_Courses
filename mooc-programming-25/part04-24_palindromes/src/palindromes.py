# Write your solution here
def palindromes(string):
    rev_string = string[::-1]
    if rev_string == string:
        return True
    else:
        return False


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
while True:
    check = input("Please type in a palindrome: ")
    if not palindromes(check):
        print("that wasn't a palindrome")
    elif palindromes(check):
        print(f"{check} is a palindrome!")
        break
