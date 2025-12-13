# Write your solution here
def even_numbers(integers):
    even_list = []
    for i in integers:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
