import timeit

##reads csv file, returns a list of lists
def get_board(csvfile):
    csvlist=[]
    fp=open(csvfile)
    for i in fp:
        csvlist.append(i.strip().split(','))
    fp.close()
    return csvlist

##returns characters (not empty) present in given row
def in_row(board,row,column):
    Row=[]
    for i in board[row]:
        if i=='+':
            continue
        else:
            Row.append(int(i))
    return Row

##returns characters (not empty) present in given column
def in_column(board,row,column):
    Col=[]
    for i in range(len(board)):
        if board[i][column]=='+':
            continue
        else:
            Col.append(int(board[i][column]))
    return Col

##returns characters (not empty) present in given sector
def in_sector(board,row,column):
    Sec=[]
    seclen=int((len(board[row]))**(.5))
    for i in range(seclen):
        if row<(seclen*(i+1)):
            for j in range(seclen):
                if column<(seclen*(j+1)):
                    for k in range((seclen*i),(seclen*(i+1))):
                        for l in range((seclen*j),(seclen*(j+1))):
                            if board[k][l]=='+':
                                continue
                            else:
                                Sec.append(int(board[k][l]))
                    return Sec

##returns coordinates of first empty cell in board
##if none, returns empty list (BASE CASE)
def get_blank(board):
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j]=='+':
                return [i,j]
    return []

##prints board with solved characters present    
def print_board(board):
    print('+','---+'*len(board[0]),sep='')
    for i in board:
        print('| ', end='')
        for j in i:
            if j=='+':
                print(' ',' | ',sep='',end='')
            else:
                print(j,' | ',sep='',end='')
        print('')
        print('+','---+'*len(board[0]),sep='')

##returns a list of potential characters for given board
def valid_characters(board):
    validlist=[]
    for i in range(len(board)):
        validlist.append(i+1)
    return validlist

##attempts to solve board, returns True or False
##if True: prints completed board
def solve(board):
    blank=get_blank(board)
    row=blank[0]
    column=blank[1]    
##what values should be tried for this empty cell
    validlist=valid_characters(board)
    Row=in_row(board,row,column)
    Col=in_column(board,row,column)
    Sec=in_sector(board,row,column)
    for i in Row:
        if i in validlist:
            validlist.remove(i)
        else:
            continue
    for i in Col:
        if i in validlist:
            validlist.remove(i)
        else:
            continue
    for i in Sec:
        if i in validlist:
            validlist.remove(i)
        else:
            continue
##base case if no legal moves to be made
    if validlist==[]:
        return False
    for i in validlist:
##records guess in current cell
        board[row][column]=i
##base case if board is complete
        if get_blank(board)==[]:
            return True
        else:
            if solve(board):
                return True
##resets cell to empty if guesses did not work
    board[row][column]='+'
    return False

    

board=(get_board('sudoku.csv'))

print_board(board)
start_time=timeit.default_timer()
if solve(board):
    print(timeit.default_timer()-start_time)
    print_board(board)
