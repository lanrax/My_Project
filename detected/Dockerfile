FROM  nvidia/cuda:11.1.1-cudnn8-runtime-ubuntu20.04
MAINTAINER shaoyufei
WORKDIR /root
USER root
COPY ./modelfire /root/modelfire 
COPY ./modelfire_infrared /root/modelfire_infrared
COPY ./modelperson /root/modelperson
COPY ./modelperson_infrared /root/modelperson_infrared
COPY ./requirements.txt /root
COPY ./Arial.ttf /root/.config/Ultralytics/Arial.ttf
COPY ./yolov5-master  /home/hadoop/detectproject/yolov5-master
RUN apt update \
    && apt install -y python3-pip\
    && pip3 install -r /root/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
#RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata \
#    && sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
#    && apt-get clean \
#    && apt-get update \
#    && apt install -y python3-pip python3-dev build-essential python3-dev libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev \
#    && pip3 install --upgrade pip \
#ARG workdir=/root
#WORKDIR ${workdir}
#ENV TZ="Asia/Shanghai"
#RUN pip3 install -r /root/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 

