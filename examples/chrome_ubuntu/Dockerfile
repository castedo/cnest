FROM docker.io/ubuntu:19.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install icedtea-netx

COPY google-chrome-80.0.3987.132-amd64.deb google-chrome.deb
RUN apt-get -y install ./google-chrome.deb

COPY cnest-entry /usr/bin
COPY cnest-user-setup /usr/bin

RUN apt-get clean

