def generate_chessboard():
    for row in range(8):
        line = ""
        for col in range(8):
            if (row + col) % 2 == 0:
                line += "X"
            else:
                line += "O"
        print(line)


generate_chessboard()
