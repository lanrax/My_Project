FROM  python:3.8.10
MAINTAINER shaoyufei
ENV PYTHONUNBUFFERED 1
RUN mkdir /root/web
COPY ./manage.py  /root/web/
COPY ./eyedetected  /root/web/eyedetected
COPY ./gunicorn.conf.py  /root/web/
COPY ./requirements.txt /root/web/
ARG workdir=/root/web/
WORKDIR ${workdir}
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

