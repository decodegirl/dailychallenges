# count how many of each “category” of each image there are

counter_dict ={}
with open("/Users/celinesurai/Desktop/practice.txt","r") as open_file:
    line = open_file.readline()
    while line:
        print(line)
        line = line[3:-26]
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = open_file.readline()

print(counter_dict)


# Given a .txt file that has a list of a bunch of names,
# count how many of each name there are in the file, and print out the results to the screen.
dict_counter= {}
with open('/Users/celinesurai/Desktop/nameslist.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in dict_counter:
            dict_counter[line] += 1
        else:
            dict_counter[line] = 1
        line = f.readline()

print(dict_counter)
