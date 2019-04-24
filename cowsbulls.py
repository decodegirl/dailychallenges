# Cow & Bulls Game - a game where a 4 digit number will be generated automatically and user have to guess that number.
# For every perfectly guessed digit at perfect place user get a cow
# For every perfectly guessed digit at wrong place user get a Bull {Bull = Total matching digit - cows}
# game continues until player guess the number exactly {4 cows} At the end the code will show how many guess count.


import random


def cowBull_loop():
    ask= str(input("enter a four digit number: "))
    cow = 0
    bullCow=0  # total number of digit guessed perfectly. right place + wrong place
    for i in range(0,4):
        if num[i] == ask[i]:
            cow += 1
    for i in num:
        if i in ask:
            bullCow += 1
    bull=bullCow-cow
    print("you have {} cows and {} bulls".format(cow,bull))
    return cow


if __name__ == '__main__':
    num = str(random.randrange(1000,9999))
    print(num) # prints out the randomly generated 4 digit.
    cow= 0
    count=0
    while cow != 4:
        count += 1
        cow = cowBull_loop()
