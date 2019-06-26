import pandas as pd
import numpy as np


def peak_detection(data, lag):
    # Lag is the number of items we consider for finding the mean and std deviation
    mean = np.mean(data[:lag])  # Mean of first 'lag' number of samples
    std = np.std(data[:lag])    # Standard deviation of first 'lag' number of samples
    peak = 0                # Initial peak count = 0
    if std*10 > mean:       # Condition to consider a values as peak
        for val in data:    # If the mean is much larger than the std, then values greater than mean are peaks
            if val > mean:
                peak += 1
    return peak


def print_peaks(input_path):
    print('\n', input_path, '\n')
    excel_data = pd.read_excel(input_path)  # Reading the excel file from the input path

    # Splitting the data into smaller segments of 200 items in length
    oil_pressure = excel_data['Hydraulic Oil Pressure'].tolist()
    oil_pressure2 = oil_pressure[0:200]     # Segment containing first 200 samples
    oil_pressure4 = oil_pressure[200:400]   # Samples containing next 200 samples from 200 to 400
    oil_pressure6 = oil_pressure[400:600]   # 400 to 600 samples
    oil_pressure8 = oil_pressure[600:800]
    oil_pressure10 = oil_pressure[800:1000]
    oil_pressure12 = oil_pressure[1000:1200]
    oil_pressure14 = oil_pressure[1200:1400]
    oil_pressure16 = oil_pressure[1400:1600]
    oil_pressure18 = oil_pressure[1600:1800]
    oil_pressure20 = oil_pressure[1800:2000]
    oil_pressure22 = oil_pressure[2000:2200]
    oil_pressure24 = oil_pressure[2200:2400]
    oil_pressure26 = oil_pressure[2400:2600]

    # Taking the first 100, 150 samples or using full 200 samples to find the mean and standard deviation
    for lag in [100, 150, 200]:

        print("length = {:<3}\t\t"
              "total = {:<4}\t[0:2] = {:<3}\t"
              "[2:4] = {:<3}\t[4:6] = {:<3}\t"
              "[6:8] = {:<3}\t[8:10] = {:<3}\t"
              "[10:12] = {:<3}\t[12:14] = {:<3}\t"
              "[14:16] = {:<3}\t[16:18] = {:<3}\t"
              "[18:20] = {:<3}\t[20:22] = {:<3}\t"
              "[22:24] = {:<3}\t[24:26] = {}"
              .format(lag,
                      peak_detection(oil_pressure, lag),    # Number of peaks in first segment 0 - 200
                      peak_detection(oil_pressure2, lag),   # Number of peaks in second segment 200 - 400
                      peak_detection(oil_pressure4, lag),   # Number of peaks in third segment 400 - 600
                      peak_detection(oil_pressure6, lag),   # 600 - 800
                      peak_detection(oil_pressure8, lag),   # 800 - 1000
                      peak_detection(oil_pressure10, lag),
                      peak_detection(oil_pressure12, lag),
                      peak_detection(oil_pressure14, lag),
                      peak_detection(oil_pressure16, lag),
                      peak_detection(oil_pressure18, lag),
                      peak_detection(oil_pressure20, lag),
                      peak_detection(oil_pressure22, lag),
                      peak_detection(oil_pressure24, lag),
                      peak_detection(oil_pressure26, lag)))


print_peaks("Excel data/SampleValues.xlsx")                   # First given data
print_peaks("Excel data/sampleValues - Higher.xlsx")          # First given data but a constant value is added to all samples
print_peaks("Excel data/sampleValues - Changed.xlsx")         # First given data but shuffled
print_peaks("Excel data/sampleValues - Changed Higher.xlsx")  # First given data, shuffled and constant added
print_peaks("Excel data/sampleValues - New.xlsx")             # New data from the debug message file
print_peaks("Excel data/sampleValues - New Higher.xlsx")      # Constant value is added to the newer data
print_peaks("Excel data/sampleValues - Newer.xlsx")           # New Data is shuffled
