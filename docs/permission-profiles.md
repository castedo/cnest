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
```
