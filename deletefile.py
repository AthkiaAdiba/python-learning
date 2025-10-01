import os
import shutil

path = 'empty_folder'

try:
    # os.remove(path)   # delete a file
    # os.rmdir(path)    # delete a empty folder
    shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print('That file was not found.')
except PermissionError:
    print('You do not have permission to delete that.')
except OSError:
    print('You can not delete that folder using this function.')
else:
    print(path + ' was deleted.')