@echo off
echo Starting MLflow server...
mlflow server ^
    --backend-store-uri file://D:\\ ^
    --default-artifact-root .


