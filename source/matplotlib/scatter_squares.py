import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x*x for x in x_values]
plt.scatter(x_values,y_values,c =y_values,cmap=plt.cm.Reds,edgecolors='none',s = 20)
plt.title("Scatter Squares",fontsize=24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("Square value",fontsize = 14)
plt.tick_params(axis='both',which ='major',labelsize=14)
plt.savefig('plot.png',bbox_inchs='tight')
plt.show()
