# Compute the number of lines, words and characters in a file
# Save the results in a new file

inf = open("input_file.txt", "r")
outf = open("output_file.txt", "w")

lines = 0
words = 0
chars = 0

line = inf.readline()

while line != "":
    lines = lines + 1
    words = words + len(line.split())
    chars = chars + len(line)

    line = inf.readline()

outf.write("Lines: " + str(lines) + "\n")
outf.write("Words: " + str(words) + "\n")
outf.write("Characters: " + str(chars) + "\n")

inf.close()
outf.close()

