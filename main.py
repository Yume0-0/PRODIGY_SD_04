grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

sub_grids = [grid[0][0] , grid[0][1] , grid[0][2] ,
             grid[1][0], grid[1][1] , grid[1][2] ,
             grid[2][0], grid[2][1] , grid[2][2]]

# Function to take puzzle input from the user
def puzzle_input():
    for i in range(0,9):
        for j in range(0,9):
                    n = input(f'Enter the number between 1 and 9 for cell ({i+1}, {j+1}) or press enter to keep empty: ')
                    if n == '' :
                        continue
                    while n != '' and (not n.isdigit() or not 1<= int(n) <=9) :
                      n = input('please enter a number between 0 and 9 :        ')
                    grid[i][j] = int(n)
    print(grid)
    print("The input Sudoku grid is :")
    for i in range(0,9):
        row = ''
        for j in range(0,9):
            row += str(grid[i][j]) + ' '
            if (j + 1) % 3 == 0  and j != 8:
                row += '| '
        print(row)
        if (i+1) % 3 == 0 and i != 8 :
            print('-'* 21)


def empty_cell() :
    for i in range(9):
        for j in range(9) :
            if grid[i][j]==0:
                return i , j
    return None,None

def check_if_valid(grid ,row , col , number ) :
    if number in grid[row]:
        return False
    if number in [grid[i][col] for i in range(9)]:
        return False

    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == number:
                return False
    return True

# Placeholder for the grid_input function
def backtracking():
    i , j = empty_cell()
    if i == None :
        return True
    for guess in range(1,10):
        if check_if_valid(grid , i , j , guess) :
            grid[i][j] = guess
            if backtracking() :
                return True
            grid[i][j] = 0

    return False


def game_loop() :
    print('welcome to the sudoku puzzle game ! you can input you own puzzle then start the process of backtracking , give it a try and input S to start or E to exist the game :D !!')
    decision = input('your answer       :  ')
    if decision == 'S' :
        puzzle_input()
        if backtracking():
            print("Sudoku solved successfully!")
            for row in grid:
                print(row)
        else:
            print("No solution exists for the given Sudoku.")


game_loop()