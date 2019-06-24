import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Excel data/SampleValues - Newer.xlsx")
oil_pressure = data['Hydraulic Oil Pressure'].tolist()
plt.hist(oil_pressure, bins=25)
plt.xlabel('Oil Pressure')
plt.ylabel('No of times repeated')
plt.show()
