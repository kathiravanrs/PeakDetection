import pandas as pd
import numpy as np
from math import pi, sqrt, exp

data = pd.read_excel("SampleValues.xlsx")
oil_pressure = data['Hydraulic Oil Pressure'].tolist()[:200]
peak = 0

for count in range(1, len(oil_pressure)//30):
    pressure_slice = oil_pressure[(count - 1) * 30: count * 30]
    mean = np.mean(pressure_slice)
    std = np.std(pressure_slice)

    for val in pressure_slice:
        z = (val-mean)/std
        normal = 1/sqrt(2*pi) * exp(-(z*z)/2)
        if 1-normal > 0.85:
            peak += 1

print(peak)
