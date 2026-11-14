#!/usr/bin/env -S just --justfile

default:
  just --list

build-docs:
  mkdocs build

smoke-test:
  test/test-cnest-in-podman.sh
