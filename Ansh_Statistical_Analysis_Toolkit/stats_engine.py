import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")

columns = ['Amount', 'Discount', 'Quantity_Sold']

def compute_statistics(df, cols):
    print(" ")
    print("Mean = Average value")
    print("Median = Middle value of dataset")
    print("Variance = Measures how much the data values spread out from the mean.")
    print("Standard Deviation = Average distance of data points from the mean.")
    print("Skewness = Measures the asymmetry of a data distribution.Positive skew → long tail on the right,Negative skew → long tail on the left,Zero skew → symmetric distribution")
    print("Kurtosis = Measures the tailedness or peakedness of a distribution. High K -> heavy tail, Low K -> light tail")

    for col in columns:
        data = df[col]
        
        mean = np.mean(data)
        median = np.median(data)
        variance = np.var(data, ddof=1)      # sample variance
        std = np.std(data, ddof=1)            # sample std deviation
        skewness = np.mean(((data-mean)/std)**3)    # approach using numpy
        kurtosis = np.mean(((data-mean)/std)**4)    # approach using numpy

        print(f"\nStatistics for {col}")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Variance: {variance}")
        print(f"Standard Deviation: {std}")
        print(f"Skewness: {skewness}")
        print(f"Kurtosis: {kurtosis}")