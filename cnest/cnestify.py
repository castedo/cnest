import argparse
from subprocess import check_call, check_output, CalledProcessError 

from cnest.getpath import getpath

class Container:
    def __init__(self, src_img):
        self.cid = check_output(['buildah', 'from', src_img])
        self.cid = self.cid.decode("utf-8").rstrip('\n')

    def buildah(self, subcmd, args=[]):
        cmdlist = ['buildah', subcmd, self.cid] + args
        print("+ " + " ".join(cmdlist))
        check_call(cmdlist)

    def append_line(self, line, path, newline=True):
        sh_cmd = "echo" if newline else "echo -n"
        sh_cmd += " '{}' >> {}".format(line, path)
        self.buildah('run', ['sh', '-c', sh_cmd])

def main():
    parser = argparse.ArgumentParser(description="cnestify an image")
    parser.add_argument('src_img', help="source image")
    parser.add_argument('dst_img', help="destination image")
    parser.add_argument('--nestsign', help="nest sign", default='📦')
    parser.add_argument('--entry', help="cnest-entry file",
        default=getpath("cnest-entry"))
    parser.add_argument('--profile', help="profile.d directory",
        default=getpath("profile-d"))
    parser.add_argument('--groups', action='append', help="additional groups")
    args = parser.parse_args()

    container = Container(args.src_img)
    try:
        container.buildah('copy', [args.entry, "/usr/bin/"])
        container.buildah('copy', [args.profile, "/etc/profile.d/"])
        container.append_line(args.nestsign, "/etc/nestsign", newline=False)
        container.buildah('copy', [getpath("nestkit"), "/opt/nestkit"])
        if args.groups:
            line = "usermod --append --groups {} $1".format(",".join(args.groups))
            container.append_line(line, "/opt/nestkit/boostuser")
        container.buildah('commit', [args.dst_img])
    except CalledProcessError:
        exit(1)
    finally:
        container.buildah('rm')

if __name__ == '__main__':
    main()

