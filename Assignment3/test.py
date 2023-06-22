a = not (5 % 2 == 0)
b = 'a' in 'bamboo'
print(a)
print(b)
if a and b:
    print('x')
if a or b:
    print('y')
else:
    print('z')