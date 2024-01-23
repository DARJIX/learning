import seaborn as sns
import pandas as pd
iris=pd.read_csv("Iris.csv")
sns.regplot(x="PetalLengthCm" , y="PetalLengthCm",data=iris)
plt.show()
 