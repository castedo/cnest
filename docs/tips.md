Tips &amp; Tricks
=================

GNU Stow
--------

[GNU Stow](https://www.gnu.org/software/stow/) is a nice tool for making files
and directories available inside partially shared home directories inside nest
containers. This approach gives more flexibilty than relying on only mount
volumes (podman --volume).
Other similar setups can be found on
[dotfiles.github.io](https://dotfiles.github.io/)


CentOS 7 color emoji issues
---------------------------

There's some kind of TTY bug in CentOS 7 that gets triggered
by having a colorful emoji in the prompt. Using a monochrome
emoji like ✱ (echo $'\u2731') avoids the bug.

