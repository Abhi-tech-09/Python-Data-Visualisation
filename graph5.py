from main import * 
import matplotlib.pyplot as plt

f = [0 for i in range(0,500)]
c = [0 for i in range(0,500)]
e = [0 for i in range(0,500)]

for i in range(0,len(cat)) :
    if cat[i] == "Furniture" : 
        f[order[i]] += quant[i]
    if cat[i] == "Clothing" : 
        c[order[i]] += quant[i]
    if cat[i] == "Electronics" : 
        e[order[i]] += quant[i]


m = [0,0,0]
g = [0,0,0]
up= [0,0,0]
mp = [0,0,0]
r = [0,0,0]

for i in range(len(state)) : 
    if state[i] == "Maharashtra" : 
        m[0] += f[ord[i]]
        m[1] += c[ord[i]]
        m[2] += e[ord[i]]
    if state[i] == "Gujarat" : 
        g[0] += f[ord[i]]
        g[1] += c[ord[i]]
        g[2] += e[ord[i]]
    if state[i] == "Uttar Pradesh" : 
        up[0] += f[ord[i]]
        up[1] += c[ord[i]]
        up[2] += e[ord[i]]
    if state[i] == "Madhya Pradesh" : 
        mp[0] += f[ord[i]]
        mp[1] += c[ord[i]]
        mp[2] += e[ord[i]]
    if state[i] == "Rajasthan" : 
        r[0] += f[ord[i]]
        r[1] += c[ord[i]]
        r[2] += e[ord[i]]


plt.bar([1,2,3,4,5], [m[0] , g[0] , up[0],mp[0],r[0]] , label = "furniture")
plt.bar([1,2,3,4,5], [m[1] , g[1] , up[1],mp[1],r[1]] , bottom = [m[0] , g[0] , up[0],mp[0],r[0]] , label = "clothing")
plt.bar([1,2,3,4,5], [m[2] , g[2] , up[2],mp[2],r[2]] , bottom = [m[1]+m[0] , g[1]+g[0] , up[1]+up[0],mp[1]+mp[0],r[1]+r[0]] , label = "electronics")

plt.xlabel("cities")
plt.ylabel("Quantity")
plt.xticks([1,2,3,4,5],['Maharashtra','Gujarat','Uttar Pradesh','Madhya Pradesh' ,'Rajasthan'])
plt.xlabel("States")
plt.ylabel("Number of items");
plt.legend() ;  
plt.show() ;

