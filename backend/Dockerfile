FROM mysql

ADD ./db /create_db

RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install -y python3-pip \
&& apt-get clean \
&& pip3 install mysql-connector-python \
&& python3 /create_db/medishare_db.py