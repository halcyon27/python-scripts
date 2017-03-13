# use to rename files in dir according to single scheme
# files can be numbered or not according to file type

import sys, os

path = os.getcwd()
filename_new = sys.argv[1]
num_files = len([f for f in os.listdir(path)])
i = 1

for f in os.listdir(os.getcwd()):
    if f.endswith(".xml"):
		os.rename(f, filename_new + '_' + str(i) + f[-4:])
		print f + ' --> ' + filename_new + '_' + str(i) + f[-4:]
		i = i + 1
		continue
    if f.endswith(".txt") or f.endswith(".gpx") or f.endswith(".kml") or f.endswith(".kmz"):
		os.rename(f, filename_new)