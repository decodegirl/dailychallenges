# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

type1 = str(input("Enter a string:"))

if type1 == type1[::-1]:
    print(" This string is a palindrome!")
else:
    print("This is not a palindrome")

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#  Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new = []
for item in a:
    if item % 2 == 0:
        new.append(item)
print(new)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([items for items in a if items % 2 == 0])

