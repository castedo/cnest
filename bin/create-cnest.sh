#!/usr/bin/bash
set -o errexit -o pipefail -o nounset

if [[ $# -lt 1 ]]; then
    COMMAND=$'\u001b[1m'$(basename "$0")$'\u001b[0m'
    echo "Usage:"
    echo "  [USER=user] $COMMAND image [podman_create_options ...]"
    exit 2
fi

IMAGE=$1
shift
if [[ ! -v USER ]]; then
  USER=$(id -un)
fi

CONTAINER_NAME=$(podman create \
    --userns=keep-id \
    --uts=private \
    --cgroups=enabled \
    --pid=host \
    --user root \
    "$@" \
    $IMAGE \
    sleep inf)

podman inspect $CONTAINER_NAME --format={{.Name}}

podman start $CONTAINER_NAME > /dev/null
podman exec -i --user root $CONTAINER_NAME /bin/bash -s $USER <<'EOF'
  set -o nounset
  if command -v sudo > /dev/null; then
    NONROOTRUN="sudo -u $1"
  else
    NONROOTRUN="runuser -u $1 --"
  fi
  install -d -o $1 -g $1 /home/$1
  usermod --home /home/$1 $1
  $NONROOTRUN cp --recursive --preserve --no-clobber /etc/skel/. /home/$1
  passwd --delete $1 > /dev/null
  usermod --append --groups sudo $1 2> /dev/null || usermod --append --groups wheel $1
EOF
podman stop $CONTAINER_NAME > /dev/null

TEMPFILE=$(mktemp)
trap 'rm -f $TEMPFILE' EXIT

cat > $TEMPFILE <<'EOF'
  if [ -n "$PS1" ] && [ -r /etc/nestsign ]; then
      NESTSIGN=$(cat /etc/nestsign)
      case "$PS1" in
          '\s-\v\$ ') # default bash prompt
              PS1="$NESTSIGN$CONTAINER_NAME[\u@\h \W]\\$ " ;;
          *debian_chroot*)
              debian_chroot=$NESTSIGN$CONTAINER_NAME ;;
          [*)
              PS1="$NESTSIGN$CONTAINER_NAME$PS1" ;;
      esac
  fi
EOF
podman cp $TEMPFILE $CONTAINER_NAME:/etc/profile.d/nestprompt.sh

# check if /etc/nestsign exists by attempting copy to stdout
if ! podman cp $CONTAINER_NAME:/etc/nestsign - >/dev/null 2>&1; then
  # copy a default nestsign if one does not exist
  echo 📦 > $TEMPFILE
  podman cp $TEMPFILE $CONTAINER_NAME:/etc/nestsign
fi
