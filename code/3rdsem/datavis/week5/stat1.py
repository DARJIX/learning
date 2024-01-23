import pandas as pd
import numpy as np
my_series=pd.Series([1,2,3,4,5,6])
#series mean value,max value,min value,standard deviation value
mean=my_series.mean()
print("mean:",mean)
max=my_series.max()
print("Max:",max)
min=my_series.min()
print("Minimum:",min)
standdev=my_series.std()
print("Standard deviation:",standdev)