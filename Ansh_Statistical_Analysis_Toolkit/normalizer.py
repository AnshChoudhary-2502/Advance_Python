import pandas as pd

df = pd.read_csv("sales.csv")

columns = ['Amount', 'Discount', 'Quantity_Sold']

print("Min–Max scaling rescales data into a fixed range, usually [0, 1].")

df_minmax = df.copy()
for col in columns:
    min_val = df[col].min()
    max_val = df[col].max()

    df_minmax[col] = (df[col] - min_val) / (max_val - min_val)
    # print(df_minmax)

numeric_cols = ['Amount', 'Discount', 'Quantity_Sold']

def apply_normalization(df, cols):
    print("Z-score scaling centers data around 0 and scales it by standard deviation.")

    df_zscore = df.copy()
    for col in numeric_cols:
        mean = df[col].mean()
        std = df[col].std()

        if std != 0:
            df_zscore[col] = (df[col] - mean) / std
        # print(df_zscore[col].head(20))

    print("Robust scaling uses: (Median instead of mean, IQR instead of standard deviation) for outlier heavy data")

    df_robust = df.copy()

    for col in numeric_cols:
        median = df[col].median()
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        if iqr != 0:
            df_robust[col] = (df[col] - median) / iqr

    print(df_robust.head(20))