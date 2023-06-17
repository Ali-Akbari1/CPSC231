#Gold is solid when the temperature is below 1064.Assignment3
#Gold is liquid when the temperature is between 106.43 and 287.00
#Otherwise Gold is gaseous

temp = int(input("What is the temperature of the gold "))

if (temp < 1064.43):
    print("Gold is solid")
elif (temp > 1064.43 and temp < 2807.00):
    print("Gold is liquid")
else:
    print("Gold is gaseous")