# Write your solution here
def who_won(game_board: list) -> int:
    player1 = 0
    player2 = 0
    for row in game_board:
        for area in row:
            if area == 1:
                player1 += 1
            elif area == 2:
                player2 += 1
    
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0