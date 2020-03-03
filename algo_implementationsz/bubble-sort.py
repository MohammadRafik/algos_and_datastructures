
def bubble_sort(arry):
    for i in range(len(arry)):
        for j in range(len(arry)-1):
            if arry[j+1] < arry[j]:
                tmp = arry[j]
                arry[j] = arry[j+1]
                arry[j+1] = tmp
    return arry


from test_cases import array1
print(bubble_sort(array1))