from sklearn.metrics import r2_score
import pandas as pd
import joblib as jb
from sklearn.ensemble import RandomForestRegressor
import os
import logging

def check_dump(rf_model:RandomForestRegressor,x_test:pd.DataFrame,y_test:pd.Series):
    logging.info("Checking the r2_score of the model")
    y_pred=rf_model.predict(x_test)
    acc=r2_score(y_test,y_pred)
    acc=acc*100
    logging.info(f"The R2 scor of the Regression Model is {acc:.4f}")
    
    if acc>=30:
        logging.info("Saving the Model in the Directoery")
        model_dir = r"C:\Users\Anurag\OneDrive\Desktop\macine_operation\mlflow_working\Saved_model"
        os.makedirs(model_dir, exist_ok=True)
        
        model_path = os.path.join(model_dir, "rf_model.jbl")
        
        # Ensure the model is being saved properly
        jb.dump(rf_model, model_path)
        
        print(f"✅ Model Successfully Saved at {model_path}")
    else:
        logging.error(f"Model R2 is Less Than the 70% threshold So we are not Saving this {acc}")    
    return acc   