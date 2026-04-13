From pyhton:3.9-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r -e .

ENV PYTHONPATH=.
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0 ,--server.headless=true"]

