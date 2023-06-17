# compute n-factorial for some n-values entered by the user

# read n from user and ensure it is non-negative

n = int(input("Enter the number "))

while n < 0:
    print("This was not a valid input. Try again... ")
    n = int(input("Enter the number "))

original_n = n
result = 1

for n in range(1, n+1):
    result = result * n

print(original_n, "factorial is", result)
