
n = int(input("Enter a non-negative integer: "))

power = 1
i = 0

while i <= n:
    print(str(i) + " " + str(power))
    power = 2 * power
    i += 1
