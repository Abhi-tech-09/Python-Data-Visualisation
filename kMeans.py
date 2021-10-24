from main import *
import random as rand
import matplotlib.pyplot as plt


def normalise(a, lend, rend):
    mx = max(a)
    mn = min(a)
    l = lend
    r = rend
    for i in range(0, len(a)):
        a[i] = (((a[i] - mn)*(r-l))//(mx - mn)) + l


def cal_dist(k, par):
    m1 = [0, 0]
    for x in k[0]:
        m1[0] += x[0]
        m1[1] += x[1]
    m1[0] = m1[0]//len(k[0])
    m1[1] = m1[1]//len(k[0])

    m2 = [0, 0]
    for x in k[1]:
        m2[0] += x[0]
        m2[1] += x[1]
    m2[0] = m2[0]//len(k[1])
    m2[1] = m2[1]//len(k[1])

    dist1 = abs(par[0]-m1[0])**2 + abs(par[1]-m1[1])**2
    dist2 = abs(par[0]-m2[0])**2 + abs(par[1]-m2[1])**2

    if dist1 >= dist2:
        return True
    else:
        return False


for i in range(len(amount)):
    amount[i] = int(amount[i])
for i in range(len(profit)):
    profit[i] = int(profit[i])

normalise(amount, 1, 50)
normalise(profit, -50, 50)


for i in range(0, len(profit)):
    profit[i] = (profit[i]*10)//amount[i]

final = [(amount[i], profit[i]) for i in range(0, len(amount))]

final.sort()
final = list(set(final))
print(final)

i = rand.randint(0, len(final)-1)
j = rand.randint(0, len(final)-1)


k = [[final[i]], [final[j]]]

flag = 0
while True:
    temp = [[], []]
    for x in final:
        if cal_dist(k, x):
            temp[1].append(x)
        else:
            temp[0].append(x)

    if temp[0] == k[0] and temp[1] == k[1]:
        k = temp
        break
    else:
        k = temp


print(k[0])
print("================================================================================================")
print(k[1])

x1 = [x[0] for x in k[0]]
y1 = [x[1] for x in k[0]]
x2 = [x[0] for x in k[1]]
y2 = [x[1] for x in k[1]]

plt.scatter(x1, y1, label="k2")
plt.scatter(x2, y2, label="k1")

plt.xlabel("Amount")
plt.ylabel("Profit/Amount")
plt.legend()

plt.show()
