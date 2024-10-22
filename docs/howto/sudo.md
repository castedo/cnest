How to Enable Sudo in a Container
=================================

Rather than running commands from the host system such as
```
podman exec $CONTAINER dnf --yes install
```
or
```
podman exec $CONTAINER apt-get --yes install
```
to install software inside the container, some users might prefer to run
```
sudo dnf install
```
or
```
sudo apt-get install
```

This how-to guide will show you how to enable this.


Steps
-----

### 1. Make sure `sudo` is installed in the container

If your base distribution image does not include sudo, you will need to execute
```
podman exec $CONTAINER apt-get --yes install sudo
```
or a similar command.


### 2. Make sure your user in the container has Sudo rights

On most distros, you just need to add a user to either the `wheel` group, on Fedora-based distros,
or `sudo` on Debian-based distros.

```
podman exec $CONTAINER usermod --append --groups wheel $USER
```
or
```
podman exec $CONTAINER usermod --append --groups sudo $USER
```

### 3. Optional: enable a log of sudo commands

When updating a Containerfile (Dockerfile) to include newly added software, it can be
convenient to look back and figure out what changes were made to a container's system.

A sudo log provides a convenient mechanism to see what system changes were made via
sudo.

On most distros, placing a file in `/etc/sudoers.d/' (with a filename
without periods!) and the contents
```
Defaults logfile=/var/log/sudo.log
```
will enable a log to be recorded in `/var/log` in the container.

This can be accomplished in a variety of ways. A good method is to place the line
```
RUN echo Defaults logfile=/var/log/sudo.log > /etc/sudoers.d/sudo-log-file
```
in a `Containerfile` for building the image you use to create your container.
