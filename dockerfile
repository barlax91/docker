
FROM python:3

COPY . .

RUN apt-get update \
  && apt-get install -y python3-pip\
  && pip3 --no-cache-dir install --upgrade pip \
  && apt-get -y install vim

RUN pip install -r requirements.txt

CMD ["flask","--app","testf", "run", "--host=0.0.0.0"]