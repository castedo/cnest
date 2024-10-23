ARG PODMAN_IMG
FROM $PODMAN_IMG
ARG RPM=cnest

RUN dnf -y install 'dnf-command(copr)'
RUN dnf -y copr enable castedo/cnest
RUN dnf -y install $RPM
