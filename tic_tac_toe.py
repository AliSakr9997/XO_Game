#setup

board=["1","2","3",
       "4","5","6",
       "7","8","9"]

player1={"number":1,"symbol":"X"}
player2={"number":2,"symbol":"O"}

player = player1 
wineer = None
game_running = True



#board 
def print_board(board):
  print('\n'+board[0]+'|'+board[1]+'|'+board[2])
  print("-----")
  print(board[3]+'|'+board[4]+'|'+board[5])
  print("-----")
  print(board[6]+'|'+board[7]+'|'+board[8]+'\n')



#start_play
def Game_on(board):
  
  global player,wineer,game_running

  print_board(board)
  print(" ")

  while game_running:

    play = int(input(f"player {player['number']} turn! , choose where to play {player['symbol']} :" ))

    if play>9 or play<0:
      print("invalid input")

    elif board[play-1]=='X' or board[play-1]=='O':
      print("\nyou cant play here\n")

    else:
      board[play-1]=player["symbol"]
      print_board(board)

      if check_win(board):
        if tie_checker(board):
          if player==player1:
            player=player2
          else:
            player=player1






#check win
def check_win(board):

  win =False
  global player,wineer,game_running
  
  if board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]:
    print(f"player {player['number']} win with three {player['symbol']} in one row ! ")
    win =  True

  elif board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8]:
    print(f"player {player['number']} win with three {player['symbol']} in one column ! ")
    win =  True

  elif board[0]==board[4]==board[8] or board[2]==board[4]==board[6] :
    print(f"player {player['number']} win with three {player['symbol']} in one diagonal ! ")
    win =  True

  if win:
   game_running = False
   winner = player
  return not win
  


#check tie

def tie_checker(board):
  global player,wineer,game_running

  for i in range(len(board)):
    if board[i]!='X' and board[i]!='O':
      return game_running
    else:
      print("tie")
      game_running = False
      return game_running


Game_on(board)