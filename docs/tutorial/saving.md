Saving Personalizations Tutorial
================================

Objective
---------

In this tutorial, you will learn how to save container creation options and software
installation choices you make. These will be saved in a Base script and a Containerfile
(Dockerfile), respectively.
With these files, you can quickly recreate your personalized, persistent, multisession
container for the long-term.


Prerequisites
-------------

* The [start tutorial](start.md)


Steps
-----

### 1. Save installation commands for the long-term

Once you've determined that recently added software is working and you've decided
to use it long term, you'll want to save the installation commands in a
`Containerfile` (also known as `Dockerfile`).

For each `podman exec` command that you have run to alter the container, you should add a
corresponding `RUN` line in your Containerfile.

```
[pat@laptop ~]$ cat > Containerfile
FROM docker.io/ubuntu:jammy
RUN apt-get update
RUN apt-get install --yes cowsay
^D
[pat@laptop ~]$ 
```

The `^D` represents pressing the CTRL-D key.


### 2. Create a personalized container image

```
[pat@laptop ~]$ podman build --tag=moonix .
STEP 1/3: FROM docker.io/ubuntu:jammy
STEP 2/3: RUN apt-get update
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
...
Setting up cowsay (3.03+dfsg2-8) ...
Processing triggers for libc-bin (2.35-0ubuntu3.8) ...
COMMIT moonix
--> bd8fda2a5fa5
Successfully tagged localhost/moonix:latest
bd8fda2a5fa5fd575707bc0b081bbd9d451c760bd9bf8c83a803ceed266ee353
[pat@laptop ~]$ podman images
REPOSITORY                                          TAG          IMAGE ID      CREATED         SIZE
localhost/moonix                                    latest       bd8fda2a5fa5  46 seconds ago  186 MB
docker.io/library/ubuntu                            jammy        97271d29cb79  3 weeks ago     161 MB
```


### 3. Save a script

Now that you've recorded what software you want in future container recreations,
you also want to record the container creation options you've used with `create-cnest` (and thus `podman`).
We will record this in a personal Bash script file.

```
[pat@laptop ~]$ cat > create-mybox.sh
create-cnest localhost/moonix --network=host -v=$HOME/shr:$HOME/shr --name=mybox
^D
[pat@laptop ~]$ 
```

### 4. Recreate your container in the future

In the future, you can recreate your container using your personal Bash script.

```
[pat@laptop ~]$ bash create-mybox.sh
+ podman run --detach --cidfile=/tmp/tmp.WzVNrGB1iq --userns=keep-id:uid=48222,gid=48222 --init --user=root --network=host -v=/home/pat/shr:/home/pat/shr --name=mybox mynix sleep inf
022d2bceb4f6f8a4fb891e5c346d6553159439603fcba43840902bda921c7af8
mybox
[pat@laptop ~]$ 
```

You can use your cleanly recreated container just like the previous one.

```
[pat@laptop ~]$ cnest mybox
mybox
'/home/pat' is a different directory in the container
📦mybox[pat@laptop ~]$ cowsay My Box!
 __________
< My Box! >
 ----------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
📦mybox[pat@laptop ~]$ 
```


### Conclusion

You've now learned how to save the Podman creation options and software installations
of your choice.
