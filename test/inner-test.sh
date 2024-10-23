#/usr/bin/bash
set -o nounset
set -x

mkdir -p ~/Downloads

for I in $NEST_IMAGES; do
  create-cnest $I -v $HOME/Downloads:$HOME/Downloads --name test
  cnest test echo PASS
  podman rm test
done
