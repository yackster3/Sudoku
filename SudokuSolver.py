"""
This code uses the backtracking algorithm to solve sudoku puzzles. There are
a few sudoku puzzles that are presented to test the code that are provided.
"""
import numpy as np

"""
    Tests for functions are at the top here, you can see which functions are
    tested in their description. Some are aesthetic, so you can't really test
    them except to see how they measure up to your taste.
"""

def runTests():
    print("Testing valid solution checker")
    testValid()
    print("Testing valid checker")
    testChecker()
    print("Testing Solver")
    testSolve()
    return

def testSolve(puzzle = None):
    if puzzle == None:
        #53 empty cell Sudoku Puzzle
                           #0 1 2 3 4 5 6 7 8
        puzzle = np.array([[1,3,0,8,0,5,6,0,0], # 0
                           [0,0,6,0,2,0,0,0,1], # 1
                           [0,2,0,0,4,0,5,0,0], # 2
                           [0,8,0,0,0,0,0,0,0], # 3
                           [6,0,9,0,0,0,0,0,5], # 4
                           [0,0,0,0,0,0,0,3,0], # 5
                           [0,0,2,0,5,0,0,4,0], # 6
                           [8,0,0,0,3,0,9,0,0], # 7
                           [0,0,1,0,0,2,0,5,7]])#8
                           #0,1,2,3,4,5,6,7,8
    answer = solve(puzzle)
    return answer

"""
    Allows you to test a specified puzzle and get the result
    without inputing any puzzle beforehand.
"""
def testPuzzle(puzzle = None):
    if puzzle == None:
        #53 empty cell Sudoku Puzzle
                           #0 1 2 3 4 5 6 7 8
        puzzle = np.array([[1,3,0,8,0,5,6,0,0], # 0
                           [0,0,6,0,2,0,0,0,1], # 1
                           [0,2,0,0,4,0,5,0,0], # 2
                           [0,8,0,0,0,0,0,0,0], # 3
                           [6,0,9,0,0,0,0,0,5], # 4
                           [0,0,0,0,0,0,0,3,0], # 5
                           [0,0,2,0,5,0,0,4,0], # 6
                           [8,0,0,0,3,0,9,0,0], # 7
                           [0,0,1,0,0,2,0,5,7]])#8
                           #0,1,2,3,4,5,6,7,
    return puzzle

def testValid():
    if testBox():
        if testRow():
            if testCol():
                if testSolution():
                    print("Passed all tests")
                    return

    raise ValueError("Test Failed")

"""
    Contains the test case of a single box check
"""
def testBox():
    #Test Case check number in the same box
    puzzleA = np.array([[0,0,0,0,0,0,0,0,0], # 0
                       [0,0,9,6,0,8,1,2,0], # 1
                       [1,0,0,7,0,4,6,0,0], # 2
                       [4,0,0,3,0,0,8,0,0], # 3
                       [5,1,0,0,3,0,0,7,2], # 4     Error in the center 3x3
                       [0,0,8,0,0,2,0,0,3], # 5
                       [0,0,5,4,0,7,0,0,8], # 6
                       [0,8,3,5,0,6,7,0,0], # 7
                       [0,0,0,0,0,0,0,0,0]])# 8
                       #0,1,2,3,4,5,6,7,8
    if checkValid(puzzleA, 3,3):
        print("Find the error")
        print(puzzleA)
        raise ValueError("Failed test case SAME BOX!")
    else:
        return True
"""
    Contains the test case for the rows
"""
def testRow():
    #Test Case check number in the same row
    puzzleB = np.array([[0,0,0,0,0,0,0,0,0], # 0
                       [0,2,9,6,0,8,1,2,0], # 1     Error on row 1
                       [1,0,0,7,0,4,6,0,0], # 2
                       [4,0,0,3,0,0,8,0,0], # 3
                       [5,3,0,0,0,0,0,7,2], # 4
                       [0,0,8,0,0,2,0,0,3], # 5
                       [0,0,5,4,0,7,0,0,8], # 6
                       [0,8,3,5,0,6,7,0,0], # 7
                       [0,0,0,0,0,0,0,0,0]])# 8
                       #0,1,2,3,4,5,6,7,8

    #Test Case check number in the same row
    if checkValid(puzzleB, 1,1):
        print("Find the error:")
        print(puzzleB)
        raise ValueError("Failed test case SAME ROW!")
    else:
        return True

"""
    Contains the test case for the columns
"""
def testCol():
    print("Testing Column:")
    puzzleC = np.array([[0,0,0,0,0,0,0,0,0], # 0
                        [0,0,9,6,0,8,1,2,0], # 1
                        [1,0,0,7,0,4,6,0,0], # 2
                        [4,0,0,3,0,0,8,0,0], # 3
                        [5,3,0,0,0,0,0,7,2], # 4
                        [0,0,8,0,0,2,0,0,3], # 5
                        [0,0,5,4,0,7,0,0,8], # 6
                        [0,8,3,5,0,6,7,0,0], # 7
                        [0,0,0,3,0,0,0,0,0]])# 8
                        #0,1,2,3,4,5,6,7,8      The error is on column 3

    if checkValid(puzzleC, 3,3):
        print("Find the error:")
        printBoard(puzzleC)
        raise ValueError("Failed test case SAME COL!")
    else:
        return True

