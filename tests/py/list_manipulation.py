count = [0] * 26
strobe = [1,2,3,4,5] * 3

tuple_count = tuple((1,2,3)) * 3

# tuple_times_list = tuple(2) * count


print(count)

print(strobe[11])

print(tuple_count)

dict = { 1 : 'one', 2 : 'two', 'list': [1,2] }  
tuple3 = tuple(dict) 
print(tuple3) 
dict['list'].append('appending to dict at 1')
print(dict)
print(dict['list'])
# list_of_tuples = [(1,2), (3,4),(1,2)] 
# dict2 = {}

# for t in list_of_tuples:
#     dict2(t).append(t)
# print(dict2)
list = 520
print(list)