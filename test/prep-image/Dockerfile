FROM quay.io/podman/stable

RUN yum -y install 'dnf-command(copr)'
RUN yum -y copr enable castedo/cnest

USER podman
RUN podman pull docker.io/debian

USER root
