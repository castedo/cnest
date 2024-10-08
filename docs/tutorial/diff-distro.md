Different Distro Tutorial
=========================

<!-- copybreak off -->


Objective
---------

You will create a container using the [`create-cnest` Bash
script](https://github.com/castedo/cnest/tree/main/bin/create-cnest) that demonstrates:

* using a Linux distro that is different from your host system (unless you're on Ubuntu Jammy),
* being isolated from the host system, and
* having multiple concurrent interactive shell sessions in the same container.


Prerequisites
-------------

* Linux (tested on RHEL 9 and Fedora 40, but some other distros should work)
* [Podman](../podman.md) 4.4+ (`docker` might work as well)
* [`create-cnest` and `cnest`](../install.md)


Steps
-----


### 1. Create an Ubuntu container

```
[castedo@onyx ~]$ create-cnest docker.io/library/ubuntu:jammy
Trying to pull docker.io/library/ubuntu:jammy...
...
...
...
+ podman run --detach --cidfile=/tmp/tmp.88vzKkjlUb --userns=keep-id:uid=48222,gid=48222 --init --user=root ubuntu:jammy sleep inf
333e015f56a7bbbf11d9f653e57bcee46713c2b8efe71f32fb880a4dfadb4be9
adoring_franklin
```

The last line printed is the name of the newly created container.
Since we didn't specify a name, `podman` has automatically generated the name
`adoring_franklin`.


### 2. Enter the container

```
[castedo@onyx ~]$ cnest adoring_franklin
adoring_franklin
'/home/castedo' is a different directory in the container
(📦adoring_franklin)castedo@333e015f56a7:~$ pwd
/home/castedo
(📦adoring_franklin)castedo@333e015f56a7:~$ ls -la
total 12
drwxr-xr-x. 2 castedo castedo   57 Sep 11 14:07 .
drwxr-xr-x. 1 root    root      21 Oct  7 19:48 ..
-rw-r--r--. 1 castedo castedo  220 Jan  6  2022 .bash_logout
-rw-r--r--. 1 castedo castedo 3771 Jan  6  2022 .bashrc
-rw-r--r--. 1 castedo castedo  807 Jan  6  2022 .profile
(📦adoring_franklin)castedo@333e015f56a7:~$ 
```

You've entered your newly created container.
You can see that your home directory inside the container is different
from your home directory on the host system.


### 3. Run `ps` and `top`

Now, we'll look at all the processes running in your new container.

```
(📦adoring_franklin)castedo@333e015f56a7:~$ ps -efH
UID          PID    PPID  C STIME TTY          TIME CMD
castedo        5       0  0 19:48 pts/0    00:00:00 /bin/bash --login
castedo       15       5  0 20:14 pts/0    00:00:00   ps -efH
root           1       0  0 19:48 ?        00:00:00 /run/podman-init -- sleep inf
root           2       1  0 19:48 ?        00:00:00   sleep inf
(📦adoring_franklin)castedo@333e015f56a7:~$ top
```

`ps -e` lists all the processes. But, since you are in an isolated container, only a
few are visible.
The "root" user in this container is not the *real* root of your host system.
Let's run `top` to see live updates to the process list.

```
(📦adoring_franklin)castedo@333e015f56a7:~$ top
```

You will now see `top` running and showing an ongoing update of all the processes.
Note the PID (process ID) of `top` itself.
The next step will assume the PID is `38`,
but you should use the actual PID you see reported by `top`.


### 3. Kill `top` from a second session

Now, open a new second terminal window and enter the container as a second session.

```
[castedo@onyx ~]$ cnest adoring_franklin
'/home/castedo' is a different directory in the container
(📦adoring_franklin)castedo@333e015f56a7:~$ 
```

Notice that a new `bash` process is reported by `top` in the first terminal window.

Assuming the PID (process ID) for `top` is `38`, let's kill it and then exit this second
session.

```
(📦adoring_franklin)castedo@333e015f56a7:~$ kill 38
(📦adoring_franklin)castedo@333e015f56a7:~$ exit
logout
```

We now see that the `top` process in the first session has been terminated.

<!-- copybreak on -->

### 4. Delete the container

Now that we've observed this container is too isolated,
we'll exit the remaining session and delete the container.

```
(📦adoring_franklin)castedo@333e015f56a7:~$ exit
logout
adoring_franklin
[castedo@onyx ~]$ podman rm adoring_franklin 
adoring_franklin
[castedo@onyx ~]$ 
```


### Conclusion

You've created a container using the [`create-cnest` Bash
script](https://github.com/castedo/cnest/tree/main/bin/create-cnest) and seen that this
container:

* runs Ubuntu Jammy, even if your host distro is not,
* is so isolated it's essentially useless, and
* can be entered through multiple interactive concurrent shell sessions.
