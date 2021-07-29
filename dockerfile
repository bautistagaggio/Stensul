
FROM python:3.9.5-alpine

# run a docker build command and the image gets created.

RUN mkdir /usr/src/tests

WORKDIR /usr/src/tests

COPY STENSUL /usr/src/tests

# copy requirments.txt to the working directory
COPY ./requirements.txt .

# installing dependencies 

RUN python -m pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .

# run the docker build command again

COPY ./setup.py ./setup.py

RUN make install-dev

CMD ["pytest", "--junit-xml=testResults.xml", "--log-cli-level=INFO"]



