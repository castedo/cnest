set -o errexit

INNER_CONTAINER="nested"
set -x

mkdir -p ~/Downloads
create-nest isolated-docker-library debian $INNER_CONTAINER
cnest $INNER_CONTAINER echo PASS
podman stop $INNER_CONTAINER
