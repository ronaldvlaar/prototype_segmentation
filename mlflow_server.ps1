Write-Host "Starting MLflow server..."
rm -r E:/home/rvlaar/mlflow
cp -r E:/home/rvlaar/.mlflow/ E:/home/rvlaar/mlflow 
python update_meta.py 1
mlflow server `
    --backend-store-uri file://E:/home/rvlaar/mlflow
