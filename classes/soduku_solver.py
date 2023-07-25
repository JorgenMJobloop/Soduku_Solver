static_board = [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def animate_ascii_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("----------------")
            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(r" | ", end="")
                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

def find_empty_num(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j) # return tuples of iterator i & j
    return None



def solve_board(board, valid_num, pos):
    find_num = find_empty_num(board=any)
    if not find_num:
        return True
    else:
        row, col = find_num

    for i in range(1,10):
        if valid_num(board, i, (col, row)):
            board[row][col] = i
        
        if solve_board(board):
            return True
        board[row][col] = 0

    return False

def valid_numbers(board,num,pos):
    for i in range(len(board)):
        if board[pos[i][0]] == num and pos[1] != i:
            return False
    for j in range(len(board)):
        if board[pos[j][0]] == num and pos[1] != j:
            return False
        
    x_pos = pos[1] // 3
    y_pos = pos[0] // 3

    for g in range(x_pos*3, y_pos*3 + 3):
        for h in range(x_pos*3, y_pos*3 + 3):
            if board[g][h] == num and (g,h) != pos:
                return False
    return True              



