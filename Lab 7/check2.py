def read_board(fn):
    # Start here for checkpoint 1b.  Note that the syntax is not
    # correct until you have filled the for loop
    board = []
    count = 0
    for line in open(fn,'r'):
        board.append([])
        for c in line.strip():
            if c != ' ':
                board[count].append(c)
        count += 1
    return board
                

def print_board( board ):
    # Print each row on a separate line
    for r in range(0,9):
        # Every third row, print a line of ----
        if r%3 == 0:
            print '-'*25

        # Print the contents of each row, with a '|' at the start, at
        # the end, and separating each block
        print '|',
        for c in range(0,9):
            print board[r][c],
            if c==2 or c==5:
                print '|',
            elif c==8:
                print '|'

    # End with a line of ---
    print '-'*25

def verify_board_is_complete(board):
    # Replace this for Checkpoint 3
    return True

def ok_to_add(row,col,num,board):
    #check block
    if row > 8 or col > 8:
        return False
    
    for i in range(row % 3, (row % 3) + 4):
        for j in range(col & 3, (col %3) +  4):
            if i != row and j != col:
                if board[i][j] == num:
                    return False
    
    #check col/row
    for i in range(0,9):
        if i != row:
            if board[i][col] == num:
                return False
        if i != col:
            if board[row][i] == num:
                return False
    
    return True

##################################################

if __name__ == "__main__":
    name = raw_input("Enter the file for the initial Sudoku board ==> ").strip()
    board = read_board(name)
    print_board(board)

    
    # For Checkpoint 2, remove the triple quotes and below
    while True:
        print
        line = raw_input("Enter row col and num (. to erase) to insert (-1 to end) ==> ")
        line = line.split()
        row = int(line[0])
        if row == -1:
            break
        col = int(line[1])
        num = line[2].strip()
        if num == '.':
            board[row][col] = '.'
        elif ok_to_add(row-1,col-1,num,board):
            board[row][col] = num
            print "Updated board"
        else:
            print "Illegal move"
        print_board(board)
    # Remove triple quotes down to here
    

    '''
    # For Checkpoint 3, remove the triple quotes here
    verify_board_is_complete(board)
    '''
