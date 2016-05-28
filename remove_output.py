import glob
import os
for i in (glob.glob("output*.dxf")):
    if i.startswith('output'):
        os.remove(i)