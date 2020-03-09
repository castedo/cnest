cnest
=====
<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Nest_-_Bird_%28PSF%29.png/260px-Nest_-_Bird_%28PSF%29.png" alt="Bird Nest">

Simple scripts for personal (rootless) persistent parallel containers designed
to be run with:

* personal: rootless podman into containers as same user
* persistent: mutable "pet" containers where you can interactively run yum,
  apt-get, change settings, etc... in containers you don't want automatically
  deleted
* parallel: multiple containers that all persist and will be invoked by
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


Similar Tools
-------------

These scripts are inspired by
[Fedora Silverblue Toolbox](https://github.com/containers/toolbox).
But the files in this cnest repository:
* serve a slightly different purpose
* are decoupled so that they can be used independently
* are simply enough to merely serve as code examples, if not used as is

