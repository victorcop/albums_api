# specify the image you want to use build docker image

FROM python

# Maintainer name to let people know who made this image.

MAINTAINER Kartik <victorcop90@gmail.com>

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python setup.py