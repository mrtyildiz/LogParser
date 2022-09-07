FROM balabit/syslog-ng:latest

RUN apt install -y python3 && apt install python3-pip -y
COPY logparser.zip /
RUN apt install -y zip
RUN unzip logparser.zip -d /app
COPY requirements.txt app/
RUN apt install nano -y
RUN pip3 install -r /app/requirements.txt
COPY definition.py app/api_app/definition.py
COPY parser_new.py app/api_app/parser.py
COPY messages /var/log/
COPY start.sh opt/
#ENTRYPOINT ["/bin/echo", "/opt/start.sh"]