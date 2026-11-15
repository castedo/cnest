#!/usr/bin/env -S just --justfile

default:
  just --list

build-docs:
  mkdocs build

smoke-test:
  test/test-cnest-in-podman.sh

build-rpm:
  build-rpm-from-git cnest

build-test-rpm:
  build-rpm-from-git --work cnest
