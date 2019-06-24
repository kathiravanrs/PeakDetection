import pandas as pd
import numpy as np


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
excel_data2 = pd.read_excel("SampleValues - Changed.xlsx")
oil_pressure2 = excel_data2['Hydraulic Oil Pressure'].tolist()

slice_range = 200
print('\n')
for thresh in [0.5, 0.75, 1, 1.5, 1.75, 2, 2.5, 3, 3.5, 4, 4.5]:
    for initial in [30, 40, 50, 60]:
        print("threshold = {:<4}\tlength = {:<2}\t\t"
              "Peaks2 = ({:<2},{:<2})\tPeaks4 = ({:<2},{:<2})\t"
              "Peaks6 = ({},{})\tPeaks8 = ({},{})\tPeaks10 = ({},{})"
              .format(thresh,
                      initial,
                      peak_detection(oil_pressure2[:slice_range], initial, thresh),
                      peak_detection(oil_pressure[:slice_range], initial, thresh),
                      peak_detection(oil_pressure2[:2*slice_range], initial, thresh),
                      peak_detection(oil_pressure[:2*slice_range], initial, thresh),
                      peak_detection(oil_pressure2[:3*slice_range], initial, thresh),
                      peak_detection(oil_pressure[:3*slice_range], initial, thresh),
                      peak_detection(oil_pressure2[:4*slice_range], initial, thresh),
                      peak_detection(oil_pressure[:4*slice_range], initial, thresh),
                      peak_detection(oil_pressure2[:5*slice_range], initial, thresh),
                      peak_detection(oil_pressure[:5*slice_range], initial, thresh)))
    print('\n')
