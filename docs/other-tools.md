Other Alternatives
==================

This page provides some tips on alternative resources if you have any of the
following objectives:

* trying to run a GUI application that is NOT packaged for your Linux distro
* installed software to have access to all of your desktop environment
* seeking an isolation approach that also works without Linux

GUI applications
----------------

For desktop GUI applications, [flatpaks](https://flatpak.org/) are a more advanced and
appropriate approach than regular [OCI](https://opencontainers.org/) (Docker)
containers.
If the GUI application you want to run is available on [Flathub](https://flathub.org/)
(or similar source), you probably want to use that rather than running it
from an OCI container.

You can still try to run GUI applications out of a container. Using the `podman --network
host` option might be all you need to get your GUI application working to an acceptable
level.
You can also consider using convenient wrappers of Podman that have specific features
to help enable access to desktop environments:

* [Toolbx](https://containertoolbx.org)
* [Distrobox](https://github.com/89luca89/distrobox)
* [Podbox](https://github.com/DimaZirix/podbox)

<!-- copybreak -->

Full access to your desktop environment 
---------------------------------------

Tools like [distrobox](https://github.com/89luca89/distrobox) and
[toolbx](https://github.com/containers/toolbox) will by default grant full access to
your desktop environment.  Desktop features that work outside a container will probably work "out of
the box" in a container created by these tools.
In contrast, Podman will by default create containers that are highly isolated with limited
access to the host environment. 
There's a fundamental trade-off between giving software full access so that desktop features
automatically work vs running software in a contained, isolated system.

!!! tip "Author suggestion"
    When I want to access my full desktop environment from the shell command line, I
    don't run it in a container; I just run it in a regular shell session from
    a regular terminal window. I only run software in OCI containers that does NOT need
    full desktop access.


Isolation of macOS and Windows software
---------------------------------------

Most software development ecosystems evolve their own environment isolation solutions.
Usually, they are language-specific, such as Python's
[virtualenv](https://virtualenv.pypa.io) environments, or started out that way, such as
[conda](https://conda.io/), but now support many languages.
One benefit of these isolation
systems is they are cross-platform and can run natively on Windows or macOS without Linux.
In contrast, Podman uses the
[OS-level virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization) 
approach of Linux containers. Linux containers are not as portable, but they offer
a more extreme level of isolation.

You can also use [hardware
virtualization](https://en.wikipedia.org/wiki/Hardware_virtualization) to run
virtual machines (VMs) of Linux, macOS, or Windows on a desktop environment of a different
operating system.
