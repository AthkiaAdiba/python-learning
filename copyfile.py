# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (files creation and modification time)

import shutil

shutil.copyfile('test.txt', 'copy.txt')  # src,dst