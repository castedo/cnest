FROM registry.fedoraproject.org/fedora:32

RUN yum -y update

RUN yum -y install glx-utils mesa-dri-drivers

RUN yum -y install alsa-plugins-pulseaudio

RUN yum -y install libcanberra-gtk3 PackageKit-gtk3-module

COPY google-chrome-81.0.4044.138-x86_64.rpm google-chrome.rpm
RUN yum -y install google-chrome.rpm

COPY cnest-entry /usr/bin

RUN yum clean metadata

