How to Enable a GUI
===================

This guide will show you how to allow programs within your container to access Wayland and/or X
Window, providing a limited Graphical User Interface (GUI).
Depending on your distribution and the needs of a GUI application,
access to Wayland and/or X Window might not provide the level of desktop integration
that you want.
For full desktop integration, consider [other solutions](../other-tools.md).

There are at least three options to give a container access to your host
windowing system.

Option 1: By Network
--------------------

On some distributions, sharing the network with the host enables access to Wayland
and/or X Window. For example, by adding the following options to `create-cnest` (or
`podman create` or `podman run`):

```
--network=host --uts=host --add-host=$HOSTNAME:127.0.0.1
```

Option 2: By Wayland
--------------------

If you're not sharing the host's network, or if that approach does not work,
on most distributions, you can add the following options
to enable Wayland access:

```
--volume=$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/$WAYLAND_DISPLAY
--env=XDG_RUNTIME_DIR=/tmp
--env=WAYLAND_DISPLAY=$WAYLAND_DISPLAY
```

Option 3: By X Window
---------------------

All major Linux distributions have transitioned from X Window to Wayland.
If you still want to use X Window,
the following option should enable it on most distributions:

```
--volume=/tmp/.X11-unix:/tmp/.X11-unix
```
