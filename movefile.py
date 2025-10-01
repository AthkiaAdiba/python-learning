import os

source = 'test.txt'
destination = 'C:\\Users\\HP\OneDrive\\Desktop\\test.txt'

try:
    if os.path.exists(source):
        print('This is already a file here.')
    else:
        os.replace(source, destination)
        print(source + " was moved.")
except FileNotFoundError:
    print(source + ' was not found')