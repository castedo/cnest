How to share only part of your home directory
=============================================


After [installation](install.md), you can
```text
[castedo@hostop ~]$ create-cnest
Usage:
  [USER=user] create-cnest image [podman_create_options ...]

Locally stored images:
  quay.io/centos/centos:stream9
  docker.io/library/debian:latest
[castedo@hostop ~]$ 
```

```text
[castedo@hostop Downloads]$ create-cnest debian --name mynest -v .:$HOME/Downloads
+ podman create --cidfile=/tmp/tmp.iwKa5Jk8Ts --userns=keep-id --init --user=root --name mynest -v .:/home/castedo/Downloads debian sleep inf
95bcb24705340b6453067af1e527c7026379d022a2d05cede450a149fa5b1ed1
mynest
[castedo@hostop ~]$ podman ps -a
CONTAINER ID  IMAGE                            COMMAND     CREATED         STATUS            PORTS       NAMES
95bcb2470534  docker.io/library/debian:latest  sleep inf   31 seconds ago  Created                       mynest
```
This creates a new container named `mynest`, which is
highly isolated and only shares `~/Downloads` with the host.

To enter this new nest container, do:
```text
[castedo@hostop Downloads]$ cnest mynest
mynest
(📦mynest)castedo@95bcb2470534:~/Downloads$ ls -l 
total 10825920
-rw-r--r--. 1 castedo castedo 11085742080 Sep 24 15:08  rhel-9.4-x86_64-dvd.iso
(📦mynest)castedo@95bcb2470534:~/Downloads$ 
```

Notice that `cnest` preserved the current working directory when entering the new nest
container.
