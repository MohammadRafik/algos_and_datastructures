
def i_t_s(intgr):
    if intgr == 0:
        return ''
    else:
        return i_t_s(int(intgr/10)) + str(intgr%10)


print(i_t_s(1234505))

