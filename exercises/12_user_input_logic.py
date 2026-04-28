uinput = int(input("Feed me a number: "))

# checking to see if input is positive, negative or 0
if uinput > 0: 
    print(uinput, "is positive")
if uinput < 0: 
    print(uinput, "is negative")
if uinput == 0: 
    print(uinput, "is equal to 0")

# checking to see if input is odd or even
uinput2 = int(input("Feed me another number: " ))

if uinput2 % 2 == 0: 
    print(uinput2, "is an even number")
else:
    print(uinput2, "is an odd number")


# checking to see which input is bigger 
if uinput>uinput2: 
    print(uinput, "is bigger")
else:
    print(uinput2, "is bigger")