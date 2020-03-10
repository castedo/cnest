FROM docker.io/fedora:31

RUN yum -y update

RUN yum -y install icedtea-web

COPY google-chrome-78.0.3904.108-x86_64.rpm google-chrome.rpm
RUN yum -y install google-chrome.rpm

COPY cnest-entry /usr/bin

RUN yum clean metadata

