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

Some of the features enables by `cnestify` are:

* add a symbol to the prompt inside the container
* add the user to the `sudo` or `wheel` group inside the container


### Requirements for images pulled from repositories

* `sleep inf` is valid commmand to run
