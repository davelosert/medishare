FROM python

ADD . /opt/medishare

RUN cd /opt/medishare && pip install -r  requirements.txt

CMD [ "python3", "/opt/medishare/medishare.py" ]
