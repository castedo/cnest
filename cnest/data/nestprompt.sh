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
