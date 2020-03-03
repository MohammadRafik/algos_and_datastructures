

def insert_sort(arry):
    i = 0
    while( i < len(arry)):
        j = i
        while(0 < j):
            if arry[j] < arry[j-1]:
                tmp = arry[j]
                arry[j] = arry[j-1]
                arry[j-1] = tmp
            else:
                break
            j -= 1
        i += 1
    return arry
        


from test_cases import array1

print(insert_sort(array1))