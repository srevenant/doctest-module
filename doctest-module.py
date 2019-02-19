#!/usr/bin/env python3

"""
This scans and doctests all files in a module

It is very hard to get this to work right; it should be a flaggable behavior for doctest to just
recursively scan all things in a module.
"""

import os
import sys
import doctest
import importlib
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="folder that is base module to search from")
    args = parser.parse_args()

    sys.path.append("src")
    importlib.invalidate_caches()

    for root, dir, files in os.walk(args.folder):
        for file in files:
            if file[-3:] != ".py":
                continue
            modfile = os.path.join(root, file)
            modname = modfile[:-3]
            modname = re.sub(os.path.sep + "__init__", "", modname)
            modname = re.sub(os.path.sep, ".", modname)
            print("===================================== " + modname)
            module = importlib.import_module(modname)
            (failed, total) = doctest.testmod(module, verbose=True)
            if failed:
                sys.exit(1)
