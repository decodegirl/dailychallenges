# Write a program that asks the user how many Fibonnaci numbers
#  to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two numbers in the sequence.
#  The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def gen_fib():
    count = int(input(" How many numbers do you want to generate: "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]

    elif count > 2:
        fib = [1,1]
        while i < (count -1):
            fib.append((fib[i] + fib[i-1]))
            i += 1
    return fib


print(gen_fib())


# the following is an explanation of how this works
# Example:
# i = 1
# number entered by user = 10
# the current state of the fib list is [1,1] because the number entered is bigger than 2

# while i < (num - 1) defines that the while loop stops after the number entered by the user
#  is reached (the minus 1 makes sure it`s the exact number because indexes start at 0 instead of 1)

# fib.append(fib[i] + fib[i-1]) takes the current value of i as an index,
#  adds the number before that and appends the final value to the fib list.
# With the example I used the function would say:

# 1. iteration of the while loop: fib.append(fib[1] + fib[0])
# (fib[0] is the first value in the current list so it would be 1, fib[1]
#  is the second value in the list, which is also 1. the value that is appended would be 1+1=2)
# 2. fib.append(fib[2] + fib[1])
# (same goes here: fib[2] is the newly generated third value in the list which is 2, the second value is 1; 1+2 = 3)

# 3. fib.append(fib[3] + fib[2])
# (fib[3] = 3; fib[2]= 2 so the added value is 3+2 = 5)
# ...
# the i += 1 is the same as i = i+1. That just keeps the index moving forward.

