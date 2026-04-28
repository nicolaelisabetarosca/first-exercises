name = input("What is your name? ")
age = int(input("What is your age? "))

if age >= 18: 
    print("Hello", name, ", you are an adult")
else: 
    print("Hello", name, ", you are still underage")

# ---------------------

numbers = [23, 24, 56, 66, 99, 100, 9, 10]

for number in numbers:
    print(number)

for number in numbers: 
    if number % 2 == 0: 
        print(number, "is even")


# -----------------------

even_numbers = 0
odd_numbers = 0


for number in numbers: 
    if number % 2 == 0:
        even_numbers = even_numbers + 1
    else:
            odd_numbers = odd_numbers + 1
             
        
print("This is the sum of the even numbers in the list:", even_numbers)
print("This is the sum of the odd numbers in the list:", odd_numbers)


# ----------------

bigger = 0
smaller = 0
equal = 0

for number in numbers: 
     if number > 10:
          bigger = bigger + 1
     if number < 10: 
          smaller = smaller + 1
     if number == 10: 
          equal = equal + 1

print("sum of the smaller numbers than 10 is", smaller)
print("sum of the bigger numers than 10 is", bigger)
print("this is the number of numbers equal to 10: ", equal)



          