
def h_s(cap, num = 1):
    if num == cap:
        return 1/num
    else:
        return 1/num + h_s(cap, num+1)

list_of_solutions = []
y = []
for i in range(10,1000,10):
    list_of_solutions.append(h_s(i))

difference = []
for i in range(len(list_of_solutions)-1):
    difference.append(list_of_solutions[i+1]-list_of_solutions[i])
    y.append(i*10)

import matplotlib.pyplot as plt
plt.plot(difference, y)
plt.show()