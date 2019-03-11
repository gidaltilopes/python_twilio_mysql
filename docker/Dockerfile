FROM python:3.5.6-alpine
ADD . /<path>/python
WORKDIR /<path>/python
RUN pip3 install -r requeriments.txt
ENTRYPOINT ["python", "run.py"]
