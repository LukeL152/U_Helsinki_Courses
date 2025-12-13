# Write your solution here
def factorials(n: int):
    key = {}
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        key[i] = fact

    return key

