Tools in the `cnest` package
============================

Primary tools:

* `cnest` for entering persistent containers
* `create-cnest` for creating persistent containers

The `cnest` package includes bash auto-completions for both tools.

cnest
-----

`cnest` is a simple script for invoking
`podman exec/start/stop` with some extra niceties:

* Unlike `podman exec`, you can omit the command to exec, and it will default to
  executing either the command `/bin/bash --login`.
* It will stop the container if there are no more `podman exec` sessions (of which
  `cnest` sessions are one case).
* It will automatically keep you in your current directory if
  your current directory is also shared with the nest container.
* Look at the `podman exec` arguments in
  [the script](https://github.com/castedo/cnest/blob/main/bin/cnest)
  for the rest of the niceties.


### Container requirements for `cnest`

The `cnest` script can be used with any container that:

* Will run in the background after `podman start` (e.g., runs `sleep inf`).
* Has `/bin/bash` available to execute.

A container does not have to be created with `create-cnest`.


create-cnest
------------

`create-cnest` is for creating a container.
It's mostly just a wrapper around `podman run`.
A bonus feature enabled by `create-cnest` is adding a symbol and container name to the
prompt inside the container.


### Image requirements for `create-cnest`

* Mandatory POSIX commands: `cp`, `chown`, `chmod`, `mkdir`, `sleep`
* `bash`, `useradd`, and `groupadd` (widely included in most distros)
