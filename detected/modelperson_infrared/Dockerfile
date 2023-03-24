FROM  nvidia/cuda:11.1.1-cudnn8-runtime-ubuntu20.04
MAINTAINER shaoyufei
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt install -y python3-pip
RUN apt install ffmpeg libsm6 libxext6  -y
RUN apt install libgl1 -y
RUN apt-get update \
    && apt-get install -y tar git curl nano wget dialog net-tools build-essential \
    && apt-get install --no-install-recommends -y -q python3 python3-pip python3-dev \
    && apt-get install -y libxml2-dev libxslt-dev python-dev zlib1g-dev                                             
RUN apt-get install -y build-essential python3-dev libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev
RUN pip3 install --upgrade pip
RUN mkdir /root/modelperson
ARG workdir=/root/modelperson
WORKDIR ${workdir}
COPY ./person_infrared.py  /root/modelperson
COPY ./requirements.txt /root/modelperson
COPY ./yolov5-master  /home/hadoop/detectproject/yolov5-master
ENV TZ="Asia/Shanghai"
RUN pip3 install -r /root/modelperson/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 
CMD ["python3","/root/modelperson/person_infrared.py"]
#ENTRYPOINT ["python3", "fire.py"]

## shell脚本
##执行docker镜像生成命令
