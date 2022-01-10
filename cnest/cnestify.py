import argparse
from subprocess import check_call, check_output, CalledProcessError 

from cnest.getpath import getpath

def buildah(args):
    print("+ buildah " + " ".join(args))
    check_call(['buildah'] + args)

def main():
    parser = argparse.ArgumentParser(description="cnestify an image")
    parser.add_argument('src_img', help="source image")
    parser.add_argument('dst_img', help="destination image")
    parser.add_argument('--nestsign', help="nest sign", default='📦')
    parser.add_argument('--nestkit', help="nestkit directory",
        default=getpath("nestkit"))
    parser.add_argument('--entry', help="cnest-entry file",
        default=getpath("cnest-entry"))
    parser.add_argument('--profile', help="profile.d directory",
        default=getpath("profile-d"))
    args = parser.parse_args()

    container = check_output(['buildah', 'from', args.src_img])
    container = container.decode("utf-8").rstrip('\n')
    try:
        buildah(['copy', container, args.entry, "/usr/bin/"])
        buildah(['copy', container, args.nestkit, "/opt/nestkit"])
        buildah(['copy', container, args.profile, "/etc/profile.d/"])
        sh_cmd = "echo -n {} > /etc/nestsign".format(args.nestsign)
        buildah(['run', container, 'sh', '-c', sh_cmd])
        buildah(['commit', container,  args.dst_img])
    except CalledProcessError:
        exit(1)
    finally:
        buildah(['rm', container])

if __name__ == '__main__':
    main()

