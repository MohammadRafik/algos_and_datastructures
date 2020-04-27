def power(x,y):
    if y == 0:
        return 0
    if y == 1:
        return x
    else:
        return x * power(x,y-1)

for i in range(0,40):
    print(power(2, i))