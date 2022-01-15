Other Tools
===========

The `cnest` package of tools was inspired by
[Fedora Silverblue Toolbox](https://github.com/containers/toolbox).
But the script files in this cnest repository:
* are for creating containers from many different images, especially of non-Fedora distros
* are for controlling what permissions and capabilities are given to nest containers
* are decoupled so that they can be used, or not used, independently
* are simply enough to merely serve as code examples, if not used as-is

A new and similar tool is [distrobox](https://github.com/89luca89/distrobox).
Unlike toolbox, and like cnest, distrobox is designed for lots of different
images from lots of different distros.
Unlike `cnest`, designed to be run from many distros, including distros
without `podman`.

Yet another similar tool is [podbox](https://github.com/DimaZirix/podbox)
"Container sandbox for GUI applications" with some nice features for working
with contained GUI applications.

Before attemping to containerize a GUI app, check to see if a [flatpak](https://flatpak.org/)
is available. A GUI desktop application that has already been flatpak'ed
will likely work better and more seamlessly than implementing a new container.

