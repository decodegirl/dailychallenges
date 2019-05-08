import random
number=int(input("enter a number less than 99 :"))
first=0
last=99
flag=0
count=0
while flag==0:
    guess=random.randint(first,last)
    print(guess)
    count+=1
    if guess>number:
        print("too high")
        last=guess-1
    elif guess==number:
        print("you have guessed the correct number in "+str(count)+" turns.")
        break
    elif guess<number:
        print("too low")
        first=guess+
