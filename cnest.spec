Name: cnest
Version: 1
Release: 2%{?dist}
Summary: Simple scripts for personal persistent parallel containers

License: MIT
URL: https://github.com/castedo/cnest
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
Requires: bash, coreutils, findutils
Requires: python3
Requires: podman, buildah, skopeo

%description
Simple scripts for personal persistent parallel containers designed to be:
* personal: with rootless podman into containers as same user
* persistent: with mutable "pet" containers where you can interactively run
  yum, apt-get, change settings, etc in containers you don't want auto deleted
* parallel: with multiple containers that all persist and are invoked by
  identifying a container name (pattern)

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

%changelog
* Mon Sep 06 2021 Castedo Ellerman <castedo@castedo.com> 1-2
- new package built with tito

