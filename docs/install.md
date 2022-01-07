cnest installation
==================

[![Copr build status](https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/status_image/last_build.png)
](https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/)

Please [Email me](mailto:castedo@castedo.com) if you start using cnest or
create-nest and want backwards compatibility maintained.


RHEL 8
------

If you use a RHEL 8 based distro like me, then you can

```
yum copr enable castedo/cnest
yum install cnest
```
[Email me](mailto:castedo@castedo.com) if you want a copr package for another distro.


Fedora
------

I've built the RPM package to be Fedora friendly.
Chances are you can do the following:
```
yum install https://github.com/castedo/cnest/releases/download/cnest-1.3-1/cnest-1.3-1.el8.noarch.rpm
```
Check the github releases to make sure this rpm URL is the latest.


Future
------

I'm planning to make this package Python `pip` installable from the git repository.

