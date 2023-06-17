

# FOR ASSINGMENT

names = []
name = input("Enter a name:")
names.append(name)
names_str = input("Enter names separated by comma:")
names.extend(names_str.strip().split(","))
print(names)

