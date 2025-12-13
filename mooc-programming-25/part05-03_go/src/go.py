# Write your solution here
def who_won(game_board: list):
    p1 = 0
    p2 = 0
    for i in game_board:
        p1 += i.count(1)
        p2 += i.count(2)

    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    elif p1 == p2:
        return 0
