from __future__ import print_function
import os
import sys

argv = sys.argv[1:]

modes = ["keep", "gitignore", "list"]
help = False
if len(argv) != 2:
    help = True
else:
    basedir = argv[1]
    if argv[0] in modes:
        mode = argv[0]
    else:
        help = True
if help:
    print("\n  usage: gitkeep <%s> <basedir>\n" % "|".join(modes))
    print("      gitkeep will create a file in all empty directories found in basedir depending on first argument:")
    print("              keep:  create empty file .keep")
    print("         gitignore:  create .gitignore which ignores everything except itself\n")
    print("              list:  create no files, list empty directories only\n")
    sys.exit(0)
    
for path, dirs, files in os.walk(basedir):
    if len(dirs) == 0 and len(files) == 0:
        if mode == "keep":
            newfile = os.path.join(path, ".keep")
            with open(newfile, "w") as f:
                pass
        elif mode == "gitignore":
            newfile = os.path.join(path, ".gitignore")
            with open(newfile, "w") as f:
                f.write("# Ignore everything in this directory\n")
                f.write("*\n")
                f.write("# Except this file\n")
                f.write("!.gitignore\n")
        elif mode == "list":
            newfile = path
        else: raise Exception("Unknown mode '%s'" % mode)
        print(newfile)
