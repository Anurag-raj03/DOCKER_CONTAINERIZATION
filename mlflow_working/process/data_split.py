from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import logging

def spliting(df:pd.DataFrame):
    if 'Sleep efficiency' not in df.columns:
         raise KeyError("Columns 'Sleep efficiency' is not present in the DataFrame")
    logging.info("Splitting the data into the train test")
    x=df.drop('Sleep efficiency',axis=1)
    y=df['Sleep efficiency']
    
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    return x_train,x_test,y_train,y_test