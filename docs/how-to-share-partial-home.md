How to share only part of your home directory
=============================================


After [installation](install.md), you can
```text
[castedo@nasa ~]$ create-nest
Usage:
  create-nest
    to print list of available permission profiles.
  create-nest profile image_ref container_name
    to build nest container.
Permission profiles available from /home/castedo/.config/cnest/profiles:
only-downloads
[castedo@nasa ~]$ 
```
to see available permission profiles. If this is the first time
running `create-nest` then a profile `only-downloads` has been copied to
`~/.config/cnest/profiles` for convenienice.

```text
[castedo@nasa ~]$ mkdir -p ~/Downloads
[castedo@nasa ~]$ create-nest only-downloads debian mynest
+ podman create --userns=keep-id --name mynest --uts=private --hostname mynest.nasa.home --cgroups=enabled --pid=host --volume /home/castedo/Downloads:/home/castedo/Downloads debian sleep +Inf
c239882d78d3d069629557a5ee77207dfdca764bfce0c10f4229d50c87859983
+ podman cp mynest:/opt/nestkit -
[castedo@nasa ~]$ podman ps -a
CONTAINER ID  IMAGE                            COMMAND     CREATED         STATUS            PORTS       NAMES
7cf7c014f5e7  docker.io/castedo/share:rtd-4    sleep +Inf  11 minutes ago  Up 4 minutes ago              rtd-4
c239882d78d3  docker.io/library/debian:latest  sleep +Inf  31 seconds ago  Created                       mynest
[castedo@nasa ~]$ 
```
This creates a new container named `mynest` which is
highly isolated and only shares `~/Downloads` with the host.

To enter this new nest container do:
```text
[castedo@nasa ~]$ cnest mynest
mynest
castedo@mynest:/$ cd /home/castedo
castedo@mynest:/home/castedo$ ls -l
total 4
drwxr-xr-x. 4 castedo castedo 4096 Jan 13 22:15 Downloads
castedo@mynest:/home/castedo$ 
```
