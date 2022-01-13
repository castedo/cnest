Name: cnest
Version: 1.4
Release: 1%{?dist}
Summary: Simple scripts for personalized persistent controlled containers

License: MIT
URL: https://github.com/castedo/cnest
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
Requires: bash, coreutils
Requires: podman, buildah, skopeo
BuildRequires: python3-devel, python3-setuptools

%?python_enable_dependency_generator

%description
Simple scripts for personalized persistent controlled containers designed
to be:
* personalized: with rootless podman into containers personalized for local user
* persistent: with mutable "pet" containers where you can interactively run yum,
  apt-get, change settings, etc... in containers you don't want automatically
  deleted
* controlled: profiles picked by the user determine what capabilities are given
  to the container (isolation by default)

%prep
%autosetup -n cnest-%{version}

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/cnest
%{_bindir}/cnestify
%{_bindir}/create-nest
%{_bindir}/create-nest-by-tag
%{_bindir}/cnest-permission-definitions
%{_bindir}/guess-container
%{python3_sitelib}/cnest/
%{python3_sitelib}/cnest-%{version}*

%license LICENSE

%changelog
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

