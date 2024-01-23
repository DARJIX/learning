import pandas as pd
import numpy as np

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Names = ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ"]
City = ["MYSURU", "BANGLORE", "DELHI","MUMBAI","MYSURU", "BANGLORE", "DELHI", "MUMBAI", "MYSURU", "BANGLORE"]
columns = ['Number', 'Name', 'City']

ds = pd.DataFrame({'Number': Number, 'Name': Names, 'City': City}, columns=columns)

gender = pd.DataFrame({'Gender': ['Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male']})

ds['Gender'] = gender
ds['Height'] = np.random.randint(120, 175, size=(10,))  # Directly assign the array
ds['Weight'] = np.random.randint(50, 110, size=(10,))  # Directly assign the array
ds.set_index('Number', inplace=True)  # Set index in place

print(ds.describe())
print(ds.corr())