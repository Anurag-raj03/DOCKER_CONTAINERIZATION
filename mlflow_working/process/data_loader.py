import pandas as pd
import logging

def loading_file(file_path:str):
   
    try:
        if file_path.endswith(".csv"):
            df=pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df=pd.read_excel(file_path)
        else:
            raise ValueError("The avialble file is not in the correct format")
        logging.info(f"Data loaded successfully {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading the data")
        return None
        
        
            
            