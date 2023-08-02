# Intern2grow

## Area Calculator
It will display a menu to the user where they can choose the shape for which they want to calculate the area (square, rectangle, or circle). Based on their choice, the program will ask for the required inputs (side length, rectangle length and width, or circle radius) and calculate the area accordingly. The result will then be printed on the screen. The program will continue to run until the user chooses to exit.

## Calc Library
The file "arithmetic_operations.py" contains four functions: add, subtract, multiply, and divide. These functions perform addition, subtraction, multiplication, and division operations respectively. The divide function checks if the divisor is zero and raises a ValueError in such cases.

## Words Counter
It will prompt you to enter the file path of the file you want to analyze. After providing the file path, the program will read the contents of the file and perform the analysis. It will calculate the number of characters, words, and sentences in the file using the respective functions (count_characters, count_words, count_sentences). Finally, it will display the analysis results on the console.

## Tic Tac Toe Game
The Tic Tac Toe game is played between the user and the computer. The user's name is requested at the beginning of the game, and the number of user wins is retrieved from a text file (user_scores.txt) using the get_user_score function. After each game, if the user wins, the score is updated by incrementing the user's win count and the update_score function is called to write the updated score to the file. The current score is displayed to the user after each game. The file format used to store the scores is user_name:user_wins.
