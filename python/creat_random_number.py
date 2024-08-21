import random
guess_atempt=8
r=random.randint(0,100)
# print(r)
while(0<guess_atempt+1):
    num=int(input("Guess The Number :"))
    print("remening attempt",guess_atempt)
    if(num>r):
        print("plz  Enter Lower Number :")
    elif(num<r):
        print("Plz Enter Higher Number :")
    else:
        print("Congract..! \n You won Match")
        break
    if(guess_atempt<1):
        print("Ohh..You Defeat The Match \n you cross the max attempt..")
            # break

    guess_atempt=guess_atempt-1
