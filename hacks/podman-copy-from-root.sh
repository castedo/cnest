#!/bin/bash
set -o errexit

if [[ -z "$1" ]]; then
  echo "Usage: $0 {img}"
  exit 1
fi

sudo podman save $1 | podman load

