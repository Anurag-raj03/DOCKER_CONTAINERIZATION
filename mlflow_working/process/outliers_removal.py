import pandas as pd
import numpy as np

def removing_outliers(df: pd.DataFrame):
    df_filtered = df.copy()
    outlier_removed = False

    for col in df.select_dtypes(include=['float','int']).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        IQR = q3 - q1

        lower_bound = q1 - 1.5 * IQR
        upper_bound = q3 + 1.5 * IQR

        filtered_rows = (df_filtered[col] >= lower_bound) & (df_filtered[col] <= upper_bound)

        if not filtered_rows.all():
            outlier_removed = True

        df_filtered = df_filtered[filtered_rows]
    
    if not outlier_removed:
        return df
    
    return df_filtered
