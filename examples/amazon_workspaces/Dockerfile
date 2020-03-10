FROM docker.io/ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install gnupg2 ca-certificates

# https://clients.amazonworkspaces.com/linux-install.html
COPY ADB332E7.asc .
RUN apt-key add ADB332E7.asc
RUN echo "deb [arch=amd64] https://d3nt0h4h6pmmc4.cloudfront.net/ubuntu bionic main" > /etc/apt/sources.list.d/amazon-workspaces-clients.list 
RUN apt-get -y update

RUN apt-get -y install workspacesclient

COPY cnest-entry /usr/bin

RUN apt-get clean

