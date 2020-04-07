def func(XD, *args,**kwargs):
    for i in args:
        print(i)

def func2(*args,**kwargs):
    for k, v in kwargs.items():
        print(k + ': '+v)


func('xd','123','ayyy','wahoo')
print()
func2(first ='Geeks', mid ='for', last='Geeks')