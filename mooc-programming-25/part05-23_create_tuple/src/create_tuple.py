# Write your solution here
def create_tuple(x: int, y: int, z: int):
    integers = [x, y, z]
    integers.sort()
    sum = x + y + z
    int_tuple = (integers[0], integers[2], sum)
    return int_tuple

