import os
import numpy as np
clear = lambda: os.system('cls')

global play
play = '🔴'
board = np.array([['  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ']])


InGame = True

def listToString(s):
  str1 = ""
  return (str1.join(s))


def BoardPrint():
  clear()
  print('___ A __|___ B __|___ C __|___ D __|___ E __|___ F __|___ G __')
  for i in range(0, 6):
    row = ''
    for index, j in enumerate(board[i]):
      st = '   '
      st2 = '   |'
      if (index == 6):
        row += (st + j + st)
      else:
        row += (st + j + st2)
    print(row)
    print('--------|--------|--------|--------|--------|--------|--------')


def AddPiece(column, player):
  for i in reversed(range(0, 6)):
    if (board[i][column] == '  '):
      board[i][column] = player
      return True

  return False


def Verify():
  for i in board:
    txt = listToString(i)
    if ('🔴🔴🔴🔴' in txt):
      print('Red win.')
      return False
    elif ('🔵🔵🔵🔵' in txt):
      print('Blue win.')
      return False
  #Column auth
  for i in range(0, 7):
    txt = ''
    for j in range(0, 6):
      txt += board[j][i]
    if ('🔴🔴🔴🔴' in txt):
      print('Red win.')
      return False
    elif ('🔵🔵🔵🔵' in txt):
      print('Blue win.')
      return False
  #Diagonla auth
  for i in range(-2, 4):
    txt1 = listToString(np.diag(board, i))
    txt2 = listToString(np.diag(np.rot90(board), i))
    if ('🔴🔴🔴🔴' in txt1 or '🔴🔴🔴🔴' in txt2):
      print('Red win.')
      return False
    elif ('🔵🔵🔵🔵' in txt1 or '🔵🔵🔵🔵' in txt2):
      print('Blue win.')
      return False
  return True


def SetColumn():
  colToPut = 0
  colInf = input("Select the column:")
  if (colInf == 'a' or colInf == 'A'):
    colToPut = 0
  elif (colInf == 'b' or colInf == 'B'):
    colToPut = 1
  elif (colInf == 'c' or colInf == 'C'):
    colToPut = 2
  elif (colInf == 'd' or colInf == 'D'):
    colToPut = 3
  elif (colInf == 'e' or colInf == 'E'):
    colToPut = 4
  elif (colInf == 'f' or colInf == 'F'):
    colToPut = 5
  elif (colInf == 'g' or colInf == 'G'):
    colToPut = 6
  else:
    clear()
    BoardPrint()
    print("That is not a valid column.")
    return SetColumn()
  return colToPut


def Game(player):
  col = SetColumn()
  if (AddPiece(col, player)):
    return '🔵' if player == '🔴' else '🔴'
  else:
    return player


while InGame:
  BoardPrint()
  InGame = Verify()
  if (InGame):
    play = Game(play)
