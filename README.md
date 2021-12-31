cnest & create-nest
===================
<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Nest_-_Bird_%28PSF%29.png/260px-Nest_-_Bird_%28PSF%29.png" alt="Bird Nest">

Simple scripts for personal (rootless) persistent parallel containers designed
to be:

* personal: with rootless podman into containers as same user
* persistent: with mutable "pet" containers where you can interactively run yum,
  apt-get, change settings, etc... in containers you don't want automatically
  deleted
* parallel: with multiple containers that all persist and are invoked by
  identifying a container name (pattern)


cnest
-----

[cnest](bin/cnest) is a simple script for invoking
`podman exec` with some extra niceties:

* unlike `podman exec`, you can omit the command to exec and it will default to
  executing either the command
  * /usr/bin/cnest-entry in the container if it exists OR
  * /bin/bash --login
* the container's command line prompt will report the container name if your
  image or container has been setup as documented in
  [prompt/](prompt/).
* if optional [guess-container](bin/guess-container) is installed, you can type a
  container name without a version suffix (e.g. type "webdev" and it guesses
  you want a container named "webdev-5")
* look at the podman exec arguments in the script for the rest of the niceties

### Container requirements

The [cnest](bin/cnest) script can be used with any container that

* will run in the background after `podman start`
* has either `/bin/bash` or `/usr/bin/cnest-entry` available to execute

A container does not have to created with [create-nest](bin/create-nest).


create-nest
-----------

The script [create-nest](bin/create-nest) is for creating "nests", that is
containers created from a local-only personalized "nest" container image.

A profile is specified when creating a nest. A profile file defines:

* from which container image repository to customize a local "nest" image and container

* what `podman create` options to add, such as home directories to share

### Requirements for images pulled from repositories

* `sleep +Inf` is valid commmand to run
* either `useradd` is installed or `/usr/sbin/cnest-user-setup` exists


How to use
----------

### Install

If you use a RHEL 8 based distro like me, then you can

```
yum copr enable castedo/cnest
yum install cnest
```

Contact me if you want a package for another distro.

### Configure profiles

You need to add profiles into either `/etc/cnest/profiles/` or
`~/.config/cnest/profiles/`.

An example profile is [development](config/profiles/development).
A profile is just a shell script that will be sourced by `create-nest` to
determine what OSI repository to pull images from and what permissions and
capabilities to expose to a created nest container.

Once you have profiles confidered you can do

```
create-nest
```
to list available profiles, or

```
create-nest some_profile
```
to list available OSI image names, or

```
creat-nest some_profile some_name
```
to create a nest container from image `some_name` and name the container the
same, or

```
creat-nest some_profile some_name a_diff_name
```
to name the container `a_diff_name`.


Similar Tools
-------------

These scripts are inspired by
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


Old Examples
------------

See [profiles](profiles/) for example profile files and
[the default configuration file](config/default.env).

Below are some old examples that probably still work, but I haven't tested them
in a while.

[Example Dockerfile, image building, and container creating scripts](examples/)
for containerizing:

* [Chromium on RHEL/Fedora (using PulseAudio/WebCam)](examples/chromium)
* [Google Chrome on Fedora (using PulseAudio/WebCam)](examples/chrome_fedora)
* [Google Chrome on Ubuntu (using PulseAudio/WebCam)](examples/chrome_ubuntu/)
* [PulseAudio Test](examples/pulseaudio-test/)
* [non-X11 Wayland GNOME Calculator](examples/wayland-test)

### Desktop Menu Item/Icon Installation

For adding desktop menu item/icons, see the
[install-desktop-menu script in the Chromium Example](examples/chromium/install-desktop-menu).

