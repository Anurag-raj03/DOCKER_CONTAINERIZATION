from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import logging

def model_training(x_train:pd.DataFrame,y_train:pd.Series):
    if len(x_train)!=len(y_train):
        raise ValueError(f"Mismatch the number of sample between the x_train {len(x_train)} and y_train {len(y_train)}")
    logging.info("Training the RandomForestRegressor model..")
    rf_model=RandomForestRegressor()
    rf_model.fit(x_train,y_train)
    logging.info("Model Training completed successfully.")
    
    return rf_model
    