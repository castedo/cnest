#!/usr/bin/env -S just --justfile

default:
  just --list

build-docs:
  mkdocs build

smoke-test:
  test/test-cnest-in-podman.sh

test-build-rpm:
  rpmbuild -ba --build-in-place --noprep --define 'ignore_source 1' cnest.spec
