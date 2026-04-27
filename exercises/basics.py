age = 28


if age >= 18:
    print("adult")
else:
    print("minor")


temperature = 10 

if temperature > 20: 
    print("warm")
else: 
    print("cold")


x = [1, 2, 3, 4, 5]
print (x)

print(sum(x))

# how do you print even numbers?
print ([n for n in x if n % 2 == 0])

# Print numbers backwards from 5 to 1

print (x[::-1])

name = input("What is your name? ")

def takes_name(name): 
    print("Hello", name)

takes_name(name)

list_numbers = [13 , 42, 7, 19, 3]

print(list_numbers)

print(list_numbers[0])

for number in list_numbers:
    print(number)

list_numbers.append(99)

print(list_numbers)
