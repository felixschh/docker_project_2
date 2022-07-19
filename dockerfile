FROM python:3

COPY ./requirements.txt /mnist-classifier/requirements.txt

WORKDIR /mnist-classifier

RUN pip3 install -r requirements.txt

COPY . /mnist-classifier

ENTRYPOINT [ "python3" ]

CMD [ "api.py" ]