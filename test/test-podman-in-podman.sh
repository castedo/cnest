#!/bin/bash
set -o errexit

if [[ -z "$1" ]]; then
  THIS_SCRIPT=$'\u001b[1m'"$(basename $0)"$'\u001b[0m'
  echo "Usage: $THIS_SCRIPT cnest_rpm_url"
  exit 1
fi

FLAGS="--privileged"
# More details: www.redhat.com/sysadmin/podman-inside-container
OUTER_CONTAINER="cnest_tester"
INNER_CONTAINER="nested"

set -x

podman run -d $FLAGS --name $OUTER_CONTAINER --user podman \
    quay.io/podman/stable sleep +Inf

podman exec --user root $OUTER_CONTAINER yum install -y $1

podman exec --user podman $OUTER_CONTAINER \
    mkdir -p /home/podman/Downloads

podman exec --user podman $OUTER_CONTAINER \
    create-nest isolated-docker-library debian $INNER_CONTAINER

podman exec --user podman $OUTER_CONTAINER \
    cnest $INNER_CONTAINER echo PASS

podman exec --user podman $OUTER_CONTAINER \
    podman stop $INNER_CONTAINER

podman stop $OUTER_CONTAINER

