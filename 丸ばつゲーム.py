gameBoard = [0,1,2,3,4,5,6,7,8] # ゲームに利用する盤面
gameBoard = [0,'o',2,3,4,5,6,7,8] # プレイヤーが座標1に'o'を入力
gameBoard = [0,'o',2,3,4,5,6,7,8] # プレイヤーが座標1に'o'を入力
0o2
345
678
gameBoard = [0,'o',2,3,4,5,6,7,8] # こんな盤面の時
print(gameBoard[1]) # ← こうすると o が表示される
gameBoard = [0,'o',2,3,4,5,6,7,8] # こんな盤面の時
print(gameBoard[1]) # ← こうすると o が表示される
for i in range(0, len(gameBoard)):
    if(i%3 == 2): # 3回に1回は改行
        print(gameBoard[i]) # 改行する
    else :
        print(gameBoard[i], end="") # 改行しない
if(i%3 == 2):
gameBoard = [0,1,2,3,4,5,6,7,8] # ゲームに利用する盤面

for i in range(0, len(gameBoard)):
    if(i%3 == 2): # 3回に1回は改行
        print(gameBoard[i]) # 改行する
    else :
        print(gameBoard[i], end="") # 改行しない

012
345
678
gameBoard = [0,1,2,3,4,5,6,7,8] # ゲームに利用する盤面

# 盤面を3x3で表示する関数
def displayBoard():
    for i in range(0, len(gameBoard)):
        if(i%3 == 2): # 3回に1回は改行
            print(gameBoard[i]) # 改行する
        else :
            print(gameBoard[i], end="") # 改行しない

# ここが本命
displayBoard() # 盤面表示
print('Hello!') # 無駄にHelloを表示
displayBoard() # 盤面表示
def displayBoard():

012
345
678
Hello!!
012
345
678
def inputBoard(playerType):
# ターンを進めるための関数
def inputBoard(playerType):
    # 1.座標を入力させる
    if(playerType == "o"):  # o が渡されたら座標を入力
        tgt = int(input("0~8の座標を入れてください: "))
    else: # xが渡されたらランダムで座標を入力
        tgt = random.randint(0,8)

    # 2.入力座標に 'o'か 'x' が入っていたら再入力
    if(gameBoard[tgt] == 'o' or gameBoard[tgt] == 'x'):
        inputBoard(playerType)

    # 3.gameBoardに反映
    else:
        gameBoard[tgt] = playerType


inputBoard('o') # これでユーザーに入力をさせることができる
inputBoard('x') # これでCPUに入力をさせることができる
tgt = int(input("0~8の座標を入れてください: ")) # プレイヤーの入力座標受付
tgt = random.randint(0,8)
import random
def inputBoard(playerType):
    # 1.座標を入力させる
    if(playerType == "o"):  # o が渡されたら座標を入力
        tgt = int(input("0~8の座標を入れてください: "))
    else: # xが渡されたらランダムで座標を入力
        tgt = random.randint(0,8)
# 2.入力座標に 'o'か 'x' が入っていないことを確認
if(gameBoard[tgt] == 'o' or gameBoard[tgt] == 'x'): inputBoard(playerType)
if( 条件A or 条件B): 実行するもの 
# 3.gameBoardに反映
else: gameBoard[tgt] = playerType
import random

gameBoard = [0,1,2,3,4,5,6,7,8] # ゲームに利用する盤面

# 盤面を3x3で表示する
def displayBoard():
    # gameBoardの要素を1つずつ表示
    for i in range(0, len(gameBoard)):
        if(i%3 == 2): # 3回に1回は改行
            print(gameBoard[i]) # 改行する
        else :
            print(gameBoard[i], end="") # 改行しない

# ターンを進める
def inputBoard(playerType):
    # 1.座標を入力させる
    if(playerType == "o"):  # o が渡されたら座標を入力
        tgt = int(input("0~8の座標を入れてください: "))
    else: # xが渡されたらランダムで座標を入力
        tgt = random.randint(0,8)

    # 2.入力座標に 'o'か 'x' が入っていないことを確認
    if(gameBoard[tgt] == 'o' or gameBoard[tgt] == 'x'):
        inputBoard(playerType)

    # 3.gameBoardに反映
    else:
        gameBoard[tgt] = playerType

# ゲームの進行
displayBoard()
inputBoard('o') # ユーザーのターン
displayBoard()
inputBoard('x') # CPUのターン
displayBoard()
# ゲームの進行
displayBoard()
inputBoard('o') # ユーザーのターン
displayBoard()
inputBoard('x') # CPUのターン
displayBoard()
# ゲームの進行
while(True):
    displayBoard()
    inputBoard('o') # ユーザーのターン
    displayBoard()
    inputBoard('x') # CPUのターン
# ゲームの進行
while(True):
    displayBoard()
    inputBoard('o') # ユーザーのターン
    displayBoard()
    inputBoard('x') # CPUのターン

#  勝利判定
def winner():
    # 勝ち手を列挙
    lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ]
    # forで勝ち手を1パターンずつ見ていく
    for i in range(0, len(lines)):
        [a, b, c] = lines[i]
        # 勝ち手の場所に同じ記号が入っていないかを確認
        if gameBoard[a] and gameBoard[a] == gameBoard[b] and gameBoard[a] == gameBoard[c]: 
            # 同じ記号が入っていたら、入っている記号を返す
            return gameBoard[a]
    # どちらも勝っていない場合はNoneを返す
    return None
