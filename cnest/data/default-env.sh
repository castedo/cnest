
CNEST_SHARE_NETWORK="
    --network host
"

CNEST_X11="
    --volume /tmp/.X11-unix:/tmp/.X11-unix
"

CNEST_TMP_DIR=/tmp
WAYLAND_DISPLAY=wayland-0
CNEST_WAYLAND="
    --volume /run/user/$UID/$WAYLAND_DISPLAY:$CNEST_TMP_DIR/$WAYLAND_DISPLAY
    --env WAYLAND_DISPLAY=$WAYLAND_DISPLAY
    --env XDG_RUNTIME_DIR=$CNEST_TMP_DIR
"

CNEST_SYSTEM_BUS="
    --volume /run/dbus/system_bus_socket:/run/dbus/system_bus_socket
"

DBUS_SOCKET=/run/user/$UID/bus
CNEST_SESSION_BUS="
    --volume $DBUS_SOCKET:$DBUS_SOCKET
    --env DBUS_SESSION_BUS_ADDRESS=unix:path=$DBUS_SOCKET
"

PULSE_SOCKET=/run/pulse/native
PULSE_COOKIE=/run/pulse/cookie
CNEST_PULSEAUDIO="
    --volume /run/user/$UID/pulse/native:$PULSE_SOCKET
    --volume $HOME/.config/pulse/cookie:$PULSE_COOKIE
    --env PULSE_SERVER=unix:$PULSE_SOCKET
    --env PULSE_COOKIE=$PULSE_COOKIE
"

