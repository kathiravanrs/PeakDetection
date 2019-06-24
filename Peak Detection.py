import pandas as pd
import numpy as np


def peak_detection(data, lag):
    # Lag is the number of items we consider for finding the mean and std deviation
    mean = np.mean(data[:lag])
    std = np.std(data[:lag])
    peak = 0
    if std*10 > mean:
        for val in data:
            if (val-mean) > 0:
                peak += 1
    return peak


def print_peaks(input_path):
    print('\n', input_path, '\n')
    excel_data = pd.read_excel(input_path)  # Reading the excel file from the input path

    # Splitting the data into smaller segments of 200 items in length
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
                      peak_detection(oil_pressure, lag),
                      peak_detection(oil_pressure2, lag),
                      peak_detection(oil_pressure4, lag),
                      peak_detection(oil_pressure6, lag),
                      peak_detection(oil_pressure8, lag),
                      peak_detection(oil_pressure10, lag),
                      peak_detection(oil_pressure12, lag),
                      peak_detection(oil_pressure14, lag),
                      peak_detection(oil_pressure16, lag),
                      peak_detection(oil_pressure18, lag),
                      peak_detection(oil_pressure20, lag),
                      peak_detection(oil_pressure22, lag),
                      peak_detection(oil_pressure24, lag),
                      peak_detection(oil_pressure26, lag)))


print_peaks("Excel data/SampleValues.xlsx")                     # First given data
print_peaks("Excel data/sampleValues - Higher.xlsx")    # First given data but a constant value is added to all samples
print_peaks("Excel data/sampleValues - Changed.xlsx")           # First given data but shuffled
print_peaks("Excel data/sampleValues - Changed Higher.xlsx")    # First given data, shuffled and constant added
print_peaks("Excel data/sampleValues - New.xlsx")               # New data from the debug message file
print_peaks("Excel data/sampleValues - New Higher.xlsx")        # Constant value is added to the newer data
print_peaks("Excel data/sampleValues - Newer.xlsx")             # New Data is shuffled
