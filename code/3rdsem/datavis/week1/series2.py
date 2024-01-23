import pandas as pd
s1=pd.Series([95,89,80,92],index=['IP','Math','Chem','Bio'])
for index,value in s1.items():
	value=value+10
	if index=='IP':
		print(f"the marks in {index} is :\t {value}")
	print(f"\n {index}\t{value}")
	
