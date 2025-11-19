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

