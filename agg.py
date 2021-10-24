print("Enter Item Order")
item = input().strip().split(' ')
# item = ['E', 'A', 'C', 'B', 'D']
print("\nEntire distance matrix enter karo")
dist = []
mx = 10**9+7
# enter it like this [[0.0, 0.71, 5.66, 3.61, 4.24, 3.2], [0.71, 0.0, 4.95, 2.92, 3.54, 2.5], [5.66, 4.95, 0.0, 2.24, 1.41, 2.5], [3.61, 2.92, 2.24, 0.0, 1.0, 0.5], [4.24, 3.54, 1.41, 1.0, 0.0, 1.12], [3.2, 2.5, 2.5, 0.5, 1.12, 0.0]]

# No input validation has been done 

for i in range(0, len(item)):
    temp = input().strip().split(' ')
    dist.append([float(x) for x in temp])

print(dist)
print(item)

dmap = {}

for i in range(0, len(dist)):
    dmap[item[i]] = {}
    for j in range(0, i):
        dmap[item[i]][item[j]] = dist[i][j]
        dmap[item[j]][item[i]] = dist[i][j]


# print(dmap)
oldmap = dmap
print(oldmap)


def cal_dist(x, y):
    if isinstance(x, str) and isinstance(y, str):
        # print(x)
        # print(y)
        # print("End call")
        return oldmap[x][y]
    mn = mx
    if isinstance(x, tuple):
        for val in x:
            mn = min(cal_dist(val, y), mn)
    elif isinstance(y, tuple):
        for val in y:
            mn = min(cal_dist(x, val), mn)
    return mn


# print(cal_dist('D', ('B', 'C')))

flag = 0
cnt = 0 
while len(item) != 1 :
    mn_value = mx
    mnt = []
    for x in item :
        for y in item :
            if x == y : 
                continue 
            val = cal_dist(x,y)
            if val < mn_value :
                mnt = [x,y]
                mn_value = val

    item.remove(item[item.index(mnt[0])])
    item.remove(item[item.index(mnt[1])])
    # print(item.index(mnt[1]))
    mnt = tuple(mnt)
    item.append(mnt)
   
print(item)
