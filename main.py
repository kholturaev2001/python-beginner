# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copy2('test.txt', 'C:\\Users\\user\\Desktop\\copy.txt') # src, dst
