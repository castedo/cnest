Name: cnest
Version: 2.1
Release: 2%{?dist}
Summary: Simple scripts for personalized persistent controlled containers

License: MIT
URL: https://github.com/castedo/cnest
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
Requires: bash, coreutils
Requires: podman >= 4.4

# macro %{bash_completions_dir} is defined by the epel-rpm-macros package to
# %{_datadir}/bash-completion/completions

%description
Simple scripts for personalized persistent controlled containers designed
to be:
* personalized: with rootless podman into containers personalized for local user
* persistent: with mutable "pet" containers where you can interactively run dnf,
  apt-get, change settings, etc...
* controlled: isolated by default, home is not mounted, only a minimal number of podman
  options are enabled, additional options are passed through to podman

%prep
%autosetup -n cnest-%{version}

%build

%install
install -d %{buildroot}%{_bindir}
install -pm 0755 -t %{buildroot}%{_bindir} bin/cnest bin/cnest-ls bin/create-cnest
install -Dpm 0644 -t %{buildroot}%{bash_completions_dir} completion/cnest
ln -s cnest %{buildroot}%{bash_completions_dir}/create-cnest

%files
%{_bindir}/cnest
%{_bindir}/cnest-ls
%{_bindir}/create-cnest
%{bash_completions_dir}/cnest
%{bash_completions_dir}/create-cnest

%doc README.md
%license LICENSE

%changelog
* Tue Oct 08 2024 Castedo Ellerman <castedo@castedo.com> 2.1-2
- avoid UID collisions with image; no add sudo group (castedo@castedo.com)
- fix completion load delay (castedo@castedo.com)
* Thu Oct 03 2024 Castedo Ellerman <castedo@castedo.com> 2.0-1
- drop Python code, create-nest and other obsolete files (castedo@castedo.com)
- remove obsolete cnest-entry feature (castedo@castedo.com)
- remove obsolete cnestify script (castedo@castedo.com)
- use --init instead of --pid=host (castedo@castedo.com)
- don't set podman defaults (castedo@castedo.com)
- bash completion for cnest and create-cnest (castedo@castedo.com)
- new create-cnest and cnest-ls utilities (castedo@castedo.com)
- container name in prompt without touching hostname (castedo@castedo.com)

* Tue Sep 05 2023 Castedo Ellerman <castedo@castedo.com> 1.8-1
- v1.8 bump; hashbang /usr/bin (castedo@castedo.com)
- run sleep inf as root, not user (castedo@castedo.com)
- add container network name to /etc/hosts file (castedo@castedo.com)

* Sat Aug 27 2022 Castedo Ellerman <castedo@castedo.com> 1.7-2
- fix invalid --entry param default (issue #16) (castedo@castedo.com)
- Update install.md (castedo@castedo.com)

* Sat Apr 02 2022 Castedo Ellerman <castedo@castedo.com> 1.6-1
- move change of container directory logic into host cnest; 1.6
  (castedo@castedo.com)
- typos (castedo@castedo.com)
- add doc section about cnestify (castedo@castedo.com)
- fix out of date create-nest documentation (castedo@castedo.com)
- Fix issue #10; make smoketest less annoyingly slow (castedo@castedo.com)
- some tips-n-tricks for the docs (castedo@castedo.com)
- update pip install directions version (castedo@castedo.com)

* Mon Jan 17 2022 Castedo Ellerman <castedo@castedo.com> 1.5-2
- make rpm and Python package versions equal (castedo@castedo.com)

* Mon Jan 17 2022 Castedo Ellerman <castedo@castedo.com> 1.5-1
- cd to home when dir not match; cnestify run as root
- remove workdir setting in cnest (castedo@castedo.com)

* Thu Jan 13 2022 Castedo Ellerman <castedo@castedo.com> 1.4-1
- rpm using python package install
- fix bug caused by temp use of tags
- cnestify build from Dockerfile; robustness fixes
- bug fixes; more predictable behavior
- better error handling on permission profiles
- fix bugs; add groups and stowhome cnestify options
- port cnestify-image to Python
- pip installable
- no repository in profiles; new create-nest-by-tag
- new cnestify-image; elim build-nest-image
* Fri Jan 07 2022 Castedo Ellerman <castedo@castedo.com> 1.3-1
- Eliminate OSVIRTALIAS
- make cnest provide pwd and inode to container session
- eliminate hack sourcing from within profile files

* Sun Jan 02 2022 Castedo Ellerman <castedo@castedo.com> 1.2-1
- get single rpm working on fedora 35
- bug fixes
- include one profile for very isolated nests
- stop container when no more exec sessions

* Mon Sep 06 2021 Castedo Ellerman <castedo@castedo.com> 1-2
- new package built with tito

