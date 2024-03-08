# Importing Libraries

from tkinter import *
from random import randint

# Frame, Background, Title of GUI
root = Tk()
root.title("Rock Paper Scissor Game")
root.config(bg="#9b59b6")  # Moderate violet
root.geometry("1300x500")

# Image
rock_user = PhotoImage(file='Rock2.png')
paper_user = PhotoImage(file='Paper2.png')
scissor_user = PhotoImage(file='Scissor2.png')
rock_comp = PhotoImage(file='Rock.png')
paper_comp = PhotoImage(file='Paper.png')
scissor_comp = PhotoImage(file='Scissor.png')

# Inserting Image
user_label = Label(root, image=scissor_user, bg="#9b59b6")
comp_label = Label(root, image=scissor_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Score
playerScore = Label(root, text=0, font=40, bg="#9b59b6", fg="black")
computerScore = Label(root, text=0, font=40, bg="#9b59b6", fg="black")
playerScore.grid(row=1, column=3)
computerScore.grid(row=1, column=1)

# Indicator
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Message
msg = Label(root, font=50, bg="#9b59b6", fg="black", 
            text="\U0001F604 Lets Start the Game \U0001F604", width=35)
msg.grid(row=3, column=2)

# Update message
def updateMessage(x):
    msg['text'] = x

# Update user score
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore["text"] = str(score)

def updateUserScore2(h):
    playerScore['text'] = h

# Update computer score
def updateComputerScore():
    score = int(computerScore['text'])
    score += 1
    computerScore["text"] = str(score)

def updateComputerScore2(m):
    computerScore['text'] = m

# Update User_indicator
def updateUser_Indicator1():
    user_indicator.config(bg="Green")

def updateUser_Indicator2():
    user_indicator.config(bg="Red")

def updateUser_Indicator3():
    user_indicator.config(bg="#9b59b6")

# Update Comp_indicator
def updateComp_Indicator1():
    comp_indicator.config(bg="Green")

def updateComp_Indicator2():
    comp_indicator.config(bg="Red")

def updateComp_Indicator3():
    comp_indicator.config(bg="#9b59b6")

# Check winner
def checkWinner(player,computer):
    if player == computer:
        updateMessage("\U0001F61B Both are Same and Its a tie!!! \U0001F61B")
        updateUser_Indicator3()
        updateComp_Indicator3()
        root.config(bg="#9b59b6")
    elif player == "rock":
        if computer == "paper":
            updateMessage("\U0001F622 Paper Wraps Rock and You loose \U0001F622")
            updateComputerScore()
            updateComp_Indicator1()
            updateUser_Indicator2()
        else:
            updateMessage("\U0001F60E Rock smash Scissor and You Win \U0001F60E")
            updateUserScore()
            updateUser_Indicator1()
            updateComp_Indicator2()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("\U0001F622 Scissor cuts Paper and You loose \U0001F622")
            updateComputerScore()
            updateComp_Indicator1()
            updateUser_Indicator2()
        else:
            updateMessage("\U0001F60E Paper Wraps Rock and You Win \U0001F60E")
            updateUserScore()
            updateUser_Indicator1()
            updateComp_Indicator2()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("\U0001F622 Rock smash Scissor and You loose \U0001F622")
            updateComputerScore()
            updateComp_Indicator1()
            updateUser_Indicator2()
        else:
            updateMessage("\U0001F60E Scissor cuts Paper and You Win \U0001F60E")
            updateUserScore()
            updateUser_Indicator1()
            updateComp_Indicator2()

    else:
        pass

# Update choices
choice = ("rock","paper","scissor")
def updateChoice(x):
# For computer
     compChoice = choice[randint(0,2)]
     if compChoice == "rock":
         comp_label.configure(image=rock_comp)
     elif compChoice == "paper":
         comp_label.configure(image=paper_comp)
     else:
         comp_label.configure(image=scissor_comp)

# For user
     if x == "rock":
         user_label.configure(image=rock_user)
     elif x == "paper":
         user_label.configure(image=paper_user)
     else:
         user_label.configure(image=scissor_user)

     checkWinner(x,compChoice)

# Reset the Game
def resetGame():
    user_indicator.config(bg='#9b59b6')
    comp_indicator.config(bg='#9b59b6')
    updateMessage("\U0001F604 Lets Start the New Game \U0001F604")
    updateUserScore2(0)
    root.config(bg="#9b59b6")
    updateComputerScore2(0)
    comp_label.configure(image=scissor_comp)
    user_label.configure(image=scissor_user)

# Button
rock = Button(root, width=20, height=2, text="ROCK",   # light red
                bg="#FF3E4D", fg="white", command= lambda:updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",  # bright yellow
                bg="#FAD02E", fg="white", command= lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",  # vivid cyan(greenish-blue)
                bg="#0ABDE3", fg="white", command= lambda:updateChoice("scissor")).grid(row=2, column=3)

# Reset Button
reset = Button(root, width=20, height=2, text="RESET GAME",
                bg="violet", fg="white", command = resetGame).grid(row=4, column=4)


root.mainloop()