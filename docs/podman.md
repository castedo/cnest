Podman
======

To follow this guide, you need to have [Podman](https://podman.io) installed.

!!! tip
    If you want to run an application that is available as an
    [OCI](https://opencontainers.org/) (Docker) container image,
    you probably want to run it in a temporary container and not a personalized
    persistent multisession container. If running a containerized application is your
    objective, jump to the section on [temporary containers](temp-containers.md).

!!! note
    You can probably use `docker` instead of `podman`.  However, the author recommends
    using `podman`.  Podman can run rootless containers, which do not require root
    privileges and do not run through a daemon process.


Once you have Podman installed, you can use simple wrapper scripts such as:

* [`create-cnest`](https://github.com/castedo/cnest/tree/main/bin/create-cnest)
  to create persistent multisession containers and then
* [`cnest`](https://github.com/castedo/cnest/tree/main/bin/cnest)
  to run interactive shell sessions inside them.

These wrapper scripts are not intended to eliminate the need to call `podman` directly.
Below are notable `podman` commands that you will still want to use in addition to
wrapper scripts.

To get started with this guide,
[install `create-cnest` and `cnest`](install.md).


### Notable podman commands

| Command           | Description                             |
| ----------------- | --------------------------------------- |
| `podman images`   | List container images in local storage  |
| `podman rmi`      | Remove a locally stored container image |
| `podman ps --all` | List all containers                     |
| `podman rename`   | Rename a container                      |
| `podman rm`       | Remove a container                      |
| `podman start && podman exec` | Run a command in a started container |
