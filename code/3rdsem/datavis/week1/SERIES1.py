import pandas as pd
s2=pd.Series([100,200,300,400,500],index=['A','B','C','D','E'])
print(s2.to_string(dtype=False))
