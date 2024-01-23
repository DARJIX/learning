import matplotlib.pyplot as plt
plt.style.use("seaborn-v0")
X=[590,540,740,130,810,300,320,230,470,620,770,250]
Y=[32,36,39,52,61,72,77,75,68,57,48,48]
plt.scatter(X,Y)
plt.xlim(0,1000)
plt.ylim(0,100)
plt.title("Relation b/w Temp and Ice coffee")
plt.xlabel('sold coffee')
plt.ylabel('temp in F')
plt.show()
