Tools in the `cnest` package
============================

Primary tools:

* `cnest` for entering [nest containers](what-are-nest-containers.md)
* `create-nest` for creating [nest containers](what-are-nest-containers.md)
* `cnestify` for creating images with enhanced functionality enabled by `cnest`
  and `create-nest`


cnest
-----

`cnest` is a simple script for invoking
`podman exec/start/stop` with some extra niceties:

* unlike `podman exec`, you can omit the command to exec and it will default to
  executing either the command `/bin/bash --login`
* you can type a container name without a version suffix (e.g. type "webdev"
  and it guesses you want a container named "webdev-5")
* will stop the container if there are no more podman exec sessions (of which
  cnest sessions are one case)
* will automatically keep you in your current directory if
  your current directory is also shared with the nest container
* look at the podman exec arguments in
  [the script](https://github.com/castedo/cnest/blob/main/bin/cnest)
  for the rest of the niceties


### Container requirements

The `cnest` script can be used with any container that

* will run in the background after `podman start`
* has `/bin/bash` available to execute

A container does not have to be created with `create-nest`.


create-nest
-----------

`create-nest` is for creating a container. It's mostly just a wrapper around
`podman create`.
A permissions profile must be given to specify what `podman create` options to
add, such as home directories to share.

Optionally, if the image has the following scripts, they will be run **in
the new container** upon creation:

* /opt/nestkit/boostuser (run as root, username passed as parameter)
* /opt/nestkit/userinit (run as the user)

### Requirements for images pulled from repositories

* `sleep inf` is valid commmand to run


cnestify
--------

`cnestify` builds an enhanced image to be used for creating nest containers.
The image can start from a `Dockerfile` or you can just specify an image to
start with.

Some of the features enables by `cnestify` are:

* add a symbol to the prompt inside the container
* add groups to the user inside the container
* hook in a /usr/bin/cnest-entry script to be run by `cnest`
* override what `/etc/profile.d/` scripts should be added

Run `cnestify` or look at one of the How-to guides for more details on how to
use.
