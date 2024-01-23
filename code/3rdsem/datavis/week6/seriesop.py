import pandas as pd
import numpy as np

s1 = pd.Series(['A', 'B', 'C', 'D', 'E', 'F'])
print("Original Series:")
print(s1)


print("\nCheck if 'F' is in the series:")
print(s1.str.contains('F'))




print("\nLength of the series:")
print(len(s1))


s2 = pd.Series([1, 20, 35, 67, 8, 9])


print("\nElements greater than 4:")
print(s2[s2>4])



s2 = s2.astype(str)

# Add two series
result = s1 + s2
print("\nConcatenation of two series:")
print(result)
