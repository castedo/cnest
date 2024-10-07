Installation
============

The Bash scripts [`cnest`](https://github.com/castedo/cnest/tree/main/bin/cnest)
and [`create-cnest`](https://github.com/castedo/cnest/tree/main/bin/create-cnest)
are independent scripts under 100 lines.
You can use them as-is or as examples for creating your own scripts calling `podman`.

Regardless, the quickest way to follow this guide and its tutorials is to install
`cnest` and `create-cnest` on your system.
Once you have `create-cnest` and `cnest` installed on your machine,
you're ready to [start a simple tutorial on how to use them](create-cnest-tutorial.md).

## Install option 1: Just copy the Bash scripts

The `cnest` and `create-cnest` scripts are simple enough that you can copy them
from [this Git repository](https://github.com/castedo/cnest/tree/main/bin) to your
`~/bin` directory (or a comparable location).

If you want Bash auto-completion, you need to run the script
[completion/cnest](https://github.com/castedo/cnest/blob/main/completion/cnest).
Alternatively, you can opt for installing the RPM, which will automatically set up Bash completion.


## Install option 2: Install the RPM package

If you use RHEL, CentOS, or Fedora, you can:

```text
dnf copr enable castedo/cnest
dnf install cnest
```
<a class="reference external" href="https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/">
  <img src="https://copr.fedorainfracloud.org/coprs/castedo/cnest/package/cnest/status_image/last_build.png" alt="Copr build status"/>
</a>

Please [email Castedo](mailto:castedo@castedo.com) if you start using `cnest` or
`create-cnest` and want backward compatibility maintained.
