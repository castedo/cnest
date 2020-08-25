cnest
=====
<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Nest_-_Bird_%28PSF%29.png/260px-Nest_-_Bird_%28PSF%29.png" alt="Bird Nest">

Simple scripts for personal (rootless) persistent parallel containers designed
to be run:

* personal: with rootless podman into containers as same user
* persistent: with mutable "pet" containers where you can interactively run yum,
  apt-get, change settings, etc... in containers you don't want automatically
  deleted
* parallel: with multiple containers that all persist and will be invoked by
  identifying a container name (pattern)

The main script here is [cnest](cnest). It's just a simple script for invoking
`podman exec` with some extra niceties:

* if optional [guess-container](guess-container) is installed, you can type a
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


Container Creation
------------------

There are lots of ways to create containers and `cnest` can work fine with them
as long as a user account has been created in the container.

The script [create-homey-nest](create-homey-nest) can be used to create "nest"
containers that are 'personalized' for the local non-root user. For more details
see below.

Two **older** scripts, [build-nest-image](build-nest-image) and [create-nest](create-nest),
can also used to create custom "nest" containers. See [examples](examples/) for usage.

### [create-homey-nest](create-homey-nest)

This script is merely one of many ways to create containers that can be run with `cnest`.
Some benefits of `create-homey-nest` is that the home directory inside the
container is:

* fully isolated by default
* initialized and setup per the distro
* only shares home directory files and subdirectories if explicitly specified
  by a user preference file

The script [create-homey-nest](create-homey-nest) will create a container that works well
with [cnest](cnest). A preferences file can specify two items:

* from which container image repository to customize a local "nest" image and container

* what home directory files and subdirectories should be mounted in the "nest" container

The preferences file can be specified on the command line or it can be placed at
`~/.config/cnest/homey-nest.yaml` to be used by default. Here is example file:

```
base_repository: docker.io/castedo/tskit-nests
home_mounts:
    - .ssh
    - shr
    - Dropbox
    - .vim
    - .vimrc
    - .gitconfig
    - .sudo_as_admin_successful
```

As an example, if you run
```
create-homey-nest ubuntu-20.04-mspdev
```
then a "nest" container called `ubuntu-20.04-mspdev` based on the image
`docker.io/castedo/tskit-nests:ubuntu-20.04-mspdev` is created and customized
for the current user. As part of the customization, the `home_mounts` will be
mounted inside the container. Then running
```
cnest ubuntu-20.04-mspdev
```
will enter the "nest" as the local non-root user with an isolated home directory
of only `home_mounts` shared outside the container.

#### Using a shorter container name

In this early version, the hacky way to achieve a shorter container name is
to do
```
podman tag localnests:old_long_name localnests:new_short_name
```
and then run
```
create-homey-nest new_short_name
```


Desktop Menu Item/Icon Installation
-----------------------------------

For adding desktop menu item/icons, see the
[install-desktop-menu script in the Chromium Example](examples/chromium/install-desktop-menu).


Examples
--------

[Example Dockerfile, image building, and container creating scripts](examples/)
for containerizing:

* [PulseAudio Test](examples/pulseaudio-test/)
* [Webcam and non-X11 Wayland GNOME Cheese](examples/cheese_wayland)
* [Chromium on RHEL/Fedora (using PulseAudio and WebCam)](examples/chromium)
* [Google Chrome on Fedora (using PulseAudio)](examples/chrome_fedora)
* [Google Chrome on Ubuntu](examples/chrome_ubuntu/)
* [Amazon Workspaces Client](examples/amazon_workspaces/)


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

