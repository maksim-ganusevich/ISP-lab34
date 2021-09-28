FROM python:3.8
RUN mkdir -p /home/src/restapi
ADD requirements.txt /home/src/restapi
RUN pip install -r /home/src/restapi/requirements.txt
ADD main.py /home/src/restapi
ADD run.sh /home/src/restapi
ADD /app /home/src/restapi/app
RUN chmod +x /home/src/restapi/run.sh
ENV FLASK_APP /home/src/restapi/app/__init__.py
CMD /home/src/restapi/run.sh