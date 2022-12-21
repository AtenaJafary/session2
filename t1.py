import random

pc_number= random.randint(0,20)
guess=0
while True:
    user_number=int(input("please enter your number: "))
    if pc_number==user_number :
        print("YOU WIN")
        guess=guess+1
        print("your guess number: ", guess)
        break
    if pc_number>user_number:
        print("boro balatar")
        guess=guess+1
    elif pc_number<user_number:
        print("boro paeentar")
        guess=guess+1