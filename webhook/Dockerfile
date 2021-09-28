FROM python:3.8
RUN mkdir -p /home/src/webhook
ADD requirements.txt /home/src/webhook
RUN pip install -r /home/src/webhook/requirements.txt
ADD main.py /home/src/webhook
ADD run.sh /home/src/webhook
ADD /app /home/src/webhook/app
RUN chmod +x /home/src/webhook/run.sh
ENV FLASK_APP /home/src/webhook/app/__init__.py
CMD /home/src/webhook/run.sh
