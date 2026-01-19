import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("sales.csv")

columns = ['Amount', 'Discount', 'Quantity_Sold']

def analyze_distribution(df, cols):
    for col in columns:
        data = df[col]

        plt.hist(data, bins ='fd')
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.title(f"Histogram For Sales {col}")
        plt.show()

        plt.boxplot(data)
        plt.ylabel(col)
        plt.title(f"BoxPlot For Sales {col}")
        plt.show()