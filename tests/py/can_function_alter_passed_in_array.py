ary  = [1,2,3,4,5,6,'seven',8,'nine']

ary2 = ary
ary2[0] = "altered from other object"

def alter_ary(ary):
    print('function start')
    ary[1] = 'altered from inside a function'
    print(ary)
    print('fucntion end')


print(ary)
print(ary2)
alter_ary(ary2)
print(ary2)
print(ary)