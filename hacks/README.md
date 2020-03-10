hacks
=====

bugs with rootless containers
-----------------------------

You might hit bugs building images as non-root
(e.g. https://github.com/containers/fuse-overlayfs/issues/183).

If so, consider creating all images under sudo, and then create the container
as non-root after copying the needed image from root to non-root.
See [podman-copy-from-root.sh](podman-copy-from-root.sh). It's a hacky script
you can run as **non-root** to copy an image (e.g. "localnests/chromed-3") from
root's images to your personal rootless images.

