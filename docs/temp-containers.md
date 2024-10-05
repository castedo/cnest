Temporary Containers
====================

 Temporary containers are created on the fly before a containerized application is run.
When the application terminates, the container is automatically deleted.

As an example, let's say you have come across this great containerized application
[hub.docker.com/r/rancher/cowsay](https://hub.docker.com/r/rancher/cowsay).

You'll want to run it in a temporary container by using the `--rm` option of Podman as
such:

```
podman run --rm -it docker.io/rancher/cowsay moo moo mooooooo
```

For most containerized applications, there is little reason to persist and/or name the
container and then have to worry about deleting it later.

A more realistic scenario is one used by the author of this guide.  He wrote the
following bash script named `mkdocs` available in his host environment to run [Material
for MkDocs](https://squidfunk.github.io/mkdocs-material/):

```
#!/usr/bin/bash
podman run --rm -v .:/docs --network host docker.io/squidfunk/mkdocs-material "$@"
```

With the `-v .:/docs` option, the current working directory becomes available inside the
container. Thus, the author can perform the following to work on a document saved under
`~/src/mydoc`:

```
cd ~/src/mydoc
mkdocs --help
mkdocs serve
```

For a discussion of the many different ways containers can be used, [visit Fedora
Container Docs](https://docs.fedoraproject.org/en-US/containers/terminology/use_cases/).
