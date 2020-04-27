list_of_nums = [1,2,4,5,6]



def recursion_popper(ary):
    if ary:
        return ary.pop() + recursion_popper(ary)
    else:
        return 0



print(recursion_popper(list_of_nums))