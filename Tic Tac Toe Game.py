def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # No winner
    return None

def update_score(file_path, user_name, user_wins):
    with open(file_path, 'w') as file:
        file.write(f"{user_name}:{user_wins}")

def get_user_score(file_path, user_name):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(user_name):
                return int(line.split(":")[1])
    return 0

def play_tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    print("Welcome to Tic Tac Toe!")
    user_name = input("Enter your name: ")
    score_file = "user_scores.txt"
    user_wins = get_user_score(score_file, user_name)

    while True:
        print_board(board)

        # User's turn
        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Invalid move. Please try again.")

        winner = check_winner(board)

        if winner:
            print_board(board)
            print("Congratulations! You win!")
            user_wins += 1
            update_score(score_file, user_name, user_wins)
            print("Total wins:", user_wins)
            break

        # Computer's turn
        while True:
            import random
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if board[row][col] == ' ':
                board[row][col] = 'O'
                break

        winner = check_winner(board)

        if winner:
            print_board(board)
            print("Computer wins!")
            print("Total wins:", user_wins)
            break

        # Check if the board is full (tie)
        if all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            print("Total wins:", user_wins)
            break

play_tic_tac_toe()