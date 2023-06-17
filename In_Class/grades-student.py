
num_students = int(input("Enter number of students "))

num_test_scores = int(input("Enter test scores per student "))

for student in range(num_students):
    total = 0.0
    print("Student Number", student + 1)

    for test_num in range(num_test_scores):
        print("Test number", test_num + 1, end="")
        score = float(input(": "))
        total = total + score
    average = total / num_test_scores
    print("the average scores for student number", student + 1, "is", average)
    print()
