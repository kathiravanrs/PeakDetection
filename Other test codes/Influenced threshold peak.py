import pandas as pd
import numpy as np
# import pylab


def thresholding_algorithm(signal, lag_factor, threshold_factor, influence_factor):
    signals = np.zeros(len(signal))
    filtered_y = np.array(signal)
    avg_filter = [0]*len(signal)
    std_filter = [0]*len(signal)
    avg_filter[lag_factor - 1] = np.mean(signal[0:lag_factor])
    std_filter[lag_factor - 1] = np.std(signal[0:lag_factor])
    # print(avg_filter, std_filter)
    positive_peak, negative_peak = 0, 0
    for i in range(lag_factor, len(signal)):
        if abs(signal[i] - avg_filter[i-1]) > threshold_factor * std_filter[i-1]:
            if signal[i] > avg_filter[i-1]:
                signals[i] = 1
                positive_peak += 1
                # print(signal[i])
            else:
                signals[i] = -1
                negative_peak += 1
            filtered_y[i] = influence_factor * signal[i] + (1-influence_factor) * filtered_y[i-1]
            avg_filter[i] = np.mean(filtered_y[(i-lag_factor+1): i+1])
            std_filter[i] = np.std(filtered_y[(i-lag_factor+1): i+1])
        else:
            signals[i] = 0
            filtered_y[i] = signal[i]
            avg_filter[i] = np.mean(filtered_y[(i-lag_factor+1): i+1])
            std_filter[i] = np.std(filtered_y[(i-lag_factor+1): i+1])

    return dict(signals=np.asarray(signals),
                avgFilter=np.asarray(avg_filter),
                stdFilter=np.asarray(std_filter),
                positive=positive_peak,
                negative=negative_peak)


data = pd.read_excel("Excel data/SampleValues - Changed.xlsx")
y = data['Hydraulic Oil Pressure'].tolist()[:1000]

# Settings: lag = 30, threshold = 5, influence = 0
lag = 40
threshold = 4.5
influence = 0.5

# Run algo with settings from above
result = thresholding_algorithm(y, lag_factor=lag, threshold_factor=threshold, influence_factor=influence)
print(result['positive'])


# Plot result
# pylab.subplot(211)
# pylab.plot(np.arange(1, len(y)+1), y)
#
# pylab.plot(np.arange(1, len(y)+1),
#            result["avgFilter"], color="cyan", lw=2)
#
# pylab.plot(np.arange(1, len(y)+1),
#            result["avgFilter"] + threshold * result["stdFilter"], color="green", lw=2)
#
# pylab.plot(np.arange(1, len(y)+1),
#            result["avgFilter"] - threshold * result["stdFilter"], color="green", lw=2)
#
# pylab.subplot(212)
# pylab.step(np.arange(1, len(y)+1), result["signals"], color="red", lw=2)
# pylab.ylim(-1.5, 1.5)
# pylab.show()
