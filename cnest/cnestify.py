import argparse
from subprocess import run, CalledProcessError, PIPE, DEVNULL

from cnest.getpath import getpath

def buildah(args, echo=True, check=True, **more):
    cmdlist = ['buildah'] + args
    if echo:
        print("+ " + " ".join(cmdlist))
    return run(cmdlist, check=check, **more)

def buildah_output(args, echo=True, **more):
    stderr = None if echo else DEVNULL
    result = buildah(args, echo=echo, stdout=PIPE, stderr=stderr, **more)
    ret = result.stdout.decode("utf-8").rstrip('\n')
    if echo:
        print(ret)
    return ret if result.returncode == 0 else None

def append_line(line, container, path, newline=True):
    sh_cmd = "echo" if newline else "echo -n"
    sh_cmd += " '{}' >> {}".format(line, path)
    buildah(['run', container, 'sh', '-c', sh_cmd])

def build_from_image(args):
    container = buildah_output(['from', args.from_image])
    try:
        buildah(['copy', container, args.entry, "/usr/bin/"])
        buildah(['copy', container, args.profile_d, "/etc/profile.d/"])
        append_line(args.nestsign, container, "/etc/nestsign", newline=False)
        buildah(['copy', container, getpath("nestkit"), "/opt/nestkit"])
        if args.groups:
            line = "usermod --append --groups {} $1".format(",".join(args.groups))
            append_line(line, container, "/opt/nestkit/boostuser")
        buildah(['commit', container, args.image_name])
    except CalledProcessError:
        exit(1)
    finally:
        buildah(['rm', container])

def build_using_dockerfile(image_name):
    """return image ID overwritten if any"""
    cmd = ['inspect', '--type', 'image', '--format', '{{.FromImageID}}', image_name]
    old = buildah_output(cmd, echo=False, check=False)
    buildah(['bud', '--layers', '--tag', image_name])
    return old

def main():
    parser = argparse.ArgumentParser(description="cnestify an image")
    parser.add_argument('image_name', help="image name")
    parser.add_argument('--from', help="use source image instead of Dockerfile",
        dest="from_image")
    parser.add_argument('--nestsign', help="nest sign", default='📦')
    parser.add_argument('--entry', help="cnest-entry file",
        default=getpath("cnest-entry"))
    parser.add_argument('--profile-d', help="profile.d directory",
        default=getpath("profile.d"), metavar="DIR")
    parser.add_argument('--groups', action='append', help="additional groups")
    args = parser.parse_args()

    old = None
    if not args.from_image:
        # want to buildah bud with image_name so that cached layers are not deleted
        old = build_using_dockerfile(args.image_name)
        args.from_image = args.image_name
    build_from_image(args)
    if old:
        buildah(['rmi', old], echo=False)


if __name__ == '__main__':
    main()

