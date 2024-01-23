import pandas as pd
import numpy as np
dataset=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['stock1','stock2','stock3'])
dataset=dataset.reindex(['a','b','c','d','e','f','g','h'])
#print(dataset)
#print(dataset['stock1'].isnull())
#print(dataset.fillna(0))
#print(dataset.fillna(method='ffill'))
#print(dataset.replace(np.nan,0))
print(dataset.dropna())