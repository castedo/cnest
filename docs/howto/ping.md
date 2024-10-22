How to Enable Ping in a Container
=================================

This guide will show you how to enable ping to work in a container.

Prerequisites
-------------

Ensure you are set up to create a container,
such as the setup demonstrated in the [Start tutorial](../tutorial/start.md).


Steps
-----

### 1. Add the Linux capability needed by `ping`

On the command line for `create-cnest` (or `podman create` or `podman run`), add the option:

```
--cap-add=NET_RAW
```


### 2. Set the required Linux capability of the `ping` binary file

```
podman exec --user=root $CONTAINER setcap cap_net_raw+p /usr/bin/ping
```
where `$CONTAINER` is your container name or ID.
