#!/usr/bin/env python3

import argparse, getpass
from contextlib import nullcontext
from importlib import resources
from pathlib import Path
from subprocess import run, PIPE


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
        run(['podman', 'inspect', self.cid, '--format={{.Name}}'], check=True)

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


def local_or_package(local, filename):
    packpath = resources.files(__package__) / "data" / filename
    return nullcontext(local) if local else resources.as_file(packpath)


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
    with local_or_package(args.userinit, "userinit") as p:
        container.run_bash_script(p, [args.user])
    with local_or_package(args.etc_profile_d, "nestprompt.sh") as p:
        container.copy(p, Path("/etc/profile.d/"))
    etc_nestsign = Path("/etc/nestsign")
    if args.nestsign or not container.exists(etc_nestsign):
        with local_or_package(args.nestsign, "nestsign") as p:
            container.copy(p, etc_nestsign)


if __name__ == '__main__':
    main()
