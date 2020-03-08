
if [ -z "$OSVIRTALIAS" ] && [ -r /etc/osvirtalias ]; then
  OSVIRTALIAS=$(cat /etc/virtosinstance)
fi

if [ "$PS1" ] && [ "$OSVIRTALIAS" ]; then
  PS1="[\u@\h"$'\xf0\x9f\x94\xb9'"$OSVIRTALIAS \W]\\$ "
fi