"""
    Contains the test case for recognizing a solved puzzle
"""
def testSolution():
    #Test Case check solved puzzle
    puzzleD = np.array([[7,5,9,4,6,3,2,8,1], # 0
                       [1,8,3,5,2,7,9,4,6], # 1
                       [4,2,6,8,9,1,5,7,3], # 2
                       [6,7,2,3,1,4,8,9,5], # 3
                       [8,3,5,2,7,9,6,1,4], # 4
                       [9,4,1,6,8,5,7,3,2], # 5
                       [5,6,7,1,3,8,4,2,9], # 6
                       [2,1,8,9,4,6,3,5,7], # 7
                       [3,9,4,7,5,2,1,6,8]])# 8
                       #0,1,2,3,4,5,6,7,8
    if checkValid(puzzleD, 1,1):
        print("Success!")
        return True
    else:
        raise ValueError("Solution deemed invalid!")

"""
    Another test checker
"""
def testChecker():
    #Test Case check number in the same box
    puzzle = np.array([[0,0,0,0,0,0,0,0,0], # 0
                       [0,0,9,6,0,8,1,2,0], # 1
                       [1,0,0,7,0,4,6,0,0], # 2
                       [4,0,0,3,0,0,8,0,0], # 3
                       [5,3,0,0,3,0,0,7,2], # 4
                       [0,0,8,0,0,2,0,0,3], # 5
                       [0,0,5,4,0,7,0,0,8], # 6
                       [0,8,3,5,0,6,7,0,0], # 7
                       [0,0,0,0,0,0,0,0,0]])#8
                       #0,1,2,3,4,5,6,7,8
    if checker(puzzle):
        print("Find the error")
        print(puzzle)
        raise ValueError("Failed test case SAME BOX!")
    #Test Case check number in the same row
    puzzle = np.array([[0,0,0,0,0,0,0,0,0], # 0
                       [0,2,9,6,0,8,1,2,0], # 1
                       [1,0,0,7,0,4,6,0,0], # 2
                       [4,0,0,3,0,0,8,0,0], # 3
                       [5,3,0,0,0,0,0,7,2], # 4
                       [0,0,8,0,0,2,0,0,3], # 5
                       [0,0,5,4,0,7,0,0,8], # 6
                       [0,8,3,5,0,6,7,0,0], # 7
                       [0,0,0,0,0,0,0,0,0]])#8
                       #0,1,2,3,4,5,6,7,8
    if checker(puzzle):
        print("Find the error:")
        print(puzzle)
        raise ValueError("Failed test case SAME ROW!")

    #Test Case check number in the same column
    puzzle = np.array([[0,0,0,0,0,0,0,0,0], # 0
                       [0,3,9,6,0,8,1,2,0], # 1
                       [1,0,0,7,0,4,6,0,0], # 2
                       [4,0,0,3,0,0,8,0,0], # 3
                       [5,3,0,0,0,0,0,7,2], # 4
                       [0,0,8,0,0,2,0,0,3], # 5
                       [0,0,5,4,0,7,1,0,8], # 6
                       [0,8,3,5,0,6,7,0,0], # 7
                       [0,0,0,0,0,0,0,0,0]])#8
                       #0,1,2,3,4,5,6,7,8
    if checker(puzzle):
        print("Find the error:")
        print(puzzle)
        raise ValueError("Failed test case SAME COL!")
    #Test Case check solved puzzle
    puzzle = np.array([[7,5,9,4,6,3,2,8,1], # 0
                       [1,8,3,5,2,7,9,4,6], # 1
                       [4,2,6,8,9,1,5,7,3], # 2
                       [6,7,2,3,1,4,8,9,5], # 3
                       [8,3,5,2,7,9,6,1,4], # 4
                       [9,4,1,6,8,5,7,3,2], # 5
                       [5,6,7,1,3,8,4,2,9], # 6
                       [2,1,8,9,4,6,3,5,7], # 7
                       [3,9,4,7,5,2,1,6,8]])#8
                       #0,1,2,3,4,5,6,7,8
    if checker(puzzle):
        print("Success!")
    else:
        raise ValueError("Solution deemed invalid!")


