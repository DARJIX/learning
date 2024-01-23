
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Destination": ["Manager", "Developer", "Analyst", "Manager", "Analyst"],
    "Department": ["IT", "HR", "Finance", "IT", "Finance"],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "No._of_projects": [5, 3, 2, 4, 6],
    "Service": [10, 5, 8, 6, 7],
    "Salary": [80, 60, 70, 75, 90]
}
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

hf=pd.read_csv("data.csv")
print(hf)


'''hf.plot()
plt.show()'''



'''plt.figure(figsize=(10, 6))
plt.plot(df["Service"],color='blue', label='Service')
plt.plot(df["Salary"],color='green', label='Salary')
plt.show()'''

"""d1=hf.groupby(['Service']).sum()
d1.sort_values("Salary",ascending=False,inplace=True)
d1["Salary"].plot.bar()
plt.show()"""

hf[["No._of_projects","Service"]].head(10).plot.bar(color=['blue','red'])
plt.title('No._of_projects VS Service')
plt.show()
