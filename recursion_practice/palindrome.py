def palin(string, i = 0):
    if i < len(string)//2:
        if string[i] == string[-i-1]:
            return palin(string, i+1)
        else:
            return False
    else:
        return True

print(palin('8999'))