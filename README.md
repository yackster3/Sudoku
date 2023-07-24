# Sudoku
Just some fun sudoku stuff
to use, first you must make an np.array with dimensions 9x9 with numbers 1-9 in each cell organized like a regular sudoku puzzle.

In other words to print a puzzle like this:
>>>1 2 3 | 4 5 6 | 7 8 9
>>>
>>>4 5 6 | 7 8 9 | 1 2 3
>>>
>>>7 8 9 | 1 2 3 | 4 5 6
>>>
>>>----------------------
>>>
>>>2 3 1 | 5 6 4 | 8 9 7 
>>>
>>>5 6 4 | 8 9 7 | 2 3 1
>>>
>>>8 9 7 | 2 3 1 | 5 6 4
>>>
>>>----------------------
>>>
>>>3 1 2 | 6 4 5 | 9 7 8
>>>
>>>6 4 5 | 9 7 8 | 3 1 2
>>>
>>>9 7 8 | 3 1 2 | 6 4 5

you write:

>>>x = np.array([[1,2,3,4,5,6,7,8,9],
[4,5,6,7,8,9,1,2,3],
[7,8,9,1,2,3,4,5,6],
[2,3,1,5,6,4,8,9,7],
[5,6,4,8,9,7,2,3,1],
[8,9,7,2,3,1,5,6,4],
[3,1,2,6,4,5,8,7,8],
[6,4,5,9,7,8,3,1,2],
[9,7,8,3,1,2,6,4,5]])

>>>printBoard(x)

if you don't know the number at a certain location place a 0 there as a placeholder.

the code contains a few main functions

1) def printSolution(puzzle):

  A function that will print the solution to the puzzle input as an array formatted as described above.
  The output will be formatted using the "printBoard" function
  
2) def checkAnswer(puzzle, yourAnswer, x,y, tell = False):

    Checks the answers of a puzzle input as an array as described above, and returns a True of False if the answer is correct or not.
    If tell is True then it will print a message, and tell you the answer if you are incorrect.
    
 3) def solve(puzzle, progress = False):
    
    Solves the puzzle when input as described above, and then returns the solved puzzle as an array described above.
    
    If you would like to see the solution to the puzzle as the algorithm works, you can change progress to True,
    this won't show every step but the solution as the puzzle begins backtracking at the next furthest point it's
    reached.
