# gitkeep

A simple script for Python (2 or 3), which assists in the addition of (a potentially large number of) empty directories to a git repository by adding a file to each such directory.

In each empty directory that is (recursively) found within a specified directory, `gitkeep` can create either an empty file called `.keep` or (for empty directories that shall always remain empty) a `.gitignore` file which ignores everything except itself. A third mode lists empty directories without creating any files.

Run the script without any arguments for usage instructions.