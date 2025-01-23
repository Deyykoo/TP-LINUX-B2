FROM python:3

RUN apt update -y

WORKDIR /app

COPY pythonApp/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./pythonApp/main.py .

CMD [ "python", "main.py"]