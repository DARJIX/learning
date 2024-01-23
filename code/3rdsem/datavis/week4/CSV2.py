import pandas as pd
a=pd.read_csv("")
b=pd.read_csv("")
mergedDataSet=a.merge(b,on="Country name")
mergedDataSet.head()