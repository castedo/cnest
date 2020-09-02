FROM registry.fedoraproject.org/fedora:32

RUN yum -y install pulseaudio-utils

COPY random.ogg /opt
COPY cnest-entry /usr/bin

RUN yum clean metadata

