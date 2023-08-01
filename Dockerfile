FROM python:3.12-rc-bullseye
COPY requirements.txt /app/
COPY app.py /app/
COPY project/ /app/project/
WORKDIR /app/
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]
