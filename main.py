# deleting folder, which is not empty using python

import os
import shutil

path = 'folder'

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)

except FileNotFoundError:
    print('That file was not found!')
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("You can't delete that, using that function")


else:
    print(path + " was deleted")