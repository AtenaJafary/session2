import random

n=int(input("please enter n: "))
number=[]
while True:
    b=random.randint(0,n)
    if b not in number :
        number.append(b)
    elif len(number)==n:
        print(number)
        break