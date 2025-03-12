import pandas as pd
import os 

def reading_file(data_dir: str = "Data/"):
    valid_data=['csv','xlsx']
    files=[]
    for i in os.listdir(data_dir):
        if i.split(".")[-1] in valid_data:
            files.append(i)
    if not files:
        raise FileNotFoundError ("No file in the directory found following the these CSV or XLSX format")  
    if len(files)>1:
        raise ValueError("Multiple file in the folder found Kindly Make sure Only One file present")  
    return os.path.join(data_dir,files[0])
           
    
    