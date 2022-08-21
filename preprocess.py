import os
import glob

for imgpath in glob.glob('./data/*'):
    if 'val_0004' not in imgpath:
        os.(imgpath)