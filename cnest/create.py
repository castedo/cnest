#!/usr/bin/env python3

import argparse, getpass, tempfile
from pathlib import Path
from subprocess import run, PIPE

def as_file(content: str, path: Path) -> Path:
    with open(path, 'w') as f:
        f.write(content)
    return path


class Container:
    def __init__(self, image: str, create_options: list[str]):
        cmdline = ['podman', 'create']
        cmdline += [
            '--userns=keep-id',
            '--uts=private',
            '--cgroups=enabled',
            '--pid=host',
            '--user=root',
        ]
        cmdline += create_options + [image, 'sleep', 'inf']
        result = run(cmdline, check=True, stdout=PIPE, encoding="utf-8")
        self.cid = result.stdout.rstrip('\n')

    def copy(self, src: Path, dst: Path) -> None:
        s = f"{src}/." if src.is_dir() else str(src)
        run(['podman', 'cp', s, f"{self.cid}:{dst}"], check=True)

    def exists(self, path: Path) -> bool:
        result = run(['podman', 'cp', f"{self.cid}:{path}", "-"], capture_output=True)
        return result.returncode == 0

    def run_bash_script(self, path: Path, args: list[str]) -> None:
        run(['podman', 'start', self.cid], check=True, capture_output=True)
        inner_cmd = ['/bin/bash', '-s'] + args
        cmdline = ['podman', 'exec', '-i', '--user', 'root', self.cid] + inner_cmd
        with open(path, 'r') as f:
            run(cmdline, check=True, stdin=f)
        run(['podman', 'stop', self.cid], check=True, capture_output=True)

    def print_name(self):
        run(['podman', 'inspect', self.cid, '--format={{.Name}}'], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="create a nest container")
    parser.add_argument('--nestsign', help="nest sign")
    parser.add_argument('--etc-profile-d', type=Path, help="/etc/profile.d script(s)")
    parser.add_argument('--userinit', type=Path, help="user init script")
    parser.add_argument('--user', default=getpass.getuser())
    parser.add_argument(
        'image', help="image reference", metavar="image [podman_create_options ...]"
    )
    args, unknown_args = parser.parse_known_args()

    container = Container(args.image, unknown_args)

    with tempfile.TemporaryDirectory() as tempdir:
        t = Path(tempdir)

        userinit = args.userinit or as_file(USERINIT, t / "userinit.sh")
        container.run_bash_script(userinit, [args.user])

        nestprompt = args.etc_profile_d or as_file(NESTPROMPT, t / "nestprompt.sh")
        container.copy(nestprompt, Path("/etc/profile.d/"))

        etc_nestsign = Path("/etc/nestsign")
        if not args.nestsign and not container.exists(etc_nestsign):
            args.nestsign = '📦'
        if args.nestsign:
            container.copy(as_file(args.nestsign, t / "nestsign"), etc_nestsign)

        container.print_name()


USERINIT = r'''
  set -o nounset
  if command -v sudo; then
    NONROOTRUN="sudo -u $1"
  else
    NONROOTRUN="runuser -u $1 --"
  fi
  install -d -o $1 -g $1 /home/$1
  usermod --home /home/$1 $1
  $NONROOTRUN cp --recursive --preserve --no-clobber /etc/skel/. /home/$1
  passwd --delete $1 > /dev/null
  usermod --append --groups sudo $1 2> /dev/null || usermod --append --groups wheel $1
'''

NESTPROMPT = r'''
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
'''

if __name__ == '__main__':
    main()
