import pandas as pd
s1=pd.Series([39,41,42,44],index=['A','B','C','D'])
s2=pd.Series([10,10,10,10],index=['A','B','C','D'])
print((s1[:2]*100).to_string(dtype=False),"\n")
print((s1*s2).to_string(dtype=False),"\n")
print((s2[::-1]*10).to_string(dtype=False),"\n")
