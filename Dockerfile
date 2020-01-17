FROM python:2.7
RUN pip install flask
COPY app.py app.py
ENTRYPOINT [ "./app.py" ]