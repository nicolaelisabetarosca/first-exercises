
# Create a text file manually (e.g. data.txt)
# Write at least 5 lines of text into it
# Open the file in Python
# Print all contents

with open("data.txt", "w") as file:
    file.write("Line\nLine nicola Rosca\nLine\nLine\nLine nicola\nLine\nLine Rosca\nLine\nLine NICOla")
    
file = open("data.txt")
print(file.read())


# Count how many lines are in the file

with open("data.txt", 'r') as fp:
    lines = sum(1 for line in fp)
    print('Total Number of lines:', lines)

# Print only lines that contain a specific word

word = "nicola"

with open("data.txt", "r") as file: 
    for line in file:
        if word.lower() in line.lower(): 
            print(line)