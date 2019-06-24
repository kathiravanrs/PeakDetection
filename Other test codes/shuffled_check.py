import pandas as pd
import numpy as np
from random import shuffle

def peak_detection(data, lag, threshold):
    mean = np.mean(data[:lag])
    std = np.std(data[:lag])
    peak = 0
    for val in data:
        if (val-mean)/std > threshold:
            peak += 1
    return peak


excel_data = pd.read_excel("SampleValues.xlsx")
oil_pressure = excel_data['Hydraulic Oil Pressure'].tolist()
oil_pressure2 = oil_pressure[:200]
oil_pressure4 = oil_pressure[:400]
oil_pressure6 = oil_pressure[:600]
oil_pressure8 = oil_pressure[:800]
oil_pressure10 = oil_pressure[:1000]

shuffle(oil_pressure2)
shuffle(oil_pressure4)
shuffle(oil_pressure6)
shuffle(oil_pressure8)
shuffle(oil_pressure10)



print('\n')
for thresh in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
    for initial in [30, 40, 50, 60, 70, 80, 90, 100]:
        print("threshold = {:<4}\tlength = {:<3}\t\t\t"
              "Peaks2 = {:<3}\t\t\tPeaks4 = {:<3}\t\t\t"
              "Peaks6 = {:<3}\t\t\tPeaks8 = {:<3}\t\t\tPeaks10 = {}"
              .format(thresh,
                      initial,
                      peak_detection(oil_pressure2, initial, thresh),
                      peak_detection(oil_pressure4, initial, thresh),
                      peak_detection(oil_pressure6, initial, thresh),
                      peak_detection(oil_pressure8, initial, thresh),
                      peak_detection(oil_pressure10, initial, thresh)))
    print('\n')
