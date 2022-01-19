set -o errexit

INNER_CONTAINER="nested"
set -x

mkdir -p ~/Downloads
create-nest || true # ignore https://github.com/castedo/cnest/issues/10
create-nest only-downloads debian $INNER_CONTAINER
cnest $INNER_CONTAINER echo PASS
podman stop $INNER_CONTAINER
