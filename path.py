import os

path = 'C:\\Users\\HP\\OneDrive\\Desktop\\folder'

if os.path.exists(path):
    print('This file path exist!')
    if os.path.isfile(path):
        print('This is a file!')
    elif os.path.isdir(path):
        print('This is a directory!')
else:
    print('This file does not exist!')