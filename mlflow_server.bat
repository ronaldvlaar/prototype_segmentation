@echo off
echo Starting MLflow server...
mlflow server --backend-store-uri file://D:\\
timeout /t 5 /nobreak >nul

