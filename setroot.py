#!/usr/bin/env/python
"""setroot.py
Usage: setroot.py /path/to/project/root

Sets up the top-level project directory with an appropriate ACL.

If the directory does not exist it will be created.
"""

import sys
import posixpath

from qumulo.lib.request import RequestError


# set cluster IP, port, and admin creds in configuration.py
from configuration import *


def setroot(root):
    path, name = posixpath.split(root)
    print(path)
    print(name)
    try:
        RC.fs.create_directory(name=name, dir_path=path)
    except RequestError as e:
        if "fs_entry_exists_error" in str(e):
            print("WARNING: Directory exists")
    RC.fs.set_acl_v2(path=root, acl=PARENT_QACL)


if __name__ == '__main__':
    setroot(sys.argv[1])
