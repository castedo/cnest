FROM registry.access.redhat.com/ubi8:8.2
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
# or Fedora instead of RHEL8+EPEL
# FROM registry.fedoraproject.org/fedora:32

RUN yum -y update

RUN yum -y install glx-utils mesa-dri-drivers

RUN yum -y install alsa-plugins-pulseaudio

RUN yum -y install chromium

COPY cnest-entry /usr/bin

RUN yum clean metadata

