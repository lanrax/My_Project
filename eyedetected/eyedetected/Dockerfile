FROM  python:3.8.10
MAINTAINER zqq
ENV PYTHONUNBUFFERED 1
RUN mkdir /root/web
COPY ./manage.py  /root/web/
COPY ./eyedetected  /root/web/eyedetected
COPY ./pic  /root/web/pic
COPY ./gunicorn.conf.py  /root/web/
COPY ./requirements.txt /root/web/
ARG workdir=/root/web/
WORKDIR ${workdir}
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list;
RUN apt-get update --fix-missing && apt-get install -y libgl1-mesa-glx --fix-missing
