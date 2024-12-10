# reading full file and setting it into variable for operations
f = open("C:\\school\\adventofcode2024\\Day-01\\day01-data.txt")
data = f.readlines()

# creating list for each column of numbers
left = list()
right = list()

# for each line of numbers (left column and right column) put the left in left list and make it an int, do the same for the right column
for line in data:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))





