#!/usr/bin/env python

"""mktree.py -n PROJ_DIR_NAME -r PATH_TO_PROJ_ROOT
Usage: mktree.py

Creates a project skeleton inside a root set by mkroot.py that can't be deleted
or moved by regular users.
"""
import os
import argparse

from configuration import *


def create_parser():
    parser = argparse.ArgumentParser(description="Make a project skeleton")
    parser.add_argument('-r', '--root', help='desired parent directory of project directory skeleton',
                        required=True)
    parser.add_argument('-n', '--name', help='name of project directory',
                        required=True)
    return parser


def create_skeleton(args):
    RC.fs.create_directory(name=args.name, dir_path=args.root)
    skeleton_parent = os.path.join(args.root, args.name)
    for directory in DIRECTORY_SKELETON:
        full_path = os.path.join(skeleton_parent, directory)
        dir_path, name = os.path.split(full_path)
        RC.fs.create_directory(dir_path=dir_path, name=name)
        RC.fs.set_acl_v2(path=args.root, acl=CHILD_QACL)


def main():
    parser = create_parser()
    args = parser.parse_args()
    create_skeleton(args)


if __name__ == '__main__':
    main()
