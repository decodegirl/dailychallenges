my_set = {1,7,8,9,4,3,2,1,6,6,3,}
set(my_set)
print(list(my_set))

# In Python, you make and use a set with the set() keyword. For example:
names = set()
names.add("Michele")
names.add("Robin")
names.add("Michele")
print(names)


# Write a program (function!) that takes a list and returns a new list
#  that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.


def rem_dup(lst):
    new = []
    for y in lst:
        if y not in new:
            new.append(y)
    return new


print(rem_dup([4,5,9,9,2,3,]))

# this one uses sets


def dedupe_v2(x):
    return list(set(x))

print(dedupe_v2([1,3,3,5,7,7,9,4]))
