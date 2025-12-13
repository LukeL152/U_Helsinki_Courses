# Write your solution here
def formatted(floats):
    formatted_list = []
    for i in floats:
        f_str = str(f"{i:.2f}")
        formatted_list.append(f_str)
    return formatted_list

