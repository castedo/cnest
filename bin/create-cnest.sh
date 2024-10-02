#!/usr/bin/bash
set -o errexit -o pipefail -o nounset

if [[ $# -lt 1 || ! -v USER ]]; then
    COMMAND=$'\u001b[1m'$(basename "$0")$'\u001b[0m'
    echo "Usage:"
    echo "  [USER=user] $COMMAND image [podman_create_options ...]"
    exit 2
fi

IMAGE=$1
shift

CONTAINER_ID=$(podman create \
    --userns=keep-id \
    --uts=private \
    --cgroups=enabled \
    --pid=host \
    --user=root \
    "$@" \
    $IMAGE \
    sleep inf)

podman inspect $CONTAINER_ID --format={{.Name}}

podman start $CONTAINER_ID > /dev/null

podman exec -i --user root $CONTAINER_ID \
  bash -s $USER <<'EOF'
  set -o nounset
  mkdir --parents /home/$1
  chown $1: /home/$1
  usermod --home /home/$1 $1
  usermod --append --groups sudo $1 2> /dev/null || usermod --append --groups wheel $1
  passwd --delete $1 > /dev/null
EOF

podman exec $CONTAINER_ID \
  cp --recursive --preserve --no-clobber /etc/skel/. /home/$USER

podman exec -i --user root $CONTAINER_ID \
  cp /dev/stdin /etc/profile.d/nestprompt.sh <<'EOF'
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

echo 📦 | podman exec -i --user root $CONTAINER_ID \
  cp --no-clobber /dev/stdin /etc/nestsign

podman stop $CONTAINER_ID > /dev/null