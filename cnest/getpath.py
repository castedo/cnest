import argparse
from pkg_resources import resource_filename

def getpath(name):
    return resource_filename(__name__, "data/" + name)

def main():
    parser = argparse.ArgumentParser(
        description="get path to cnest package data",
    )
    parser.add_argument('name', type=str, help='data resource name')
    args = parser.parse_args()
    print(getpath(args.name))

if __name__ == '__main__':
    main()

