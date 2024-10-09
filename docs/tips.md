Tips & Tricks
=============

In addition to the tips and tricks on this page, there are the following how-to guides:

* [How-To Sudo in a Container](howto/sudo.md)
* [How-To Stow in a Container](howto/stow.md)


`cnest-ls`
----------

As an alternative to running `podman ps -a`, you might prefer running the script
[`cnest-ls`](https://github.com/castedo/cnest/tree/main/bin/cnest-ls).
It is included with the `cnest` RPM package. But it's also short and simple, so you
might prefer making your own customized copy.


`create-cnest` filenames and tab autocompletion
-----------------------------------------------

If tab autocompletion is set up for `create-cnest`, then you can also
have a custom wrapper script reuse the same autocompletion by simply naming
the script `create-cnest`. For example, put a wrapper script inside
a directory `~/myfedbox` and then when you type the full path `~/myfedbox/create-cnest`,
it will get the benefit of autocompletion just like `create-cnest`.


`create-cnest` wrapper script "chaining"
----------------------------------------

If you have multiple scripts calling `create-cnest` with different options,
you can create a common base wrapper script by making sure it uses `"$@"` to
pass along non-common options to the final call to `create-cnest`.


`dnf history`
-------------

If you are running Fedora, CentOS, or a RHELative distro inside your container,
you can run `dnf history` to see how the container has been changed through
`dnf`.


`/var/log/apt/history.log`
--------------------------

If you are using an APT-based distro inside your container,
you can run
```
cat /var/log/apt/history.log | grep Commandline
```
to see how APT has modified the container.


`/etc/profile.d` and `~/bashrc.d`
---------------------------------

Depending on the distro inside the container, 
`/etc/profile.d` and `~/bashrc.d` are locations where scripts will be automatically run
when entering a container through `cnest`.
You can bind mount files into these locations with the `-v`/`--volume` option to set
customizations such as customizing the `$PS1` command line prompt.
