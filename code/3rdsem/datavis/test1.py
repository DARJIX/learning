import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


np.random.seed(42)
random.seed(42)


categories = ['Food', 'Fashion', 'Lifestyle', 'Sports', 'News']
num_records = 10 

data = {
    'Category': [random.choice(categories) for _ in range(num_records)],
    'Followers': np.random.randint(0, 100000, size=num_records),
    'Likes': np.random.randint(-100, 1000, size=num_records)
}

df = pd.DataFrame(data)


   

negative_likes_rows = df[df['Followers'] < 0]
if not negative_likes_rows.empty:
    print("\nRows with negative Followers:")
    print(negative_likes_rows)
    

category_counts = df['Category'].value_counts()
print("\nCategory Counts:")
print(category_counts)


print("\nFirst Five Rows:")
print(df.head())

print("\nLast Five Rows:")
print(df.tail())


plt.figure(figsize=(10, 6))
plt.plot(df['Likes'])
plt.title('Likes Column Plot')
plt.xlabel('Index')
plt.ylabel('Likes')
plt.show()