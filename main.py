# deleting files using python ## NEEDS TO BE COMMITED AND PUSHED

import os
import shutil

try:
    path = 'test.txt'
    os.remove(path)

except FileNotFoundError:
    print('That file was not found!')