name = "nicolarosca"
print(name)

print(len(name))

print(name.upper)
print(name.lower)

count_letters = name.count("r")
print(count_letters)

# method one of finding a substring in a string 
x = "zz"

if x in name: 
    print("substring found ")
else: 
    print("not found")

# method two of finding a substring in a string 
found_substring = True

if x in name: 
    found_substring = True
    
else: 
    found_substring = False

print(found_substring)