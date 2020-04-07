ary = []

ary.append('one')
ary.append('two')
ary.append('three')
ary.append('four')
ary.append('five')

i = 0
while i < len(ary):
    if i == 1:
        x = ary.pop(i)

    print(ary[i])
    i += 1
print(x)