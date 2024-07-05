mainboard = ['                                 '
         ,'          |           |           '
         ,'          |           |           '
         ,'          |           |           '
         ,'          |           |           '
         ,'----------|-----------|-----------'
         ,'          |           |           '
         ,'          |           |           '
         ,'          |           |           '
         ,'----------|-----------|------------'
         ,'          |           |           '
         ,'          |           |           '
         ,'          |           |           '
         ,'          |           |           ']
miniboard = [' _|','|_|','|_',
             '_|', '|_|','|_',
             '_|', '|_|','|_']

def ShowBoard(game_board):
    for row in range(0,3):
      print(game_board[row])
    
    
a1 = '#'
b1 = '#'
c1 = '#'

a2 = '#'
b2 = '#'
c2 = '#'

a3 = '#'
b3 = '#'
c3 = '#'
board_1 = [['#','#', '#'],['#','#', '#'],['#','#', '#'],]
board = [[a1,b1,c1],[a2,b2,c2], [a3,b3,c3]]
ShowBoard(board)

play = 0
while play < 9:
    play += 1
    space = int(input('Where do you want to play?'))
    board[space[0:0]] = '$'
    ShowBoard(board)
