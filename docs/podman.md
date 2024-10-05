Podman
======

To follow this guide, you need to have [Podman](https://podman.io) installed.

!!! note
    You can probably use `docker` instead of `podman`.  However, the author recommends
    using `podman`.  Podman can run rootless containers, which do not require root
    privileges and do not run through a daemon process.

If you want to run an application that is available as an
[OCI](https://opencontainers.org/) (Docker) container, you most likely want to run it as
a temporary container and not a persistent container.
If this is your objective, jump to the section on [temporary
containers](temp-containers.md).

On the other hand, if you want to work in an interactive shell environment with a
personalized choice of Linux distribution and installed software packages, a persistent
container will be a convenient choice.
You will have the option to quickly try out and install software in an isolated
environment and have that environment persist even after rebooting your system.
