FROM alpine:3.1
MAINTAINER Ziv Rechnitser <ziv@devops.co.il>

# Install server
RUN apk add --update python

# Copy the application folder inside the container
ADD /dummyspooler /dummyspooler

RUN pip install -r /dummyspooler/requirements.txt

ENTRYPOINT ["python main.py"]
