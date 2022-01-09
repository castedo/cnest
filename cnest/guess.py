#!/usr/bin/python3

import os, sys, subprocess

def guess_container(pattern):
    if 0 == subprocess.call(['podman', 'container', 'exists', pattern]):
        return pattern
    else:
        cmd = ['podman', 'ps', '--all', '--format={{.Names}}',
               '--filter', "name={}-\d+?".format(pattern)]
        out = subprocess.check_output(cmd).decode("utf-8")
        max_num = None
        for s in out.split('\n'):
            try:
                i = int(s[len(pattern)+1:])
                if max_num is None or i > max_num:
                    max_num = i
            except ValueError:
                pass
        if max_num is None:
          exit(1)
        return "{}-{}".format(pattern, max_num)

def main():
    if len(sys.argv) < 2:
        exit(os.EX_USAGE)
    print(guess_container(sys.argv[1]))

if __name__ == '__main__':
    main()

