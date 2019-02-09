FROM python:3

WORKDIR /python-api-testing

COPY . ./

RUN pip install --upgrade pip
RUN pip install behave
RUN pip install requests