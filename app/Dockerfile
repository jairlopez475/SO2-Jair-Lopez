FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN useradd -u 10001 -r appuser
USER 10001
EXPOSE 8080
CMD ["python", "app.py"]
