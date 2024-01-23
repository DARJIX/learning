"""use seabron to output the scatter plot"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
iris=pd.read_csv("Iris.csv") # use random.randn instead of using the csv file
sns.regplot(x="PetalLengthCm" , y="PetalLengthCm",data=iris)
plt.show()
