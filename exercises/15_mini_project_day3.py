# Given a list of numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers)

# Create a new list with only even numbers
# Create a new list with only odd numbers
even = []
odd = []

for number in numbers: 
    if number % 2 == 0: 
        even.append(number)
    else:
        odd.append(number)

print("even list:", even)
print("odd list:", odd)

# Create a list of squared values

squared = []

for number in numbers: 
    squared.append(number*number)

print("the squared list:", squared)

# Find the largest squared value
print("the biggest squared value:", max(squared))

# Count how many squared values are above 50

for number in squared:
    x = squared.count(number > 50)

print("the no of squared values above 50 is", x)

# Check if a specific number exists in the original list

y = 4
exists = True

if y in numbers: 
    print(exists)

# Count how many times it appears

for number in numbers: 
    if y in numbers: 
        abc = numbers.count(4)

print(abc)