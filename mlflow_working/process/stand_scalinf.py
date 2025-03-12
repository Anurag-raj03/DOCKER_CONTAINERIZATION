from sklearn.preprocessing import StandardScaler
import pandas as pd

def scale_features(df: pd.DataFrame):
    if 'Sleep efficiency' not in df.columns:
        raise KeyError("Column 'Sleep efficiency' is not present in the DataFrame")
    
    scaler = StandardScaler()
    
    cols_to_scale = df.columns[df.columns != 'Sleep efficiency']
    
    df_scaled = df.copy()
    df_scaled[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    
    return df_scaled
