FROM tiangolo/uvicorn-gunicorn:python3.11

RUN pip install fastapi
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]