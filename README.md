[![Copr build status](https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/status_image/last_build.png)
](https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/)

cnest & create-nest
===================
<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Nest_-_Bird_%28PSF%29.png/260px-Nest_-_Bird_%28PSF%29.png" alt="Bird Nest">

[cnest](bin/cnest) is a simple wrapper script of podman for entering
[nest containers](docs/what-are-nest-containers.md).

[create-nest](bin/create-nest) is an increasingly not-so-simple script for
creating [nest containers](docs/what-are-nest-containers.md).

[What are nest containers?](docs/what-are-nest-containers.md)


How to use
----------

After [installation](docs/install.md), you can
```
create-nest
```
to see available profiles. One profile named `isolated-docker-library` is
pre-installed and can be used as such:
```
mkdir -p ~/Downloads
create-nest isolated-docker-library debian mynest
```
This creates a new personalized container named `mynest` which is
highly isolated and only shares `~/Downloads` with the host.
Instead of `debian` you can choose another distro under `docker.io/library`.

To enter this new nest container do:
```
cnest mynest
```


Profiles
--------

A profile determines what OSI repository to pull images from and what
permissions, resources and capabilities to expose to a created nest container.
In the cnest 1.x version series, a profile is just a shell script that will
be sourced by `create-nest`. But this is a proof-of-concept hack and cnest
version 2.0 will switch to some more sane format.

You can add custom profiles to `~/.config/cnest/profiles/`.
See [isolated-docker-library](config/profiles/isolated-docker-library)
for the pre-installed bare-bones example.

Once you have profiles confidered you can do

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



cnest
-----

[cnest](bin/cnest) is a simple script for invoking
`podman exec` with some extra niceties:

* unlike `podman exec`, you can omit the command to exec and it will default to
  executing either the command
  * /usr/bin/cnest-entry in the container if it exists OR
  * /bin/bash --login
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

