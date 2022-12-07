# FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04
FROM nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    software-properties-common tzdata \
    &&  ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    &&  apt-get clean \
    &&  rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get -y install python3.9 python3.9-distutils python3-pip git \
    unzip libgl1-mesa-dev cmake python3.9-dev libpng-dev libfreetype-dev \
    wget ffmpeg
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
RUN python3.9 -m pip install -U pip wheel setuptools
COPY requirements.txt ./requirements.txt
# RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
RUN pip install --no-cache-dir -r requirements.txt
