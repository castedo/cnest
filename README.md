cnest & create-nest
===================
<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Nest_-_Bird_%28PSF%29.png/260px-Nest_-_Bird_%28PSF%29.png" alt="Bird Nest">

Simple scripts for personal (rootless) persistent parallel containers designed
to be run:

* personal: with rootless podman into containers as same user
* persistent: with mutable "pet" containers where you can interactively run yum,
  apt-get, change settings, etc... in containers you don't want automatically
  deleted
* parallel: with multiple containers that all persist and will be invoked by
  identifying a container name (pattern)


cnest
-----

The script [cnest](bin/cnest) is just a simple script for invoking
`podman exec` with some extra niceties:

* if optional [guess-container](bin/guess-container) is installed, you can type a
  container name without a version suffix (e.g. type "webdev" and it guesses
  you want a container named "webdev-5")
* the container's command line prompt will report the container name if your
  image or container has been setup as documented in
  [prompt/](prompt/README.md).
* unlike `podman exec`, you can omit the command to exec and it will default to
  executing either the command
  * /usr/bin/cnest-entry in the container if it exists OR
  * /bin/bash --login
* look at the podman exec arguments in the script for the rest of the niceties


create-nest
-----------

The script [create-nest](bin/create-nest) is for creating "nests", that is
containers created from a local-only personalized container image.

A profile is specified when creating a nest. A profile file defines:

* from which container image repository to customize a local "nest" image and container

* what `podman create` options to add, such as home directories to share

As an example, if you run
```
create-nest browser chromer-11 chrome
```
then the default `browser` profile will be used. It will pull the image with
tag `chromer-11` from repository `docker.io/castedo/nests` and the custom
customize it for the current user. A container named `chrome` will be created.
Then
```
cnest chrome
```
will launch Chrome on Feodra in a container with the `~/Downloads` folder shared
with the host.

Profiles are determined by trivial shell files.
Make your own profile files or tweak the default ones.
See [examples](examples/) for examples and usage.


Desktop Menu Item/Icon Installation
-----------------------------------

For adding desktop menu item/icons, see the
[install-desktop-menu script in the Chromium Example](examples/chromium/install-desktop-menu).


Examples
--------

[Example Dockerfile, image building, and container creating scripts](examples/)
for containerizing:

* [PulseAudio Test](examples/pulseaudio-test/)
* [non-X11 Wayland GNOME Calculator](examples/wayland-test)
* [Chromium on RHEL/Fedora (using PulseAudio and WebCam)](examples/chromium)
* [Google Chrome on Fedora (using PulseAudio)](examples/chrome_fedora)
* [Google Chrome on Ubuntu](examples/chrome_ubuntu/)


Similar Tools
-------------

These scripts are inspired by
[Fedora Silverblue Toolbox](https://github.com/containers/toolbox).
But the files in this cnest repository:
* serve a slightly different purpose
* are decoupled so that they can be used, or not used, independently
* are simply enough to merely serve as code examples, if not used as-is

Also kind of similar is [podbox](https://github.com/DimaZirix/podbox)
"Container sandbox for GUI applications" with some nice features for working
with contained GUI applications.

Before attemping to containerize a GUI app, check to see if a [flatpak](https://flatpak.org/)
is available. An GUI desktop application that has already been flatpak'ed
will probably work better and more seamlessly than implementing a new container.
