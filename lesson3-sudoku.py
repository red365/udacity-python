# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

correct2 = [[1,2,3,4], 
            [2,4,1,3], 
            [3,1,4,2], 
            [4,3,2,1]]
            
incorrect6 = [[2,2,2],
              [2,2,2], 
              [2,2,2]]

incorrect7 = [[1,2,3], 
              [2,3,1], 
              [3,1,1]]
              
incorrect8 = [[1,2,3,4,5], 
              [2,3,1,5,6], 
              [4,5,2,1,3], 
              [3,4,5,2,1], 
              [5,6,4,3,2]]
    
# Check list representing a row or column for validity 
def check_row(row):
#    print row
    expected_nums = []
    i = 0
    while i < len(row):
        expected_nums.append(i + 1)
        i += 1

    for num in row:
        # Check input
        if type(num) != int:
            return False
        if num not in expected_nums:
            return False
#        print num
        i = 0
        count = 0
        
        while i < len(row):
#            print num, row[i]
            if num == row[i]:
                count += 1
            if count >= 2:
#                print "duplicate - returning false"
                return False
            i += 1
#        print "count =", count
    return True

    
def check_sudoku(sudoku):
    x = 0
    y = 0
    count = 0

# check for valid input - for some reason this returns false for 'correct2'?!?!
#    if not all(isinstance(item, int) for item in sudoku):
#        print "Throwing False!"
#        return False
    
    # Hack to get around incorrect4 seeing as solution above had to be commented out for some bizarre reason

    
    # Check row for validity
    for row in sudoku:
         count = len(row) # Get number of columns for later, assumes correct number to form a square
         if not check_row(row):
            
            return False
    
    # Build column then check for validity
    while x < count:
        column = []
        while y < len(sudoku):
            column.append(sudoku[y][x])
            y += 1
        if not check_row(column):
            return False
        x += 1
        y = 0
    
    # If both row and column checks do not return False return True
    return True
       

    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False

print check_sudoku(correct2)
# >>> True

print check_sudoku(incorrect6)
#>>> False

print check_sudoku(incorrect7)
#>>> False

print check_sudoku(incorrect8)
#>>> False
