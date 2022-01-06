import glob
import os
files = glob.glob('Mykey/*')
for f in files:
    os.remove(f)