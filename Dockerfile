FROM registry.access.redhat.com/ubi8/python-39
RUN pip install flask
WORKDIR /source
COPY app.py app.py

ENTRYPOINT python3 /source/app.py

