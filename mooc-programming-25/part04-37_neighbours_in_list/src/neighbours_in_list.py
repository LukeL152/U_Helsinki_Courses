# Write your solution here
def longest_series_of_neighbours(int_list):
    if len(int_list) < 2:
        return 1  # or 0 depending on MOOC expectations

    longest = 1
    current = 1

    for i in range(len(int_list) - 1):
        if abs(int_list[i] - int_list[i + 1]) == 1:
            current += 1
        else:
            if current > longest:
                longest = current
            current = 1

    # Final check after loop
    if current > longest:
        longest = current

    return longest
