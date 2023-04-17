FROM docker.io/bitnami/spark:3.1

USER root

# Install prerequisites
RUN apt-get update && apt-get install -y curl

RUN apt install -y ffmpeg

RUN pip3 install numpy
RUN pip3 install pydub
RUN pip3 install librosa