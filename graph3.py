from main import * 
import matplotlib.pyplot as plt
# from matplotlib import style
# style.use("ggplot")

# order - quantity
f = [0 for i in range(0,500)]
c = [0 for i in range(0,500)]
e = [0 for i in range(0,500)]

for i in range(0,len(cat)) : 
    # if order[i] == 200 : 
    #     break
    if cat[i] == "Furniture" : 
        f[order[i]] += quant[i]
    if cat[i] == "Clothing" : 
        c[order[i]] += quant[i]
    if cat[i] == "Electronics" : 
        e[order[i]] += quant[i]

r = max(len(f) , max(len(e),len(c)))


ra  = [i for i in range(0,500)]
# print(ra)
# plt.plot([],[],color ='b', label="furniture",linewidth=5)
# plt.plot([],[],color = 'g' ,label="clothing",linewidth=5)
# plt.plot([],[],color = 'k', label="electronics",linewidth=5)

# # ra = [1,2,3]
# plt.stackplot(ra , f , c , e , colors=['b','g','k']);



# plt.plot(ra , f , label = "furniture")
# plt.plot(ra , c , label = "clothing")
# plt.plot(ra , e , label = "electronics")

plt.scatter(ra , f , label = "furniture")
plt.scatter(ra , c , label = "clothing")
plt.scatter(ra , e , label = "electronics")

plt.title("Quantity bought per person")
plt.xlabel("Number of customes")
plt.ylabel("Number of items")
plt.legend() 
plt.show() 



