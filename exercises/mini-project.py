list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]

print(list_numbers)

print(list_numbers[0])

for numbers in list_numbers:
    print("This is the next number: ", numbers)

list_numbers.append(16)
print (list_numbers)

# from collections import Counter

# counter_no = Counter[0]

even_count = 0
uneven_count = 0 

for x in list_numbers: 
    if x % 2 == 0: 
        even_count = even_count + 1      
    else: 
        uneven_count = uneven_count + 1
        
print("the count of even numbers is", even_count)
print("the count of uneven numbers is", uneven_count)


# find largest number 

smallest_number = list_numbers[0]
print("smallest number is", smallest_number)

largest_number = 0


for x in list_numbers: 
    if x > smallest_number: 
        largest_number = x
    else: 
        continue;


print("the largest number is", largest_number)