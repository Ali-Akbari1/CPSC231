# consider we have defined two lists stuNames stuGrades
# stuNames has list of 4 names
# stuGrades list is a two-dimensional list having grades of three quizzes

stuNames = ["Alice", "Bob", "Carol", "Dave"]
stuGrades = [[91, 92, 93], [80, 81, 82], [70, 75, 89], [56, 76, 89]]

# compute each student average

total = []
average = []

for i in range(len(stuGrades)):
    total += [sum(stuGrades[i])]

for i in range(len(stuGrades)):
    average += [total[i]/3]

for i in range(len(stuNames)):
    print(stuNames[i]+ " average is", average[i])

maxAverage = max(average)


for i in range(len(average)):
    if average[i] == maxAverage:
        print("\n" + stuNames[i] + " has the maximum average")



