# Python program for Rock, Paper, Scissor Game

# 1= Rock 
# 2= Paper
# 3= Scissor

import random
bot = random.choice([1,2,3])
print ("\n Type: \n \t R for Rock, \n \t P for Paper, \n \t S for Scissor \n")

user = input("Enter R, P or S:")
iuser = user.upper()

dict = { "R":1,"P":2,"S":3}
revdict = { 1: "Rock", 2: "Paper", 3: "Scissor"}
print(f" You: {revdict[dict[iuser]]} \n Computer: {revdict[bot]}")

if (bot== dict[iuser]):
    print("\n \t !Draw! \n")
elif (bot == 1 and dict[iuser]==2):
    print("\n \t Congratulations! You Win.\n")
elif (bot == 1 and dict[iuser]==3):
    print("\n \t You lose.  \n")
elif (bot == 2 and dict[iuser]==1):
    print("\n \t Congratulations! You Win.\n")
elif (bot == 2 and dict[iuser]==3):
    print("\n \t You lose.\n")
elif (bot == 3 and dict[iuser]==1):
    print("\n \t Congratulations! You Win.\n")
elif (bot == 3 and dict[iuser]==2):
    print("\n \t You lose.\n")
else:
    print(" \n Input Invalid. We accept only R,P and S. \n ")