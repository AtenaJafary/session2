print("pleasse enter number or enter <exist>")
sum=0
n=0
while True :
    a=int(input("number or <0> for exit: "))

    if a==0 :
        print("the sum ofnumbers: ", sum)
        break
    n=float(a)
    sum=sum+n