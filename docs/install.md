Installation
============

There are two ways you can get `cnest`/`create-cnest`.


## Option 1: Just copy the Bash scripts

The `cnest` and `create-cnest` scripts are simple enough that you can just copy them
from [this Git repository](https://github.com/castedo/cnest/tree/main/bin) to your
`~/bin` directory (or similar).

If you want Bash auto-completion, you also need to run the script
[completion/cnest](https://github.com/castedo/cnest/blob/main/completion/cnest).
Alternatively, you can opt for installing the RPM, which will automatically set up Bash completion.


## Option 2: Install the RPM package

If you use RHEL, CentOS, or Fedora, you can

```text
dnf copr enable castedo/cnest
dnf install cnest
```
<a class="reference external" href="https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/">
  <img src="https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/status_image/last_build.png" alt="Copr build status"/>
</a>

Please [email Castedo](mailto:castedo@castedo.com) if you start using `cnest` or
`create-cnest` and want backward compatibility maintained.
