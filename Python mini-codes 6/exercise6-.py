def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # 检查行
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # 检查列
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # 检查对角线
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_full(board):
    return all([cell != " " for row in board for cell in row])


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn:")

        # 获取用户输入
        while True:
            try:
                row, col = map(
                    int,
                    input("Enter row and column (0-2) separated by a space: ").split(),
                )
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input, please enter numbers between 0 and 2.")

        # 检查是否有赢家
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # 检查是否平局
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1


tic_tac_toe()
