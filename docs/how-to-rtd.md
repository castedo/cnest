How to create a nest container for Read the Docs
================================================

This documentation is built with [Read the Docs](https://readthedocs.org/).
Read the Docs shares OCI [container
images](https://hub.docker.com/r/readthedocs/build/) used on their servers to
build documents.
It would be nice to locally replicate the same build environment used by Read
the Docs.
Using the the Read the Docs container images as a base, the author of this
documentation has built and
shared an OCI image for the version of Linux, Python and extensions specificed
in the {download}`.readthedocs.yaml <../.readthedocs.yaml>` used to build
this documentation.

This how-to guide is split into two parts. In part A we see how to create and use a
nest container using the pre-built image. In part B we see
how to create an image to be shared, like the one used in part A.

Part A: Using an image to create a nest container
-------------------------------------------------

Imagine that Jane has this `cnest` documentation checked out locally at
`~/src/cnest`.  Running `create-nest` without parameters will print what
permission profiles are defined.

```text
[jane@laptop ~]$ create-nest
Usage:
  create-nest
    to print list of available permission profiles.
  create-nest profile image_ref container_name
    to build nest container.
Permission profiles available from /home/jane/.config/cnest/profiles:
only-downloads
[jane@laptop ~]$ 
```

Since Jane wants to use local files under `~/src`, she will adapt the
pre-installed `only-downloads` permission profile to another profile that
grants access to `~/src`.

```text
[jane@laptop ~]$ pushd ~/.config/cnest/profiles
~/.config/cnest/profiles ~
[jane@laptop profiles]$ cat only-downloads 
CREATE_OPTIONS="
    --volume $HOME/Downloads:$HOME/Downloads
"
[jane@laptop profiles]$ sed s/Downloads/src/g only-downloads > only-src 
[jane@laptop profiles]$ cat only-src 
CREATE_OPTIONS="
    --volume $HOME/src:$HOME/src
"
[jane@laptop profiles]$ popd
~
[jane@laptop ~]$ create-nest
Usage:
  create-nest
    to print list of available permission profiles.
  create-nest profile image_ref container_name
    to build nest container.
Permission profiles available from /home/jane/.config/cnest/profiles:
only-downloads  only-src
[jane@laptop ~]$ 
```

The author of this documentation has shared an OCI image at
`docker.io/castedo/share:rtd-4`.
Jane can now use her permission profile plus the shared image to create a nest
container. Jane will name the container `rtd-nest`.

```text
[jane@laptop ~]$ create-nest only-src docker.io/castedo/share:rtd-4 rtd-nest
+ podman create --userns=keep-id --name rtd-nest --uts=private --hostname rtd-nest.laptop.home --cgroups=enabled --pid=host --volume /home/jane/src:/home/jane/src docker.io/castedo/share:rtd-4 sleep +Inf
6c5a1c7e029f5aab77dae6a6d50b3207eca181f261eea63a5010a0a97d672af7
...
rtd-nest
[jane@laptop ~]$ 
```

A new nest container named `rtd-nest` has been created.
With her new nest container, she can use `cnest` to enter the nest and build
the documentation in her own directory `~/src/cnest/docs`.

```text
[jane@laptop ~]$ cd src/cnest/docs/
[jane@laptop docs]$ cnest rtd-nest
rtd-nest
(📓)jane@rtd-nest:~/src/cnest/docs$ make html
Running Sphinx v4.3.2
...
build succeeded, 1 warning.

The HTML pages are in _build/html.
(📓)jane@rtd-nest:~/src/cnest/docs$
```
Jane can now open `~/src/src/cnest/docs/_build/html/index.html` on her host
computer with whatever software she has installed outside the container.

Note a few nice features of what Jane accomplished:

* Jane's laptop runs on RHEL 8 but she's able to build the documentation on the
  Linux distro used by Read the Docs which is Ubuntu.
* By running the Read the Docs environment in a container, Jane has keep all
  the software dependencies needed by Read the Docs separate from her main
  computer environment.
* Entering the nest container with `cnest` was able to recognize that her
  current directory was `~/src/cnest/docs` and automagically keeps her in
  that directory inside the nest container.
* The files written by the build will be as the same Linux user `jane` with the
  usual file permissions working as in the host environment.
* There is pretty graphical symbol in the prompt within the nest container giving
  a visual cue that Jane is running software inside the container.


Part B: Building an image to be used for nest container creation
----------------------------------------------------------------

The container image provided by Read the Docs does not have all the required
components needed to use Sphinx.
An {download}`example Dockerfile <examples/readthedocs/Dockerfile>` replicates
the core aspects of the software environment and installations triggered by the
`.readthedocs.yaml` file for the sources of this documentation.

First, we see how the author of this documentation entered the directory of the
example Dockerfile.

```text
[castedo@nasa ~]$ cd ~/src/cnest/docs/examples/readthedocs/
[castedo@nasa readthedocs]$ ls
Dockerfile  requirements.txt
[castedo@nasa readthedocs]$
```

The `cnestify` is run on the `Dockerfile` in the current directory. A "nest sign" is
specified so that is may appear at the command line prompt inside nest containers created
from this image.

```text
[castedo@nasa readthedocs]$ cnestify --nestsign 📓 docker.io/castedo/share:rtd-4
+ buildah bud --layers --iidfile /tmp/tmpieq8nd8u/iidfile
...
[castedo@nasa readthedocs]$ podman images
REPOSITORY                         TAG                      IMAGE ID      CREATED         SIZE
docker.io/castedo/share            rtd-4                    4d37a9d9e041  16 minutes ago  6.52 GB
docker.io/readthedocs/build        ubuntu-20.04-2021.09.23  c54fcbdfb6c8  3 months ago    6.09 GB
[castedo@nasa readthedocs]$
```
With the image build from the Dockerfile and then _cnestified_, the image can
be pushed and shared with others.

```text
[castedo@nasa readthedocs]$ podman push docker.io/castedo/share:rtd-4 
Getting image source signatures
Copying blob 7a10b480ae4b done
...
Writing manifest to image destination
Storing signatures
[castedo@nasa readthedocs]$
```

Now other people can perform the steps in part A.

