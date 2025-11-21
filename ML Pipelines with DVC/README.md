# Build and Track ML Pipelines with DVC

## 1. Ceate a conda environment: dvc_env

```conda
conda create -n dvc_env python=3.11 -y

conda activate dvc_env

pip install -r requirements.txt
```

## 2. Necessary DVC Commands

```dvc
git init

dvc init

dvc repro

dvc dag

dvc metrics show
```

### About setup.py and main.py

This project includes two helper files used for structuring and running the ML pipeline:

#### setup.py
Makes the project installable as a Python package. This allows modules inside the project to be imported easily when the project is used in other environments, CI/CD pipelines, or Docker containers.

```Python
from setuptools import find_packages, setup

setup(
    name = "ML_DVC_Pipeline",
    version= "0.0.0",
    author="Ntx",
    author_email="tnithusikan@gmail.com",
    packages= find_packages(),
    install_requires=[]
)
```

#### main.py
Acts as a simple orchestrator that runs each pipeline stage (data ingestion → preprocessing → feature engineering → model building → evaluation) in sequence.
While tools like DVC manage pipeline execution more efficiently, main.py is included for convenience and manual execution if needed.

But remember this is outdated and not safe enough.

```Python
import os

os.system("python src/data_ingestion.py")
print("Data ingestion run")

os.system("python src/data_preprocessing.py")
print("Data data_preprocessing run")

os.system("python src/feature_engineering.py")
print("feature_engineering run")

os.system("python src/model_building.py")
print("model_building run")

os.system("python src/model_evaluation.py")
print("model_evaluation run")
```