[a, b, c] = lines[i]
a = lines[i][0]
b = lines[i][1]
c = lines[i][2]
displayBoard() # 実行時に初めに表示される盤面

for turn in range(0,9):
    # 誰のターンかを判定する
    if(turn %2 == 0) : # あなたのターン
        print("You")
        inputBoard("o")
    else: # CPUのターン
        print("CPU")
        inputBoard("x")

    displayBoard() # 盤面表示

    if winner(): # 勝敗判定
        print(winner() + "の勝ち")
        break

    if turn == 8: # 8手目で引き分け
        print("引き分け")
        break
import random

gameBoard = [0,1,2,3,4,5,6,7,8] # ゲームに利用する盤面

# 盤面を3x3で表示する
def displayBoard():
    # gameBoardの要素を1つずつ表示
    print("--+---+--") # デコレーション
    for i in range(0, len(gameBoard)):
        if(i%3 == 2): # 3回に1回は改行
            print(gameBoard[i]) # 改行する
            print("--+---+--") # デコレーション

        elif(i%3 == 1):
            print(" | " + str(gameBoard[i]) + " | ", end="") # 改行しない
        else :
            print(gameBoard[i], end="") # 改行しない

    print()

# ターンを進める
def inputBoard(playerType):
    # 1.座標を入力させる
    if(playerType == "o"):  # o が渡されたら座標を入力
        tgt = int(input("0~8の座標を入れてください: "))
    else: # xが渡されたらランダムで座標を入力
        tgt = random.randint(0,8)

    # 2.入力座標に 'o'か 'x' が入っていないことを確認
    if(gameBoard[tgt] == 'o' or gameBoard[tgt] == 'x'):
        inputBoard(playerType)

    # 3.gameBoardに反映
    else:
        gameBoard[tgt] = playerType

# 勝利判定
def winner():
    # 勝ち手を列挙
    lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ]
    # forで勝ち手を1パターンずつ見ていく
    for i in range(0, len(lines)):
        [a, b, c] = lines[i]
        # 勝ち手の場所に同じ記号が入っていないかを確認
        if gameBoard[a] and gameBoard[a] == gameBoard[b] and gameBoard[a] == gameBoard[c]: 
            # 同じ記号が入っていたら、入っている記号を返す
            return gameBoard[a]
    # どちらも勝っていない場合はNoneを返す
    return None

displayBoard() # 実行時に初めに表示される盤面
# ゲームを実行する
for turn in range(0,9):
    # 誰のターンかを判定する
    if(turn %2 == 0) : # あなたのターン
        print("You")
        inputBoard("o")
    else: # CPUのターン
        print("CPU")
        inputBoard("x")

    displayBoard() # 盤面表示

    if winner(): # 勝敗判定
        print(winner() + "の勝ち")
        break

    if turn == 8: # 8手目で引き分け
        print("引き分け")
        break
import random

gameBoard = [0,1,2,3,4,5,6,7,8] # ゲームに利用する盤面

# 盤面を3x3で表示する
def displayBoard():
    # gameBoardの要素を1つずつ表示
    print("--+---+--") # デコレーション
    for i in range(0, len(gameBoard)):
        if(i%3 == 2): # 3回に1回は改行
            print(gameBoard[i]) # 改行する
            print("--+---+--") # デコレーション

        elif(i%3 == 1):
            print(" | " + str(gameBoard[i]) + " | ", end="") # 改行しない
        else :
            print(gameBoard[i], end="") # 改行しない

    print()

# ターンを進める
def inputBoard(playerType):
    # 1.座標を入力させる
    if(playerType == "o"):  # o が渡されたら座標を入力
        tgt = int(input("0~8の座標を入れてください: "))
    else: # xが渡されたらランダムで座標を入力
        tgt = random.randint(0,8)

    # 2.入力座標に 'o'か 'x' が入っていないことを確認
    if(gameBoard[tgt] == 'o' or gameBoard[tgt] == 'x'):
        inputBoard(playerType)

    # 3.gameBoardに反映
    else:
        gameBoard[tgt] = playerType

# 勝利判定
def winner():
    # 勝ち手を列挙
    lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ]
    # forで勝ち手を1パターンずつ見ていく
    for i in range(0, len(lines)):
        [a, b, c] = lines[i]
        # 勝ち手の場所に同じ記号が入っていないかを確認
        if gameBoard[a] and gameBoard[a] == gameBoard[b] and gameBoard[a] == gameBoard[c]: 
            # 同じ記号が入っていたら、入っている記号を返す
            return gameBoard[a]
    # どちらも勝っていない場合はNoneを返す
    return None

displayBoard() # 実行時に初めに表示される盤面
# ゲームを実行する
for turn in range(0,9):
    # 誰のターンかを判定する
    if(turn %2 == 0) : # あなたのターン
        print("You")
        inputBoard("o")
    else: # CPUのターン
        print("CPU")
        inputBoard("x")

    displayBoard() # 盤面表示

    if winner(): # 勝敗判定
        print(winner() + "の勝ち")
        break

    if turn == 8: # 8手目で引き分け
        print("引き分け")
        break