"""

"""
def testAnswerCheck(tell = False, puzzle = None):
    if puzzle == None:
        puzzle = np.array([[1,3,0,8,0,5,6,0,0], # 0
                        [0,0,6,0,2,0,0,0,1], # 1
                        [0,2,0,0,4,0,5,0,0], # 2
                        [0,8,0,0,0,0,0,0,0], # 3
                        [6,0,9,0,0,0,0,0,5], # 4
                        [0,0,0,0,0,0,0,3,0], # 5
                        [0,0,2,0,5,0,0,4,0], # 6
                        [8,0,0,0,3,0,9,0,0], # 7
                        [0,0,1,0,0,2,0,5,7]])#8
                        #0,1,2,3,4,5,6,7,8
    guess = int(input("Please guess a value: "))
    x = int(input("Please input x: "))
    y = int(input("Please input y: "))
    print(type(x))
    print(type(y))
    xB, yB = 5,2
    if checkAnswer(puzzle, guess, x, y, tell):
        if not checkAnswer(puzzle, guess, xB, yB, tell):
            print("Success!")
        else:
            raise ValueError("Invalid response: ", (guess, xB,yB))
    else:
        raise ValueError("Invalid response: ", (guess, x,y))

"""
    Test Function: "def testChecker():"
    Status: Success
    Purpose: Tests the current state of the puzzle to determine if it is or is not solved.
"""
def checker(puzzle):
    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle)):
            if not checkValid(puzzle, i, j):
                return False
    return True

"""
    Test Function: "def testValid():"
    Status: Fails on Column exclusively
    Purpose: Tests the current state of the puzzle to determine if it is or is not solved.
"""
def checkValid(puzzle, x, y, maximum = 9, minimum = 0):

    # Zero's are null values, so default true
    if puzzle[x][y] == 0:
        return True

    # Checks that the value is within bounds
    if puzzle[x][y] > maximum or puzzle[x][y] < minimum:
        return False

    #Gets one of the individual groups of 9 squares.
    group = x//3, y//3

    for i in range(group[0]*3, group[0]*3+3):
        for j in range(group[1]*3, group[1]*3+3):
            if (i != x or j != y) and puzzle[i][j] == puzzle[x][y]:
                return False

    #Checks the rows and columns
    for i in range(0, len(puzzle)):
        #Checking Column
        if puzzle[x][i] == puzzle[x][y] and i != y:
            return False

        #Checking Row
        elif puzzle[i][y] == puzzle[x][y] and i != x:
            return False
    return True

"""
    Test Function: "def testSolve():"
    Status: Success
    Purpose: Solve sudoku puzzle input as an array
    extras: progress T/F for printing the progress as you
    approach the solution.
"""
def solve(puzzle, progress = False):
    #Get the coordinates of the empty cells.
    coords = []
    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle)):
            if puzzle[i][j] == 0:
                coords.append((i,j))
                
    index = 0
    furthest = 0
    while index < len(coords) and index >= 0:
        #Find an empty cell
        x, y = coords[index]
        #Try numbers starting with 1
        puzzle[x][y] += 1
        while not checkValid(puzzle, x, y):

            puzzle[x][y] += 1
            #If all numbers invalid return to 0 and backtrack
            if puzzle[x][y] > 9:
                puzzle[x][y] = 0

        #If cell value returned to 0, continue backtracking
        if puzzle[x][y] == 0:
            if furthest < index and progress:
                furthest = index
                print("Backtracking")
                printBoard(puzzle)
            index -= 1
        else:
            index += 1
    if index < 0:
        raise ValueError("invalid Puzzle Presented, no numbers work for first empty cell")

    return puzzle

"""
    This uses the solve function to solve the puzzle but returns the solution so it's
    easier to read. Solve just returns the raw array.
"""
def printSolution(puzzle):
    return printBoard(solve(puzzle))

"""
    Prints the board all nice and neat. Usint '-' and '|' for lines
    in the sudoku puzzle.
"""
def printBoard(puzzle):
    for i in range(len(puzzle)):
        if i%3==0 and i != 0:
            print("---------------------")
        for j in range(0, len(puzzle[0])):
            if j%3 == 0 and j != 0:
                print("| ", end = "")
            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end = "")

"""
    Test Function: "def testAnswerCheck():"
    Status: Success
    Purpose: checks the answers of a Sudoku Puzzle as you solve it
    extras: tell T/F to tell you the correct answer if you're wrong.
"""
def checkAnswer(puzzle, yourAnswer, x, y, tell = False):
    solution = solve(puzzle)
    if solution[x][y] == yourAnswer:
        if tell:
            print("Have more confindence than to try cheating.")
        return True
    else:
        if tell:
            print("Cheater, the answer is: ", solution[x][y])
        return False

"""
    I think this will be a useful function to try to make and solve
    n-d sudoku puzzles.
    It basically gets the dimensions of a list.
"""
def getDimensions(puzzle, myArray = []):
    try:
        l = len(puzzle)
        myArray.append(l)
        return getDimensions(puzzle[0], myArray)

    except TypeError:
        return myArray

"""
    Gets a value based on the coordinates provided.
"""
def getValue(coords, puzzle):
    try:
        return getValue(coords[1:], puzzle[coords[0]])
    except TypeError:
        return puzzle

"""
    TODO: Iterate through the puzzle with varying numbers of coordinates and numbers in the puzzle.
"""
def validSolution(val, coordinate, puzzle):
    dimensions = getDimensions(puzzle)
    totalNum = len(dimensions)**dimensions[0]
    comp = list(np.zeros(len(coordinates)))
