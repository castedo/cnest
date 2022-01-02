Name: cnest
Version: 1.2
Release: 1%{?dist}
Summary: Simple scripts for personalized persistent controlled containers

License: MIT
URL: https://github.com/castedo/cnest
Source0: %{name}-%{version}.tar.gz

%define __brp_mangle_shebangs /usr/bin/true

BuildArch: noarch
Requires: bash, coreutils, findutils
Requires: podman, buildah, skopeo
Requires: python3

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
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install bin/cnest %{buildroot}%{_bindir}/
install bin/build-nest-image %{buildroot}%{_bindir}/
install bin/create-nest %{buildroot}%{_bindir}/
install bin/guess-container %{buildroot}%{_bindir}/

install -d %{buildroot}%{_sysconfdir}/cnest/
install config/default.env %{buildroot}%{_sysconfdir}/cnest/
install -d %{buildroot}%{_sysconfdir}/cnest/profiles/
install config/profiles/isolated-docker-library %{buildroot}%{_sysconfdir}/cnest/profiles/

%files
%{_bindir}/cnest
%{_bindir}/build-nest-image
%{_bindir}/create-nest
%{_bindir}/guess-container
%dir %{_sysconfdir}/cnest
%{_sysconfdir}/cnest/default.env
%dir %{_sysconfdir}/cnest/profiles
%{_sysconfdir}/cnest/profiles/isolated-docker-library
%license LICENSE

%changelog
* Sun Jan 02 2022 Castedo Ellerman <castedo@castedo.com> 1.2-1
- get single rpm working on fedora 35
- bug fixes
- include one profile for very isolated nests
- stop container when no more exec sessions

* Mon Sep 06 2021 Castedo Ellerman <castedo@castedo.com> 1-2
- new package built with tito

