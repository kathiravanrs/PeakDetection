import pandas as pd
import numpy as np


def peak_detection(data, lag):
    mean = np.mean(data[:lag])
    std = np.std(data[:lag])
    peak = 0
    if std > 10:
        for val in data:
            if (val-mean) > 0:
                peak += 1
    return peak


def print_peaks(input_path):
    print('\n', input_path, '\n')
    excel_data = pd.read_excel(input_path)
    oil_pressure = excel_data['Hydraulic Oil Pressure'].tolist()
    length = len(oil_pressure)
    total_peak = 0
    for i in range(1, length//200):
        segment = oil_pressure[(i-1)*200:i*200]
        total_peak += peak_detection(segment, 200)
        print(i*200, total_peak)
    print('\n\n')


print_peaks("Excel data/SampleValues.xlsx")
print_peaks("Excel data/sampleValues - Higher.xlsx")

print_peaks("Excel data/sampleValues - Changed.xlsx")
print_peaks("Excel data/sampleValues - Changed Higher.xlsx")

print_peaks("Excel data/sampleValues - New.xlsx")
print_peaks("Excel data/sampleValues - New Higher.xlsx")

print_peaks("Excel data/sampleValues - Newer.xlsx")
