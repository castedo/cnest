How-To stow home config files
=============================

[GNU Stow](https://www.gnu.org/software/stow/) is a nice tool for making files
and directories available inside partially shared home directories inside
containers. This approach gives more flexibility than relying only on bind mounts
(podman --volume).
Other similar setups can be found on
[dotfiles.github.io](https://dotfiles.github.io/).


Steps
-----

### 1. Create a "stowage" folder for "stow packages" for $HOME

We'll choose `~/stowage` on your host system as a location for "stow packages".
But you can put it pretty much anywhere you like. You probably will enjoy having this
location under source control.


### 2. Create a "stow package" for $HOME

You can create multiple "stow packages". Each stow package contains files and paths that
you want replicated into a home folder in your container.

For instance, you could do the following for Vim config:

```
mkdir -p ~/stowage/sweethome/.vim
echo 'set mouse=a' > ~/stowage/sweethome/.vim/vimrc
```

This setup is to "install" the `sweethome` package which will place a `.vim/vimrc` file
in your home directory in your container.

### 3. Create a stowhome.sh script

```
echo 'stow -d $HOME/stowage -R sweethome' > ~/stowhome.sh
```

Running this script will cause the `sweethome` stow package to be "installed" into the
home directory.


### 4. Bind mount `stowage` and `stowhome.sh` in the container

Add the following creation options to your calls to `create-cnest` (or `podman`):

```
-v $HOME/stowage:$HOME/stowage -v $HOME/stowhome.sh:/etc/profile.d/stowhome.sh
```

You can change the location and name of `stowhome.sh`, but make sure it ends with `.sh`.


Explanation
-----------

When you run `cnest` without a command, it will run `bash --login` inside the container.
On most distros, this will cause all scripts in `/etc/profile.d/` ending in `.sh` to be
sourced (run).

By bind mounting `stowhome.sh` in `/etc/profile.d`, this will cause this script to be run
every time `cnest` is run (without a command).

The `stow` command will cause symlinks to be created in the "target" directory,
mapping to all the paths found inside the stow packages passed to `stow`.
The "target" directory is the parent directory of `$HOME/stowage`, which in this case, is
$HOME. See the GNU Stow documentation for more details.

Tips
----

Sometimes Stow gets confused and will report errors. Just start deleting some of the
symbolic links in $HOME in the container and rerun `stowhome.sh`.
Keeping the `~/stowage` file under source control should make this less scary.
