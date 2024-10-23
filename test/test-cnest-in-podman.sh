#!/bin/bash
set -o errexit -o nounset

cd "$(dirname "$0")"

EXTRA_ARGS=""
if [[ -v 1 ]]; then
  EXTRA_ARGS+=" --build-arg RPM=$1"
fi

export NEST_IMAGES="
docker.io/debian:bookworm
docker.io/debian:trixie
docker.io/ubuntu:jammy
docker.io/ubuntu:oracular
registry.fedoraproject.org/fedora:40
registry.fedoraproject.org/fedora:41
"

for I in $NEST_IMAGES; do
  if ! podman image exists $I; then
    podman pull $I
  fi
done

PODMAN_IMAGES="
quay.io/podman/stable:v5.2.3
"

set -o xtrace

for PODMAN_IMG in $PODMAN_IMAGES; do
  TESTER_IMG="podman-tester/$PODMAN_IMG"

  if ! podman image exists $TESTER_IMG; then
      buildah build \
        --tag $TESTER_IMG \
        --build-arg PODMAN_IMG=$PODMAN_IMG \
        --layers \
        $EXTRA_ARGS \
        prep-image
  fi

  podman run \
      --rm \
      -it \
      --user podman \
      --userns=keep-id:uid=1000,gid=1000 \
      -v $PWD/storage.conf:/home/podman/.config/containers/storage.conf \
      -v $HOME/.local/share/containers/storage:/var/lib/shared:ro \
      -v $PWD/inner-test.sh:/opt/inner-test.sh \
      -e NEST_IMAGES \
      $TESTER_IMG \
      bash /opt/inner-test.sh
done
