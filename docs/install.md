Installation
============

<a class="reference external" href="https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/">
  <img src="https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/status_image/last_build.png" alt="Copr build status"/>
</a>

Please [Email me](mailto:castedo@castedo.com) if you start using cnest or
create-nest and want backwards compatibility maintained.


RHEL &amp; Fedora
-------------------

If you use RHEL or Fedora, then you can

```text
yum copr enable castedo/cnest
yum install cnest
```
[Email me](mailto:castedo@castedo.com) if you want a copr package for another distro.


pip install
-----------

To install version 1.7 via pip from github:

```text
python3 -m pip install git+https://github.com/castedo/cnest.git@cnest-1.7-1
```

You can avoid installing it as root by doing a local user install by adding the
`--user` option in `pip`.

