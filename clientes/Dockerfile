FROM python:alpine
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.tx
ENTRYPOINT ["python"]
CMD ["principal.py"]