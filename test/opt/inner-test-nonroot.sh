INNER_CONTAINER="nested"
set -x

mkdir -p ~/Downloads

create-cnest debian --volume $HOME/Downloads:$HOME/Downloads --name $INNER_CONTAINER

cnest $INNER_CONTAINER echo PASS
