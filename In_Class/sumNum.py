# A program that computes the sum of the numbers in a file
# The numbers need to be stored in each line of the file

# Opening file for reading

inf = open("sum.txt", "r")

total = 0
line = inf.readline()

while line != "":
    line = line.rstrip()
    print("About to add", line, " to the total...")
    total = total + float(line)
    # Read the next line
    line = inf.readline()

print("the sum of the numbers is: ", total)
