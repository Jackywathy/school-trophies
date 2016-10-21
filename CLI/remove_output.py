import glob
import os
for i in (glob.glob("*.dxf")):
    os.remove(i)
for i in glob.glob("*.csv"):
    os.remove(i)