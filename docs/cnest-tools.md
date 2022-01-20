Tools in the `cnest` package
============================

Primary tools:

* `cnest` for entering [nest containers](what-are-nest-containers.md)
* `create-nest` for creating [nest containers](what-are-nest-containers.md)
* `cnestify` for creating images with enhanced functionality enabled by `cnest`

Secondary tools:

* `create-nest-by-tag` is a simple helper wrapper script of crest-nest for
  choosing image and container names from tags in a single repository


cnest
-----

`cnest` is a simple script for invoking
`podman exec` with some extra niceties:

* unlike `podman exec`, you can omit the command to exec and it will default to
  executing either the command
  * /usr/bin/cnest-entry in the container if it exists OR
  * /bin/bash --login
* will automatically keep you in your currently directory if the container
  image has been enhanced with `cnestify` and your currently directory is
  also shared with the nest container with the same path.
* you can type a container name without a version suffix (e.g. type "webdev"
  and it guesses you want a container named "webdev-5")
* will stop the container if there are no more podman exec sessions (of which
  cnest sessions are one case)
* look at the podman exec arguments in the script for the rest of the niceties

### Container requirements

The `cnest` script can be used with any container that

* will run in the background after `podman start`
* has either `/bin/bash` or `/usr/bin/cnest-entry` available to execute

A container does not have to be created with `create-nest`.


create-nest
-----------

The script `create-nest` is for creating a container.
A permissions profile must be given to specify what `podman create` options to
add, such as home directories to share.

Optionally, if the image has the following scripts, they will be run **in
the new container** upon creation:

* /opt/nestkit/boostuser (run as root, username passed as parameter)
* /opt/nestkit/userinit (run as the user)

### Requirements for images pulled from repositories

* `sleep inf` is valid commmand to run


create-nest-by-tag
------------------

If you have many favorite images in one single repository
with tag names that can serve as container names, `create-nest-by-tag`
is convenient.

```
export CNEST_REPOSITORY=myfavrepo
create-nest-by-tag some_profile
```
to list available [OCI](https://opencontainers.org/) image tag names in `myfavrepo`, or

```
creat-nest-by-tag some_profile foo-2
```
to create a nest container from the image tagged `foo-2` and name the container
the same, or

```
creat-nest-by-tag some_profile foo-2 a_diff_name
```
to name the container `a_diff_name`.

