import pandas as pd
sales=pd.read_csv("datavis/codes-all.csv")
#print("\n\n<<<<<<<<<< First 5 records <<<<<<<\n\n")
#print(sales.head())
sales.rename(columns={"MinorUnit":'CO',"Symbol":'SYM'},inplace=True)
print(sales)
print(sales['CO'].unique())

