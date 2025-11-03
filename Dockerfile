FROM python:3.13-slim
WORKDIR /app
RUN pip install numpy scikit-learn==1.7.0 xgboost==3.1.1 fastapi uvicorn
COPY . .
EXPOSE 8080
CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8080"]