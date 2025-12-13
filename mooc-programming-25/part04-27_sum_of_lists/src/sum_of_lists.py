# Write your solution here
def list_sum(integers1, integers2):
    length = len(integers1)
    i = 0
    sum_list = []
    while i < length:
        sum = integers1[i] + integers2[i]
        sum_list.append(sum)
        i += 1
    return sum_list
