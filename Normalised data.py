import pandas as pd
import numpy as np
from random import shuffle


def peak_detection(data, lag):
    totalmean = np.mean(data)
    data = [(x-totalmean) for x in data]

    mean = np.mean(data[:lag])
    std = np.std(data[:lag])
    peak = 0
    if std > mean:
        for val in data:
            if (val-mean) > 0:
                peak += 1
        return peak


def print_peaks(input_path):
    print('\n', input_path, '\n')
    excel_data = pd.read_excel(input_path)
    oil_pressure = excel_data['Hydraulic Oil Pressure'].tolist()
    oil_pressure2 = oil_pressure[0:200]
    oil_pressure4 = oil_pressure[200:400]
    oil_pressure6 = oil_pressure[400:600]
    oil_pressure8 = oil_pressure[600:800]
    oil_pressure10 = oil_pressure[800:1000]
    oil_pressure12 = oil_pressure[1000:1200]
    oil_pressure14 = oil_pressure[1200:1400]
    oil_pressure16 = oil_pressure[1400:1600]
    oil_pressure18 = oil_pressure[1600:1800]

    shuffle(oil_pressure2)
    shuffle(oil_pressure4)
    shuffle(oil_pressure6)
    shuffle(oil_pressure8)
    shuffle(oil_pressure10)
    shuffle(oil_pressure12)
    shuffle(oil_pressure14)
    shuffle(oil_pressure16)
    shuffle(oil_pressure18)

    for initial in [50, 100, 200]:

        print("length = {:<3}\t\t[0:2] = {:<3}\t"
              "[2:4] = {:<3}\t[4:6] = {:<3}\t"
              "[6:8] = {:<3}\t[8:10] = {:<3}\t"
              "[10:12] = {:<3}\t[12:14] = {:<3}\t"
              "[14:16] = {:<3}\t[16:18] = {}"
              .format(initial,
                      str(peak_detection(oil_pressure2, initial)),
                      str(peak_detection(oil_pressure4, initial)),
                      str(peak_detection(oil_pressure6, initial)),
                      str(peak_detection(oil_pressure8, initial)),
                      str(peak_detection(oil_pressure10, initial)),
                      str(peak_detection(oil_pressure12, initial)),
                      str(peak_detection(oil_pressure14, initial)),
                      str(peak_detection(oil_pressure16, initial)),
                      str(peak_detection(oil_pressure18, initial))

                      ))


print_peaks("Excel data/SampleValues.xlsx")
print_peaks("Excel data/sampleValues - Higher.xlsx")

print_peaks("Excel data/sampleValues - Changed.xlsx")
print_peaks("Excel data/sampleValues - Changed Higher.xlsx")

print_peaks("Excel data/sampleValues - New.xlsx")
print_peaks("Excel data/sampleValues - New Higher.xlsx")
