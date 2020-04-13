def test_yield():
    for x in range(3):
        print('before yield')
        yield x
        print('after yield')

for val in test_yield():
    print(val)
    if val == 2:
        break


if not 0:
    print('hi not 0')

import collections
ans = collections.defaultdict(list)
print(ans)