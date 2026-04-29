# Create a list of numbers converted to strings


# Given a list of numbers:
# Create a new list where each number is doubled
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

numbers_doubled = []

for number in numbers:
    numbers_doubled.append(number*2)

print("numbers_doubled:", numbers_doubled)

# Create a new list where each number is squared

squared = []

for number in numbers: 
    squared.append(number*number)

print("squared:", squared)


# Create a list of only negative numbers

numbers2 = [1, 2, -3, 4, -5, 6, -7, -8, 9, 10, 11, 12]


negative_numbers = []
for number in numbers2: 
    if number < 0: 
        negative_numbers.append(number)

print("negative_numbers:", negative_numbers)


# Create a list where:
# even numbers stay the same
# odd numbers become 0

nos = [12, 13, 14, 15, 16, 17, 18, 19, 20]
nos_new = []

for number in nos: 
    if number % 2 == 0:
        nos_new.append(number)
    else:
        nos_new.append(0)

print(nos_new)