Permission Profiles
===================

A permissions profile determines what permissions, resources and capabilities
to expose to a nest container.
These permissions are intended to mimic [flatpak permissions
](https://docs.flatpak.org/en/latest/sandbox-permissions.html).

To see what permissions profiles you can pick, run `create-nest` without any
parameters:
```
create-nest
```

The first time you run `create-nest` you should see only one pre-install profile
named [only-downloads
](https://github.com/castedo/cnest/blob/main/cnest/data/starter-profiles/only-downloads).

Permission profile files are located in `~/.config/cnest/profiles/`.
You can start with [only-downloads
](https://github.com/castedo/cnest/blob/main/cnest/data/starter-profiles/only-downloads)
as a bare-bones example for making your own custom permissions profiles.

```{warning}
In the cnest 1.x version series, a profile is just a shell script that will be
sourced by `create-nest`. But this is a proof-of-concept hack. cnest version
2.0 will likely switch to some more sane format.
```


Advanced Permissions
--------------------

The `cnest` package includes some useful predefined permissions that can be
sourced in custom permission profile files. Run

```bash
cnest-permission-definitions
```

to get a path to a shell script with useful permission definitions. In your own
permission profiles you can

```bash
source $(cnest-permission-definitions)
```

To see what permission definitions are available run

```bash
cat $(cnest-permission-definitions)
```

