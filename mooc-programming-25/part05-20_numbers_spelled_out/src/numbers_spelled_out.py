# Write your solution here
def dict_of_numbers():
    ones = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    numbers = {}

    for i in range(100):
        if i < 10:
            numbers[i] = ones[i]
        elif i < 20:
            numbers[i] = teens[i]
        else:
            ten = (i // 10) * 10
            one = i % 10
            if one == 0:
                numbers[i] = tens[ten]
            else:
                numbers[i] = f"{tens[ten]}-{ones[one]}"

    return numbers
