#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import random 

board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
currentplayer = "X"
winner = None
gamerunning = True





# In[2]:


# Printing the gameboard

def printBoard(board):
    print(" | " + board[0] + " | ", board[1] + " | ", board[2] + " | ")
    print(" | " + board[3] + " | ", board[4] + " | ", board[5] + " | ")
    print(" | " + board[6] + " | ", board[7] + " | ", board[8] + " | ")

printBoard(board)


# In[3]:


# Accepting player input

def playerinput(board):
    inp = int(input("enter position number 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
        board[inp - 1] = currentplayer
    else:
        print("Oops spot already used, pick another one!")
        playerinput(board)


# In[4]:


# Check for win conditions

def checkhorizontal(board):
    global winner

    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[1]
        return True

    elif board[3] == board[4] == board[5] and board[4] != "_":
        winner = board[4]
        return True

    elif board[6] == board[7] == board[8] and board[7] != "_":
        winner = board[7]
        return True
    

    
    
def checkvertical(board):
    global winner

    if board[0] == board[3] == board[6] and board[3] != "_":
        winner = board[3]
        return True

    elif board[1] == board[4] == board[7] and board[4] != "_":
        winner = board[4]
        return True

    elif board[2] == board[5] == board[8] and board[5] != "_":
        winner = board[5]
        return True
    
    

def checkdiagonal(board):
    global winner

    if board[0] == board[4] == board[8] and board[4] != "_":
        winner = board[4]
        return True

    elif board[2] == board[4] == board[6] and board[4] != "_":
        winner = board[4]
        return True
    
    
    
    
    # Need to code tie condition
    
def checktie(board):
    global gamerunning
        
    if "_" not in board:
            
        printBoard(board)
        print("It's a tie!")
        gamerunning = False
            
    #else:
        #print("It's not a tie!")
                
    return
  
    
    # Need to code win condition
    
def checkwin():
    global gamerunning    
    if checkvertical(board) or checkdiagonal(board) or checkhorizontal(board):
            
        print("the winner is " + winner)
        gamerunning = False
        
    


# In[5]:


# Switch the players back and forth

def switchplayer():
    global currentplayer
    
    if currentplayer == "X":
        currentplayer = "O"
        
    else:
        currentplayer = "X"

# creating computer bot to make moves
def computer(board):
    global currentplayer
    global gamerunning
    
    if gamerunning == True:
        print("in computer function")
        while currentplayer == "O":
            print("in computer function after while")
            position = random.randint(0,8)
            print("in computer function after while and position")
            if board[position] == "_":
                board[position] = "O"
                break
            gamerunning = True

       
# Running the whole program
while gamerunning:
    
    
    playerinput(board)
    checkwin()
    checktie(board)
    printBoard(board)

    switchplayer()
    computer(board)
    printBoard(board)

    checkwin()     
    checktie(board)
    switchplayer()
    


# In[ ]:




