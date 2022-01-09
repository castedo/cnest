if [ -n "$PS1" ] && [ -r /etc/nestsign ]; then
    NESTSIGN=$(cat /etc/nestsign)
    case "$PS1" in
    '\s-\v\$ ') # default bash prompt
        PS1="$NESTSIGN[\u@\h \W]\\$ "
        ;;
    *debian_chroot*)
        # fancy prompt on debian
        debian_chroot=$NESTSIGN
        ;;
    [*)
        PS1="$NESTSIGN$PS1"
        ;;
    esac
fi
