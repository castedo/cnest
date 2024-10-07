Limited Access Tutorial
=======================

Objective
---------

You will create a container with limited access to your host environment using the
[`create-cnest` Bash
script](https://github.com/castedo/cnest/tree/main/bin/create-cnest).


Prerequisites
-------------

* [The previous tutorial](diff-distro.md)

Steps
-----


### 1. Create a shared directory

In contrast to [the previous tutorial](diff-distro.md), we will now
give a container access to a home subdirectory named `shr`.

```
[castedo@onyx ~]$ mkdir shr
[castedo@onyx shr]$ cd shr
[castedo@onyx shr]$ echo hello > world.txt
```

### 2. Create a Fedora container

We'll choose a different distro from [the previous tutorial](diff-distro.md).
In addition to sharing a subdirectory, we will share the network with the host
environment. There are many capabilities that are enabled by sharing the network,
including some GUI applications launching properly. 

```
[castedo@onyx shr]$ create-cnest registry.fedoraproject.org/fedora:40 \
  --volume=$HOME/shr:$HOME/shr \
  --network=host \
  --name fedy
Trying to pull registry.fedoraproject.org/fedora:40...
...
...
...
+ podman run --detach --cidfile=/tmp/tmp.qvnrK93NLn --userns=keep-id:uid=48222,gid=48222 --init --user=root -v /home/castedo/shr:/home/castedo/shr --name fedy fedora:40 sleep inf
25324f640c17b014d52ff2b307764514247392d3dbf150c409aa641527b0ab5b
fedy
```

We've also given this container a name. All of the options added are, in fact, Podman
options that are simply being passed through to `podman run`.

### 3. Enter the container

!!! tip
    If you've installed the RPM package and/or Bash completion script, then you can use
    tab completion to quickly enter a container name.

```
[castedo@onyx shr]$ pwd
/home/castedo/shr
[castedo@onyx shr]$ cnest fedy
fedy
📦fedy[castedo@onyx shr]$ pwd
/home/castedo/shr
```

Notice that you were in the `shr` subdirectory in the host environment and then stayed
in the same subdirectory when you entered the container. This is a feature of `cnest`
for directories that are shared with the same file path between the container and host.

```
📦fedy[castedo@88cec93f3679 shr]$ curl http://cows.rest/api/cow?say=moonix > moo.txt
📦fedy[castedo@88cec93f3679 shr]$ ls -l
total 4
-rw-r--r--. 1 castedo castedo 155 Oct  7 18:18 moo.txt
📦fedy[castedo@onyx shr]$ exit
logout
fedy
[castedo@onyx shr]$ ls -l
total 4
-rw-r--r--. 1 castedo castedo 155 Oct  7 18:18 moo.txt
[castedo@onyx shr]$ cat moo.txt
 ________
< moonix >
 --------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

[castedo@onyx shr]$ 
```
