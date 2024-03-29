What are nest containers?
=========================

Nest containers are [OCI](https://opencontainers.org/) containers used as
contained user environments for interactive shell sessions.
Sometimes they are referred to as "pet" Docker containers.
Nest containers are similar to [flatpaks](https://flatpak.org/) and
[conda](https://conda.io/) environments. But flatpaks are optimized for
[GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) desktop
applications.
Conda is optimized for portable software packages running natively across
Windows, macOS and Linux.
In order to run on Windows and macOS, conda can not rely on [OS-level
virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization)
which is needed to run containers.

As OCI containers, nest containers have three key features of being:

1. personalized
1. persistent
1. controlled

## Personalized

Broadly distributed OCI container images generally are not personalized to
specific user accounts. Users who want to enter shell environment as the
same non-root user account want a user account in the container to match
the local user account of the hosting computer.

## Persistent

Containers are usually non-persistent and used for services running in the
background. But for interactive shell sessions, it is convenient to let
the contained file system persist across process termination and reboots,
by default.

For instance, a user can interactively experiment with running yum,
apt-get, and in general change the contained file system across process
terminations and reboots.

## Controlled

Like users of flatpaks, users of nest containers can have different
preferences for how much of the host system is shared with the contained
environment. For instance, users

* may want to share the entire home directory, or only parts of it
* may or may not want to share the network
* may or may not want to share access to X11, Wayland, audio, video
  cameras, etc...

In general, a nest containers provides users the granularity of control
similar to flatpak applications.

