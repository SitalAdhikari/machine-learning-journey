#Guess the perfect number between 1 and 1000 --PYTHON

import random
num= random.randint(1,100)
user=int(input("Enter any number:"))


#game
s=1
i=0
while (s!=0):
    i+=1
    if (user == num):
        print(f"Congrations! You guessed right. \n In itiration:{i} ")
        s =  0
    elif( user < num):
        user=int(input("Enter higher number:"))
    else:
        user=int(input("Enter lower number:"))

with open("hello.txt", "w+") as f:
    highscore=f.read()
    if (highscore ==""):
        highscore=9999999
    else:
        highscore = int(highscore)

if (i< highscore):
    with open("hello.txt", "w") as f:
        f.write(str(i))
        print(f" \n \t Congratulation!! New record, Guess in {i}")