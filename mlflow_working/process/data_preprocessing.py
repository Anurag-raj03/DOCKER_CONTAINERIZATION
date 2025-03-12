import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
import logging

def droping_null(df:pd.DataFrame):
    logging.info("Dropping the na values because the na values are very less")
    t=df.isna().sum().max()
    if t<60:
        df.dropna(inplace=True)
        logging.info(f"Successfully deleted the the na values Because values are less than the threshold {t} ")
    else:
        raise ValueError(f"The number of na values is more than the threshold.{t}")
    return df


def dropping_unwanted_cols(df:pd.DataFrame):
    logging.info("Dropping the unwanted columns after the EDA on the Data")
    df.drop(['ID','Bedtime','Wakeup time'],axis=1,inplace=True)
    return df



def encode(df: pd.DataFrame):
    le = LabelEncoder()
    categorical_cols = df.select_dtypes(include=['object', 'string']).columns  

    if categorical_cols.empty:
        logging.warning("No categorical columns found for encoding!")
        return df  

    for col in categorical_cols:
        logging.info(f"Encoding column: {col}")  
        df[col] = le.fit_transform(df[col])

    logging.info("Label encoding completed successfully!")
    return df   
    