from main import * 
import matplotlib.pyplot as plt

# amount - profit 
f = [[] , []]
c = [[] , []]
e = [[] , []]

for i in range(0 , len(cat)) : 
    if cat[i] == "Furniture" : 
        f[0].append(amount[i])
        f[1].append(profit[i])
    if cat[i] == "Clothing" : 
        c[0].append(amount[i])
        c[1].append(profit[i])
    if cat[i] == "Electronics" : 
        e[0].append(amount[i])
        e[1].append(profit[i])

plt.scatter(f[0] , f[1] , label = "furniture")
plt.scatter(c[0] , c[1] , label = "clothing")
plt.scatter(e[0] , e[1] , label = "electronics")

plt.xlabel("Amount")
plt.ylabel("profit")
plt.xticks([60,120,180,240 ,300,360,420,480,540,600] , [100*i for i in range(1,11,1)])
plt.yticks([])

plt.title("Amount vs Profit")
plt.legend() 
plt.show() 

    
