import time
#import os

game_is_going = True
current_player = "X"
clear = lambda: os.system("clear")
cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def how_to_play():
    #patern hoe to play
    print("This is keyboard  setup in the game.  We know is on the contrary then  alfanumeric keyboard. ")
    print("\n")
    line_separator = "--+---+--"
    line_1 = "1" + " | " + "2" + " | " + "3"#lista list[ []  []  []  [] []]
  # board = [ [],[],]  board[0][0]
    line_2 = "4" + " | " + "5" + " | " + "6"
    line_3 = "7" + " | " + "8" + " | " + "9"
    print(line_1)
    print(line_separator)
    print(line_2)
    print(line_separator)
    print(line_3)
    print("\n")


def board(cells):
    # prepare output data
    line_separator = "--+---+--"
    line_1 = cells[0] + " | " + cells[1] + " | " + cells[2]
    line_2 = cells[3] + " | " + cells[4] + " | " + cells[5]
    line_3 = cells[6] + " | " + cells[7] + " | " + cells[8]
    print(line_1)
    print(line_separator)
    print(line_2)
    print(line_separator)
    print(line_3)
    print("\n")


def movement():
  #movement , set and check positon
  move = " "
  global current_player
  list_of_spaces = '1 2 3 4 5 6 7 8 9'.split()
  while move not in list_of_spaces:
    move = input(f"Enter your move {current_player}: ")
    print("\n")
    if move in list_of_spaces:
      move_int = int(move) - 1
      if cells[move_int] == ' ':#print table zmiemiac 0 na puste , 1 na x i 2 na 2 ogolnie na int bo mniej miejsca pamieci zajmują
        cells[move_int] = current_player
      else:
        print("This move is forbidden, try another position")
        print("\n")
        movement()
      board(cells)

def switch_player():
  # switch player
  global current_player
  if current_player == "X" :#  0- puste 1 -X , 2- O./to jest przykład 
    current_player = "O" 
  else:
    current_player = "X"

# funkcja do wygrania - funkcja która przyjmuje listę elementów i sprawdza, czy wszystkie są takie same
# board[0][i],-row  board[i][0],-column  board[i][i],- skos  board[i][len(board) -i ] - do 3D??

def is_win():
  # win or draw 
  sumcells = (cells.count("X") + cells.count("O")) 
  if cells[0] == cells[1] == cells[2] != " ":
    end()
  elif cells[3] == cells[4] == cells[5] != " ":
    end()
  elif cells[6] == cells[7] == cells[8] != " ":
    end()
  elif cells[0] == cells[3] == cells[6] != " ":
    end()
  elif cells[1] == cells[4] == cells[7] != " ":
    end()
  elif cells[2] == cells[5] == cells[8] != " ":
    end()
  elif cells[0] == cells[4] == cells[8] != " ":
    end()
  elif cells[2] == cells[4] == cells[6] != " ":
    end()
  elif sumcells == 9:
    end_2()
  
def end():
  # win end
  global game_is_going
  global current_player
  print(f'{current_player} WIN')
  game_is_going = False
  #input("Czy chcesz zagrać jeszcze raz? ")

def end_2():
  # draw end 
  global game_is_going
  # global current_player
  print("It's a draw")
  game_is_going = False

def game():
  # main function
  how_to_play()
  time.sleep(5)
  board(cells)
  while game_is_going:
    movement()
    #clear = lambda: os.system("clear)
    #clear()
    is_win()
    switch_player()


game()
