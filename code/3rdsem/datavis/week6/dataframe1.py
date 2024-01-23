import pandas as pd
    
df1=pd.DataFrame({'test1':[95,84,73,88,82,61],'test2':[74,85,82,73,77,79]},index=['hij','abc','def','ghi','jkl','mno'])

print(df1,end="\n\n")

print(df1['test2'],end="\n\n")

print(df1.loc['hij'],end="\n\n")

print(df1.iloc[0:2],end="\n\n")

print(df1.iloc[::2],end="\n\n")