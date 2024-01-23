import pandas as pd
s1=pd.Series(data=[31,41,51])
print((s1>40).to_string(dtype=False),"\n\n")
print(s1[s1>40].to_string(dtype=False))

