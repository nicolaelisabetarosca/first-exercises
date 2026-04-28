numbers = [4, 7, 2, 9, 7, 5, 1, 7, 3, 8, 4, 4, 4]

search = 8

if search in numbers: 
    print(search, "is in the list")

how_many_times = numbers.count(search)
print(how_many_times, "is the amount of times", search, "is in the list")


index_search = numbers.index(4)
print(index_search, "is the index of the number 4")

# find the indeces for all the number 4 

index_listing = []

for number in range(len(numbers)): 
    if numbers[number] == 4: 
        index_listing.append(number)

print(index_listing, "- indeces for the number 4")


