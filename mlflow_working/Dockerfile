FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY streamlit_app/ /app/

COPY process/ /app/process/

COPY Saved_model/ /app/Saved_model/

COPY DATA/ /app/DATA/

RUN mkdir -p /app/logs /app/mlflow_tracking

EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
