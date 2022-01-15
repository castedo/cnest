How to share only part of your home directory
=============================================


After [installation](install.md), you can
```text
create-nest
```
to see available profiles. If this is the first time
running `create-nest` then a profile `only-downloads` has been copied to
`~/.config/cnest/profiles` for convenienice.

```text
mkdir -p ~/Downloads
create-nest only-downloads debian mynest
```
This creates a new container named `mynest` which is
highly isolated and only shares `~/Downloads` with the host.

To enter this new nest container do:
```text
cnest mynest
```

## Getting more out of cnest

To take full advantage of the extra features of `cnest` an image needs to have
some extra features. The `cnestify` takes a base image and creates a new
images with extra features enabled for `cnest`.

```text
cnestify --from fedora fedplus
```

now there's a new `localhost/fedplus` image with which you can create a new
nest:

```text
create-nest only-downloads fedplus mynest2
```

Now entering the container will benefit from some extra goodies:

```text
cd ~/Downloads
cnest mynest2
```

* Notice that `cnest` detected that you were in `~/Downloads` and that
  directory is the same inside the nest container. So `cnest` kept you in the
  same directory.
* You also have an emoji to let you know you're inside a container.
* Various distro extras like coloring have been enabled because the home
  directory has been populated with distro default home files like `.bashrc`
  instead of being an empty home directory.


