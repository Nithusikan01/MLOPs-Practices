import os
import sys
import warnings
import logging

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from urllib.parse import urlparse

import mlflow
from mlflow.models.signature import infer_signature
import mlflow.sklearn

import dagshub

# Initialize and connect with dagshub repo
dagshub.init(repo_owner='tnithusikan', repo_name='MLOPs-Practices', mlflow=True)

# Initializer logger and log events
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

def metrics(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return rmse, mae, r2

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(0)

    # Read the csv data file using the url
    csv_url = (
         "https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv"
    )

    try:
        data = pd.read_csv(csv_url, sep=";")
    except Exception as e:
        logger.exception(
            "Unable to load the data file. Error: %s", e
        )
    
    # Split the dataset
    y = data["quality"]
    X = data.drop(columns=["quality"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Get hyperparameters as cmd arguments
    learning_rate = float(sys.argv[1]  if len(sys.argv) > 1 else 0.01)
    l1_ratio = float(sys.argv[2] if len(sys.argv) > 1 else 0.5)

    # Track experiments with mlfow
    with mlflow.start_run():
        # Build and train the model
        lr = ElasticNet(alpha=learning_rate, l1_ratio=l1_ratio, random_state=42)
        lr.fit(X_train, y_train)

        # Predict and evaluate the model
        pred_qualities = lr.predict(X_test)
        (rmse, mae, r2) = metrics(y_test, pred_qualities)

        print("Elasticnet model(alpha={:f}, l1_ratio={:f}):".format(learning_rate, l1_ratio))
        print(f"\nRMSE: {rmse}\nMAE: {mae}\n R2 Score: {r2}")

        mlflow.log_param("alpha", learning_rate)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # For remote server only (Dagshub)
        remote_server_uri = "https://dagshub.com/tnithusikan/MLOPs-Practices.mlflow"
        mlflow.set_tracking_uri(remote_server_uri)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registery(It doesn't work with the file store)
        if tracking_url_type_store != "file":
            # Register the model
            mlflow.sklearn.log_model(
                lr, "model", registered_model_name="ElasticnetWineModel"
            )
        else:
            mlflow.sklearn.log_model(lr, "model")


