with open("numbers.txt", "w") as file:
    file.write("10, 5, 8, 20, 3")

file = open("numbers.txt")

# Read all numbers from the file

print(file.read())

# Convert them into integers

with open('numbers.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list_file_w_strings = line.strip().split(',')

print(list_file_w_strings)

print(type(list_file_w_strings[0]))

# Store them in a list

intlist = []

for x in list_file_w_strings: 
    if isinstance(x,str): 
        x = int(x)
        intlist.append(x)

print(intlist)

print(type(intlist[4]))

# Calculate:
# total sum
# average
# largest number
# smallest number

import statistics

for number in intlist: 
    sum_all = sum(intlist)
    avg_all = statistics.mean(intlist)
    max_all = max(intlist)
    min_all = min(intlist)
    

print("the sum of all numbers is:", sum_all)
print("the average of all numbers is:", avg_all)
print("the maximum numbers of all is:", max_all)
print("the minimum of all the numbers is:", min_all)