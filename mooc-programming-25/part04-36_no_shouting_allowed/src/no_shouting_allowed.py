# Write your solution here
def no_shouting(str_list):
    no_shout = []
    for string in str_list:
        if not string.isupper():
            no_shout.append(string)
    return no_shout
