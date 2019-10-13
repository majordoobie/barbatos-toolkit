### Sample of a config
```
FROM Ubuntu # image base?
RUN apt-get update 
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APPP=/opt/source-code/app.py flask run
```