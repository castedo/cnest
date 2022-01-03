#!/bin/bash
set -o errexit

cd "$(dirname "$0")"

OPTIONAL_URL=$1
FLAGS="--privileged --pid=host --cgroups=enabled"
# More details: www.redhat.com/sysadmin/podman-inside-container
OUTER_CONTAINER="cnest_tester"
INNER_CONTAINER="nested"

set -x

podman run -d $FLAGS \
    --user podman \
    --name $OUTER_CONTAINER \
    quay.io/podman/stable \
    sleep +Inf

podman cp opt/. $OUTER_CONTAINER:/opt

podman exec --user root $OUTER_CONTAINER \
    bash /opt/inner-install-cnest.sh "$OPTIONAL_URL"

podman exec --user podman $OUTER_CONTAINER \
    bash /opt/inner-test-nonroot.sh

time podman stop $OUTER_CONTAINER

