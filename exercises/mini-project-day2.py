import statistics

numbers = [-5, 10, -2, 7, 0, 3, -8, 12, 12, 12]
even = 0 
odd = 0


for number in numbers:
    sum1 = sum(numbers)
    count = len(numbers)

    if number % 2 == 0: 
        even = even + 1
    else: 
        odd = odd + 1

    max1 = max(numbers)
    min1= min(numbers)

print("this is the sum of all the numbers: ", sum1)
print("this is the amount of numbers in the list: ", count)
print("this is the number of even numbers: ", even)
print("this is the number of odd numbers:", odd)
print("this is the largest number:", max1)
print("this is the smallest number", min1)

avg1 = statistics.mean(numbers)
print("this is the average of the numbers", avg1)

above_avg = 0

for number in numbers: 
    if number > avg1:
        above_avg = above_avg + 1

print("this is the sum of numbers above average", above_avg)


# count how many times a specific number appears 

appearance = numbers.count(12)
print("number 12 appears in the list: ", appearance, "times")

# does number 12 appear in the list? 

appearance = False 

for number in numbers: 
    if number == 1: 
        appearance = True

print(appearance)





