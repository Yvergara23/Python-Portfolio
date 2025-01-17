#Yareli
#January 7th
#Rock Paper Scissors

#Initialize
import random
wins = 0
losses = 0
tie = 0
#Functions


#Step 1:
def Intro():
    global choice
    global move
    print ("Welcome to Rock, Paper, Scissors")
    print ("What is your move?")
    print ("""
    """)
    choice = input("Rock, Paper, or Scissors?") #Choice is the players move
    choice = choice.lower()
    print ("Your move is " + str(choice))
#Step 2: Generate
def Move():
    global choice
    global move
    move = random.randint(1,3) #Move is the computer
    if move == 1:
        move = "rock"
        print ("The computer's move is rock!")
        print ("""
    """)
    if move == 2:
        move = "paper"
        print ("The computer's move is Paper!")
        print ("""
    """)
    if move == 3:
        move = "scissors"
        print ("The computer's move is Scissors!")
        print ("""
    """)

def t():
    global tie
    global wins
    global losses
    tie = tie + 1
    wins = wins + 0
    losses = losses + 0
    print ("Ties: " + str(tie))
    print ("Wins: " + str(wins))
    print ("Losses: " + str(losses))
def w():
    global tie
    global wins
    global losses
    tie = tie + 0
    wins = wins + 1
    losses = losses + 0
    print ("Ties: " + str(tie))
    print ("Wins: " + str(wins))
    print ("Losses: " + str(losses))
def l():
    global tie
    global wins
    global losses
    tie = tie + 0
    wins = wins + 0
    losses = losses + 1
    print ("Ties: " + str(tie))
    print ("Wins: " + str(wins))
    print ("Losses: " + str(losses))

#Step 3: Outcome
def Outcome():
    global tie
    global wins
    global losses
    global choice
    global move
    if choice == "rock" and move == "rock": #1st
        print ("It is a Tie")
        print ("""
    """)
        t()
    if choice == "rock" and move == "paper":
        print ("Computer wins!")
        print ("""
    """)
        l()
    if choice == "rock" and move == "scissors":
        print ("You win!")
        print ("""
    """)
        w()
    if choice == "paper" and move == "paper": #2nd
        print ("It is a Tie")
        print ("""
    """)
        t()
    if choice == "paper" and move == "rock":
        print ("You win!")
        print ("""
    """)
        w()
    if choice == "paper" and move == "scissors":
        print ("Computer wins!")
        print ("""
    """)
        l()
    if choice == "scissors" and move == "scissors": #3rd
        print ("It is a Tie")
        print ("""
    """)
        t()
    if choice == "scissors" and move == "rock":
        print ("Computer wins!")
        print ("""
    """)
        l()
    if choice == "scissors" and move == "paper":
        print ("You win!")
        print ("""
    """)
        w()
            

def Rock_Paper_Scissors():
    while True:
        Intro()
        Move()
        Outcome()
        playagain = input ("Do you want to keep playing? Yes or No")
        if playagain.lower() == "yes":
            print ("""
    """)
            print ("restarting...")
            print ("""
    """)
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print ("""
    """)
            print ("Thanks for playing")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
            

#Main
Rock_Paper_Scissors()


