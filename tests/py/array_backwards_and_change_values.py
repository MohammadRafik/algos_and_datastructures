ary = [1,2,3,4,5,6,7,None]

for j in range(len(ary)-1,-1,-1):
    if j == 4:
        ary[j] = 'changed'
    print(ary[j])
    print(j)