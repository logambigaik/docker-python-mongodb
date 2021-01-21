FROM python:3.6
RUN pip install flask flask_pymongo
COPY . /opt/
EXPOSE 5000
WORKDIR /opt
ENTRYPOINT ["python", "application.py"]
