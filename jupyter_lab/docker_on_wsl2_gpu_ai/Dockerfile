FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

RUN apt-get update && apt-get install -y \
    software-properties-common tzdata git \
    &&  ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    &&  apt-get clean \
    &&  rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Tokyo
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get -y install python3.9 python3.9-distutils python3-pip
RUN python3.9 -m pip install -U pip wheel setuptools
COPY requirements.txt ./requirements.txt
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install --no-cache-dir -r requirements.txt
