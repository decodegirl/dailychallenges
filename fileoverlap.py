# Given two .txt files that have lists of numbers in them,
# find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000,
# and the other .txt file has a list of happy numbers up to 1000.

def file_overlap(filename):
    list_to_print = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_print.append(int(line))
            line = f.readline()

    return list_to_print


prime_list = file_overlap("/Users/celinesurai/Desktop/primenumbers.txt")
happy_numbers_list = file_overlap("/Users/celinesurai/Desktop/happynumbers.txt")


overlaplist = []

for element in prime_list:
    if element in happy_numbers_list:
        overlaplist.append(element)

print(overlaplist)
