# Shows the sales of furniture , clothing and electronics throughout the year.

from main import * 
import matplotlib.pyplot as plt


Month = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]

f = [0 for i in range(12)] 
c = [0 for i in range(12)] 
e = [0 for i in range(12)] 

for i in range(0,len(target),1) : 
    # print(Month.index(month[i]))
    if item_type[i] == "Furniture" :
        f[Month.index(month[i])] = target[i]
    if item_type[i] == "Clothing" : 
        c[Month.index(month[i])] = target[i]
    if item_type[i] == "Electronics" : 
        e[Month.index(month[i])] = target[i]


# print(f , c , e)

w = 0.2 
b1 = [i+1 for i in range(12)]
b2 = [i+1+w for i in range(12)]
b3 = [i+1+2*w for i in range(12)]

plt.bar(b1 , f , w ,  label = "Furniture")
plt.bar(b2 , c , w , label = "Clothing")
plt.bar(b3 , e , w , label = "Electronics")

plt.legend()
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(b2 , Month)

plt.title("Sales Target")
plt.show() ; 






