# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # 1. Validate coordinates (must be 0, 1, or 2)
    if not (0 <= x <= 2 and 0 <= y <= 2):
        return False

    # 2. Check if the target square is empty
    if game_board[y][x] != "":
        return False

    # 3. Place the piece
    game_board[y][x] = piece
    return True

