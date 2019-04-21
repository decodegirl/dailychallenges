# character input.
# user input in python.

# Create a program that asks the user to enter their name and their age.
#  Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Give me your name:")
print("Your name is " + name)

age = int(input("Enter your age: "))

year = 100 - age

print(name + " ,You will turn 100 years old in  the year" + str(2018 + year))


# challenge 2
#  Ask the user for a number.
#  Depending on whether the number is even or odd,
#  print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = int(input("Give me a number: "))
if num % 4 == 0:
    print("You gave me a number which is even and divisible by 4!")
elif num % 2 == 0:
    print("Number is even")
else:
    print("number is odd")

num1 = int(input("Enter a number :"))
check = int(input("Enter another number:"))

if num1 % check == 0 :
    print(" Your numbers divide evenly")
else:
    print(" Your numbers do not divide evenly.")


# write a program that prints out all the elements of the list that are less than 5.
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []
for item in a:
    if item < 5:
        new.append(item)
print(new)
newnumber = int(input("Enter a number: "))
newlist = []
for item in a:
    if item < newnumber:
        newlist.append(item)
print(newlist)

