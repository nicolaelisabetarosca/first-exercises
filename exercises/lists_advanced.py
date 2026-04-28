import statistics

numbers = [-5, 10, -2, 7, 0, 3, -8, 12]

largest = max(numbers)
print(largest)

smallest = min(numbers)
print(smallest)

sum = sum(numbers)
print(sum)

avg1 = statistics.mean(numbers)
print(avg1)

new_list = []

for number in numbers: 
    if number % 2 == 0:
        new_list.append(number)

print(new_list)
    
    # -------

above_average = 0 

for number in numbers: 
    if number > avg1: 
        above_average = above_average + 1

print("This is the amount of numbers in the list that are ABOVE THE AVERAGE:", above_average)