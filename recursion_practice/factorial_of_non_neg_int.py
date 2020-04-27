
def fac(num):
    if num != 0:
        return num * fac(num-1)
    else:
        return 1

for i in range(0,20):
    print(fac(i))
