# sample() is an inbuilt function of random module in Python that returns a
# particular length list of items
# chosen from the sequence i.e. list, tuple, string or set.
# Used for random sampling without replacement.

# write a program that returns a list that contains
#  only the elements that are common between the lists
# randomly generate two lists to test this.

import random

a = random.sample(range(1,30),12)
b = random.sample(range(1,30),18)
print(a)
print(b)
result = [i for i in a if i in b]
print(result)

# another way of doing this is:


a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in set(a) if i in b]
print(result)
