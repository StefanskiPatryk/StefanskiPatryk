import random

print("Welcome in tic-tac-toe")
print("######################")

possibleNumbers= [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def printGameBoard():
    for x in range (rows):
        print("\n+---+---+---+")
        print("|",end="")
        for y in range(cols):
            print("",gameBoard[x][y], end=" |")
    print("\n +---+---+---+")
    
def modifyArray(num, turn):
    num -= 1
    if(num ==0):
        gameBoard[0][0]=turn
    elif(num ==1):
        gameBoard[0][1]=turn
    elif(num ==2):
        gameBoard[0][2]=turn
    elif(num ==3):
        gameBoard[1][-0]=turn
    elif(num ==4):
        gameBoard[1][1]=turn    
    elif(num ==5):
        gameBoard[1][2]=turn
    elif(num ==6):
        gameBoard[2][0]=turn
    elif(num ==7):
        gameBoard[2][1]=turn
    elif(num ==8):
        gameBoard[2][2]=turn



def checkForWinner(gameBoard):
    #### X axis
    if(gameBoard[0][0] == 'X' and gameBoard [0][1] == 'X' and gameboard[0][2]=='X'):
        print("X has won ;DD")
        return "X" 
    elif(gameBoard[0][0] == '0' and gameBoard [0][1] == '0' and gameboard[0][2]=='0'):
        print("X has won!")
        return "0"
    elif(gameBoard[1][0] == 'X' and gameBoard [1][1] == 'X' and gameboard[1][2]=='X'):
        print("X has won!")
        return "X"
    elif(gameBoard[1][0] == '0' and gameBoard [1][1] == '0' and gameboard[1][2]=='0'):
        print("0 has won!")
        return "0"
    elif(gameBoard[2][0] == 'X' and gameBoard [2][1] == 'X' and gameboard[2][2]=='X'):
        print("X has won!")
        return "X"
    elif(gameBoard[2][0] == '0' and gameBoard [2][1] == '0' and gameboard[2][2]=='0'):
        print("0 has won!")
        return "0"
    
    #### Y axis
    elif(gameBoard[0][0]=="X" and gameBoard[1][0]=="X" and gameBoard[2][0] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0]=="0" and gameBoard[1][0]=="0" and gameBoard[2][0] == "0"):
        print("0 has won!")
        return "0"
    elif(gameBoard[0][1]=="X" and gameBoard[1][1]=="X" and gameBoard[2][1] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][1]=="0" and gameBoard[1][1]=="0" and gameBoard[2][1] == "0"):
        print("0 has won!")
        return "0"
    elif(gameBoard[0][2]=="X" and gameBoard[1][2]=="X" and gameBoard[2][2] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][2]=="0" and gameBoard[1][2]=="0" and gameBoard[2][2] == "0"):
        print("0 has won!")
        return "0"
    #### Cross wins ;P
    elif(gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == "0" and gameBoard[1][1] == "0" and gameBoard[2][2] == '0'):
        print("0 has won!")
        return "0"
        
leaveloop = False
turn = "X"
turnCounter = 0
while(leaveloop == False):
    if(turnCounter % 2 == 1):
        printGameBoard()
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if(numberPicked >= 1 or numberPicked <=9):
            modifyArray(numberPicked, 'X')
        else:
            print("Invalid input. Please try again.")
        turnCounter +=1
    else:
        while(True):
            cpuChoice = random.choice(possibleNumbers)
            print("\nCpu choice", cpuChoice)
            if(cpuChoice in possibleNumbers):
                modifyArray(cpuChoice, '0')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break
                


















