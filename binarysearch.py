# Write a function that takes an ordered list of numbers (a list where the elements are in order
# from smallest to largest) and another number. The function decides whether or not the given
# number is inside the list and returns (then prints) an appropriate boolean.


def ordered_list(list1,num):
    for list_number in list1:
        if list_number == num:
            return True

    return False


if __name__=="__main__":
    list3 = [3,5,6,9,11,23,25]
    print(ordered_list(list3,6))
    print(ordered_list(list3,28))


##3using binary search


def binary_search(n, my_list=[]):

    while True:

        middle_list = int(len(my_list) / 2)

        if n == my_list[middle_list]:
            return True
        elif n < my_list[middle_list]:
            my_list = my_list[:middle_list]
        elif n > my_list[middle_list]:
            my_list = my_list[middle_list:]
        if len(my_list) == 1:
            return False


l = [-5, 0, 1, 4, 6, 7, 10, 12]
print (binary_search(8, l))
