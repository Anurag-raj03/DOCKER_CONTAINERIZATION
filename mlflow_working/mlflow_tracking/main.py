import mlflow
import mlflow.sklearn
import yaml
import os
import logging
import sys
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from process.data_ingestion import reading_file
from process.data_loader import loading_file
from process.data_preprocessing import droping_null, dropping_unwanted_cols, encode
from process.outliers_removal import removing_outliers
from process.stand_scalinf import scale_features
from process.data_split import spliting
from process.model_train import model_training
from process.model_acc import check_dump

config_path = os.path.join(os.path.dirname(__file__), "config.yaml")

with open(config_path, "r") as file:
    config = yaml.safe_load(file)

logging.basicConfig(level=config["logging"]["log_level"], filename=config["logging"]["log_file"], format='%(asctime)s - %(levelname)s - %(message)s')

mlflow.set_tracking_uri(config["mlflow"]["tracking_uri"])
experiment = mlflow.get_experiment_by_name(config["mlflow"]["experiment_name"])

if experiment is None:
    logging.info("Experiment does not exist. Creating a new one.")
    experiment_id = mlflow.create_experiment(config["mlflow"]["experiment_name"])
else:
    logging.info("Using existing experiment: %s", config["mlflow"]["experiment_name"])
    experiment_id = experiment.experiment_id

mlflow.set_experiment(experiment_id=experiment_id)

def main():
    logging.info("Pipeline Execution Started")
    with mlflow.start_run(run_name=config["mlflow"]["run_name"]):
        try:
            file_path = reading_file(r"C:\\Users\\Anurag\\OneDrive\\Desktop\\macine_operation\\mlflow_working\\DATA")
            logging.info(f"Data file found: {file_path}")
            
            df = loading_file(file_path)
            logging.info("File has been loaded successfully.")
            
            df = droping_null(df)
            df = dropping_unwanted_cols(df)
            df = encode(df)
            df = removing_outliers(df)
            df = scale_features(df)
            
            
            logging.info("Preprocessing and feature scaling completed successfully.")
            
            x_train, x_test, y_train, y_test = spliting(df)
            print("x_train",x_train.columns)
            logging.info(f"Data successfully split into train and test. Train shape: {x_train.shape}, Test shape: {x_test.shape}.")
            
            model = model_training(x_train, y_train)
            logging.info("Model trained successfully.")
            
            metric_value = check_dump(model, x_test, y_test)
            logging.info("Model dumped successfully.")

            input_example = np.array(x_test.iloc[:1])  
            mlflow.sklearn.log_model(
                model, 
                config["mlflow"]["artifact_path"],
                input_example=input_example
            )
            
            mlflow.log_param("model_type", config["model"]["type"])
            mlflow.log_params({"test_size": config["training"]["test_size"], "random_state": config["training"]["random_state"]})
            mlflow.log_metric(config["training"]["metric"], metric_value)
        
            logging.info("🎉 Pipeline Execution Completed Successfully!")
        
        except Exception as e:
            logging.error(f"Error Occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
