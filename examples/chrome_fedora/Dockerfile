FROM docker.io/fedora:32

RUN yum -y update

RUN yum -y install icedtea-web

COPY google-chrome-81.0.4044.138-x86_64.rpm google-chrome.rpm
RUN yum -y install google-chrome.rpm

RUN yum -y install libglvnd-glx

RUN yum -y install mesa-dri-drivers

COPY cnest-entry /usr/bin

RUN yum clean metadata

