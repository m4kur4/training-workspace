FROM ubuntu:20.04

# 日本語化
RUN apt-get update \
  && apt-get install -y locales \ 
  && apt-get install -y wget \
  && locale-gen ja_JP.UTF-8 \
  && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc