def test_yield():
    for x in range(3):
        print('before yield')
        yield x
        print('after yield')

for val in test_yield():
    print(val)
    if val == 2:
        break