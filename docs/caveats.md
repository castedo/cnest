Caveats
=======

Moving files or folders that are bind mounts
--------------------------------------------

If you use the `-v`/`--volume` option to bind mount paths in your host system,
you will need to preserve those paths.
Removing those paths will prevent containers from running.

Consider only mounting very stable paths of your host system and then rely on [GNU
Stow](howto/stow.md) to periodically move or delete files that are shared between
your container and host system.


Editing bind mounted files with certain editors
-----------------------------------------------

Bind mounting files can lead to confusing behavior when editing those
files using certain editors from the host system.
The result is editing and seeing changes to the file from the host system, but not
seeing the changes appear in the container until the container restarts.

This happens when the editor does not directly edit the file.  Some editors will rename
files to create a backup and then edit in a newly created file.  Vim, for instance, may do
this if the `backupcopy` setting is not set to `yes`. The default for Vim is not to have
`backupcopy` set to `yes`.  You can avoid this problem by having `set backupcopy=yes` in
your `vimrc` file.


CentOS 7 color emoji issues
---------------------------

There's some kind of TTY bug in CentOS 7 that gets triggered
by having a colorful emoji in the prompt. Using a monochrome
emoji like ✱ (echo $'\u2731') avoids the bug.
