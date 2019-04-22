# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list
#  of only the first and last elements of the given list. For practice, write this code inside a function.


def list_end(num):
    return [num[0],num[-1]]


a = [5,10,16,20]
print(list_end(a))
