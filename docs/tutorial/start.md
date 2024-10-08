Start Tutorial
==============

Objective
---------

In this tutorial, you will explore the key features of containers created by the
[`create-cnest` Bash
script](https://github.com/pat/cnest/tree/main/bin/create-cnest), namely:

* a distro inside the container independent of the host,
* restricted access to the host environment,
* persistent changes to the container, and
* multiple concurrent sessions inside the container.


Prerequisites
-------------

* Linux (tested on RHEL 9 and Fedora 40, but some other distros should work)
* [Podman](../podman.md) 4.4+ (`docker` might work as well)
* [`create-cnest` and `cnest`](../install.md)


Steps
-----

### 1. Create a directory to share

We start by creating a directory we will share with the container.

```
[pat@laptop ~]$ mkdir shr
[pat@laptop shr]$ cd shr
[pat@laptop shr]$ echo hello > world.txt
```

### 2. Create an Ubuntu container

We create a new container and share the `~/shr` home subdirectory with it by
using the `-v`/`--volume` option of `podman`. Options for `create-cnest` are passed through to
`podman`.

```
[pat@laptop shr]$ create-cnest docker.io/ubuntu:jammy -v=$HOME/shr:$HOME/shr
+ podman run --detach --cidfile=/tmp/tmp.SyTuPuJz4I --userns=keep-id:uid=48222,gid=48222 --init --user=root -v=/home/pat/shr:/home/pat/shr docker.io/ubuntu:jammy sleep inf
Trying to pull docker.io/library/ubuntu:jammy...
...
...
...
999d068262033c69095fdc62152d993689f2c8c20d0733e223a1c2bd2b480899
zen_franklin
[pat@laptop shr]$ 
```

The last two lines printed are the ID and the name of the created container.
Since a name wasn't specified, `podman` automatically generated the name
`zen_franklin`.


### 3. Enter the container

!!! tip
    If you've installed the RPM package and/or Bash completion script, you can use
    tab completion to quickly enter a container name.

```
[pat@laptop shr]$ pwd
/home/pat/shr
[pat@laptop shr]$ cnest zen_franklin
zen_franklin
📦zen_franklin[pat@999d06826203 shr]$ pwd
/home/pat/shr
```

Notice that you were in the `shr` subdirectory in the host environment and then stayed
in the same subdirectory upon entering the container. This is a feature of `cnest`
for directories that are shared with the same file path between the container and host.

```
📦zen_franklin[pat@999d06826203 shr]$ hostname
999d06826203
📦zen_franklin[pat@999d06826203 shr]$ echo $CONTAINER_NAME
zen_franklin
```

By default, this container has a distinct network interface from the host,
since the `podman` option `--network=host` was not added.
Under the default setting, the localhost for the host environment and the localhost in the container are
different network destinations.
Thus, this container is isolated from host services like D-Bus and Wayland.


### 4. Explore the contained file system

```
📦zen_franklin[pat@999d06826203 shr]$ ls -l
total 4
-rw-r--r--. 1 pat pat 6 Oct  8 15:43 world.txt
📦zen_franklin[pat@999d06826203 shr]$ cat world.txt
hello
```

```
📦zen_franklin[pat@999d06826203 shr]$ cd ..
📦zen_franklin[pat@999d06826203 ~]$ ls -la
total 12
drwxr-xr-x. 2 pat pat   57 Sep 11 14:07 .
drwxr-xr-x. 1 root    root      21 Oct  7 19:48 ..
-rw-r--r--. 1 pat pat  220 Jan  6  2022 .bash_logout
-rw-r--r--. 1 pat pat 3771 Jan  6  2022 .bashrc
-rw-r--r--. 1 pat pat  807 Jan  6  2022 .profile
```

You can see that your home directory inside the container is different
from your home directory on the host system.


### 5. Run `ps` and `top`

Now, let's look at all the processes running in your new container.

```
(📦zen_franklin)pat@333e015f56a7:~$ ps -efH
UID          PID    PPID  C STIME TTY          TIME CMD
pat        5       0  0 19:48 pts/0    00:00:00 /bin/bash --login
pat       15       5  0 20:14 pts/0    00:00:00   ps -efH
root           1       0  0 19:48 ?        00:00:00 /run/podman-init -- sleep inf
root           2       1  0 19:48 ?        00:00:00   sleep inf
(📦zen_franklin)pat@333e015f56a7:~$ top
```

`ps -e` lists all the processes. But, since you are in an isolated container, only a
few are visible.
The "root" user in this container is not the *real* root of your host system.
Let's run `top` to see live updates of the process list.

```
(📦zen_franklin)pat@333e015f56a7:~$ top
```

You will now see `top` running and showing ongoing updates of all the processes.
Note the PID (process ID) of `top` itself.
The next step will assume the PID is `38`,
but you should use the actual PID you see reported by `top`.


### 6. Kill `top` from a second session

Now, open a new second terminal window and enter the container as a second session.

```
[pat@laptop ~]$ cnest zen_franklin
'/home/pat' is a different directory in the container
(📦zen_franklin)pat@333e015f56a7:~$ 
```

Notice that a new `bash` process is reported by `top` in the first terminal window.

Assuming the PID for `top` is `38`, let's kill it and then exit this second
session.

```
(📦zen_franklin)pat@333e015f56a7:~$ kill 38
(📦zen_franklin)pat@333e015f56a7:~$ exit
logout
[pat@laptop ~]$ 
```

We now see that the `top` process in the first session has been terminated.


### 7. Install software for the short-term

From the same second terminal window, we can install software as the "fake" root *inside
the container* while still having a session in your first terminal window.

```
[pat@laptop ~]$ podman exec zen_franklin apt-get update
Get:1 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
...
Fetched 34.4 MB in 3s (10.7 MB/s)
Reading package lists...
Building dependency tree...
Reading state information...
All packages are up to date.
[pat@laptop ~]$ podman exec zen_franklin apt-get install --yes cowsay
Reading package lists...
...
The following NEW packages will be installed:
  cowsay libgdbm-compat4 libgdbm6 libperl5.34 libtext-charwidth-perl netbase
  perl perl-modules-5.34
0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
Need to get 8110 kB of archives.
After this operation, 48.3 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 perl-modules-5.34 all 5.34.0-3ubuntu1.3 [2976 kB]
...
Setting up cowsay (3.03+dfsg2-8) ...
Processing triggers for libc-bin (2.35-0ubuntu3.8) ...
[pat@laptop ~]$ 
```

Returning to the first terminal window, you can now use this newly installed
essential piece of software.

```
(📦zen_franklin)pat@999d06826203:~$ /usr/games/cowsay moooonix
 __________
< moooonix >
 ----------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
(📦zen_franklin)pat@999d06826203:~$ 
```





### Conclusion

You've created a container using the [`create-cnest` Bash
script](https://github.com/pat/cnest/tree/main/bin/create-cnest) and seen that this
container:

* runs Ubuntu Jammy, even if your host distro is different,
* is isolated, only sharing part of your home directory,
* has extra software installed, and 
* can be entered through multiple interactive concurrent shell sessions.

Now that you have created a persistent multisession container, continue to the [next
tutorial on how to save personalizations of your container for easier re-use in the
future](saving.md).
