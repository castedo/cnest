# command line prompting

When running an interactive shell session inside a container, it is a useful to
know the contained **environment** from the command line prompt.
You might prefer to see the actual container name **or** maybe just an alias
for the container's image.

The [cnest](../cnest) script passes both environment variables described below
(for Debian and Red Hat based distros).

## On Debian based distros

Debian already has a standard mechanism for this:

* the `debian_chroot` environment variable
* the `/etc/debian_chroot` file

So if you want to know your contained environment is `foobar` you can
do any of:

* `RUN echo foobar > /etc/debian_chroot` in a Dockerfile
* `podman exec thecontainer /bin/bash -c 'echo foobar > /etc/debian_chroot'`
* `podman exec -it --env debian_chroot=foobar /bin/bash`


## On Red Hat based distros

To enable the similar `debian_chroot` functionality on a Red Hat based distro,
you can use the [osvirtaliasprompt.sh](osvirtaliasprompt.sh) script in this folder.

Use it by either of:

* `COPY osvirtaliasprompt.sh /etc/profile.d/` in a Dockerfile
* `podman cp osvirtaliasprompt.sh thecontainer:/etc/profile.d/`

Then to set the alias to `foobar` for an image or container do any of:

* `RUN echo foobar > /etc/osvirtalias` in a Dockerfile
* `podman exec thecontainer /bin/bash -c 'echo foobar > /etc/osvirtalias'`
* `podman exec -it --env OSVIRTALIAS=foobar /bin/bash`

