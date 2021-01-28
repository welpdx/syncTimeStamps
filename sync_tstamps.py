#!/usr/bin/python

import os
import sys

for directory,subdirs,files in os.walk('.'):
    pathes=subdirs+files
    for path in pathes:
        fullpath=os.path.join(directory,path)
        target_path=os.path.join(sys.argv[1],fullpath)
        mtime=os.lstat(fullpath).st_mtime
        print('touching',target_path,':')
        try:
            os.utime(target_path,(mtime,mtime))
            print('OK')
        except:
            print('FAILED')