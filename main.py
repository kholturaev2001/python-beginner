# deleting files using python ## NEEDS TO BE COMMITED AND PUSHED

import os
import shutil

try:
    path = 'empty_folder'
    os.rmdir(path)

except FileNotFoundError:
    print('That file was not found!')

except PermissionError:
    print("You don't have permission to delete that")

else:
    print(path + " was deleted")