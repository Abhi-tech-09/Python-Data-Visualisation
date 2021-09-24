from main import * 
import matplotlib.pyplot as plt

h = []
for i in range(1 , 14) : 
    h.append([0 for i in range(1,33)])

for i in range(len(date)) : 
    s = "" 
    if date[i].find("/") != -1 : 
        a = date[i].split("/")
        month = int(a[1])
        day = int(a[0])
        # print(month , day)
        h[month][day] += 1 
    else : 
        a = date[i].split("-")
        month = int(a[1])
        day = int(a[0])
        # print(month , day)
        h[month][day] += 1

plt.pcolormesh( h ,  cmap = 'autumn' )


  
plt.title( '2-D Heat Map' )
plt.xlabel("Number of days")
plt.ylabel("Months")
plt.title("Monthly sales data")
plt.show()
