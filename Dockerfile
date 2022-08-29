FROM balabit/syslog-ng:latest

RUN apt install && apt update && apt upgrade && apt dist-upgrade
RUN apt install -y python3 && apt install python3-pip -y
COPY logparser.zip app/
COPY requirements.txt app/
RUN apt install nano -y
RUN apt install zip -y
RUN cd app/ && unzip logparser.zip
RUN pip3 install -r /app/requirements.txt
COPY start.sh opt/
ENTRYPOINT ["/bin/echo", "/opt/start.sh"]