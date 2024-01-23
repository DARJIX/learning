import pandas as pd

s1=pd.Series([5,6,7,8,9,10])
print(s1,end="\n")
s2=s1
s2.index=(['A','B','C','D','E','F'])


print(s2)