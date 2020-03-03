
def selection_sort(arry):
    for i in range(len(arry)):
        lowest_val_index = i
        j = i + 1
        while( j < len(arry)):
            if arry[j] < arry[lowest_val_index]:
                lowest_val_index = j
            j += 1
        tmp = arry[i]
        arry[i] = arry[lowest_val_index]
        arry[lowest_val_index] = tmp
    return arry






from test_cases import array1
print(selection_sort(array1))