FROM python:alpine
RUN pip install flask
COPY app.py app.py
ENTRYPOINT [ "./app.py" ]
