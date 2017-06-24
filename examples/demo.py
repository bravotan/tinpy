#!/usr/bin/env python

import tinpy 

import os
from pwd import getpwuid
from grp import getgrgid
from stat import S_ISDIR, ST_MODE, ST_UID, ST_GID
from time import time

start = time()    
dirmap = []
for fn in os.listdir('.'):
    st = os.stat(fn)
    if S_ISDIR(st[ST_MODE]):
        type = 'Directory'
    else:
        type = 'File'
    dirmap.append({'name': fn,
                   'type': type,
                   'owner': getpwuid(st[ST_UID])[0],
                   'group': getgrgid(st[ST_GID])[0]})
    
print(tinpy.build(open('demo.tpt').read(), 
            pwd=os.environ['PWD'], dirlist=dirmap,
            tekito={'hoge':'[% var hoge %]',}))
print('-' * 70)    
print('Ran (%3.3f sec)\n' % (time() - start))
