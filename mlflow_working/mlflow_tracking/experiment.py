import yaml

with open("mlflow_tracking/config.yaml", "r") as file:
    config = yaml.safe_load(file)

print(config["mlflow"]["experiment_name"])  
